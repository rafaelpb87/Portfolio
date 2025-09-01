import pytchat
import pandas as pd
import os
import time
from datetime import datetime
from googleapiclient.discovery import build

API_KEY = "INTRODUCE YOUR API KEY HERE"
VIDEO_ID = "gOJvu0xYsdo"
OUTPUT_DIR = "DIRECTORY FOR THE 2 DATASETS TO BE CREATED"

CHAT_FILE = os.path.join(OUTPUT_DIR, "casa_alofoke_livechat_data.csv")
SNAPSHOT_FILE = os.path.join(OUTPUT_DIR, "casa_alofoke_livechat_ss.csv")

youtube = build("youtube", "v3", developerKey=API_KEY)

chat = pytchat.create(video_id=VIDEO_ID)

chat_data = []
snapshot_data = []
latest_concurrent = None
latest_views = None

def get_live_stats(video_id):
    """Fetch concurrent viewers & view count for the live video."""
    request = youtube.videos().list(
        part="liveStreamingDetails,statistics",
        id=video_id
    )
    response = request.execute()
    
    if "items" in response and len(response["items"]) > 0:
        item = response["items"][0]
        live_details = item.get("liveStreamingDetails", {})
        stats = item.get("statistics", {})
        
        concurrent = live_details.get("concurrentViewers", None)
        views = stats.get("viewCount", None)
        
        return concurrent, views
    return None, None

print(f"Saving chat log → {CHAT_FILE}")
print(f"Saving snapshots → {SNAPSHOT_FILE}")

last_snapshot = time.time()

while chat.is_alive():
    # Process chat messages
    for c in chat.get().sync_items():
        chat_data.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "author": c.author.name,
            "message": c.message,
            "concurrent_viewers": latest_concurrent,
            "view_count": latest_views
        })
    
    # Save chat to CSV frequently
    if chat_data:
        df_chat = pd.DataFrame(chat_data)
        df_chat.to_csv(CHAT_FILE, index=False, encoding="utf-8-sig")
    
    # Take a snapshot every 60 seconds
    if time.time() - last_snapshot >= 60:
        concurrent, views = get_live_stats(VIDEO_ID)
        latest_concurrent, latest_views = concurrent, views
        
        snapshot_data.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "concurrent_viewers": concurrent,
            "view_count": views
        })
        df_snap = pd.DataFrame(snapshot_data)
        df_snap.to_csv(SNAPSHOT_FILE, index=False, encoding="utf-8-sig")
        
        print(f"[{datetime.now()}] Snapshot saved → viewers={concurrent}, views={views}")
        last_snapshot = time.time()
    
    time.sleep(5)  # reduce CPU usage


