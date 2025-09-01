PulsoFoke – Sentiment Analysis of Casa Alofoke Live Chat

Project Overview

This project analyzes the sentiment and engagement of the audience during the live reality show Casa Alofoke, one of the most popular reality shows in the Dominican Republic. Using live chat messages and YouTube API data, this report tracks audience sentiment, mentions of participants, and engagement patterns throughout the show.

The analysis is presented in an interactive Power BI dashboard, designed for portfolio purposes and hosted on GitHub.

This project demonstrates how to process unstructured data — text from live chat messages — and transform it into actionable insights.

ETL Process

1. Extraction

Python (pytchat + YouTube API) was used to collect data:

Live chat messages from the YouTube stream (casa_alofoke_livechat_data.csv).

Concurrent viewers and total views every minute (casa_alofoke_livechat_ss.csv).

![Python execution screenshot](Portfolio/YouTube Live Chat Analys/assets/pythonexec.png)

For portfolio purposes, a static dataset covering a defined time range is included.

The API key used to extract live views is not included in the repository.

2. Transformation

Power Query was used for text cleaning and structuring unstructured data.

A custom column was created to extract mentions of specific participants from chat messages:

= Table.AddColumn(#"Changed Type", "Participante", each 
    if Text.Contains(Text.Lower([message]), "crucita") then "crucita"
    else if Text.Contains(Text.Lower([message]), "crazy") then "crazy"
    else if Text.Contains(Text.Lower([message]), "gigi") then "gigi"
    else if Text.Contains(Text.Lower([message]), "trujillo") then "trujillo"
    else if Text.Contains(Text.Lower([message]), "luise") then "luise"
    else if Text.Contains(Text.Lower([message]), "saltamonte") then "saltamonte"
    else if Text.Contains(Text.Lower([message]), "carlos") or Text.Contains(Text.Lower([message]), "carlo") then "saltamonte"
    else if Text.Contains(Text.Lower([message]), "alofoke") then "alofoke"
    else if Text.Contains(Text.Lower([message]), "carola") or Text.Contains(Text.Lower([message]), "karola") then "karola"
    else null
)

MinuteKey was created as a unique key for each minute:

MinuteKey = 
DATE(YEAR([timestamp]), MONTH([timestamp]), DAY([timestamp])) +
TIME(HOUR([timestamp]), MINUTE([timestamp]), 0)

A one-to-many relationship was established in Power BI:

casa_alofoke_livechat_ss[MinuteKey] → casa_alofoke_livechat_data[MinuteKey]
This allows correlating viewer behavior with participant mentions.

DAX measures were created to analyze:

Messages per minute

Mentions per participant

Viewer count trends

3. Load & Real-Time Analysis

Data loaded into Power BI for visualization.

Thanks to the structure with MinuteKey, this setup can be applied to live streams for real-time analysis:

Monitor spikes in viewers as participants are mentioned.

Detect sentiment trends in real time.

Observe engagement patterns minute by minute.

For the portfolio, static data is used, but the same structure allows real-time streaming analysis if connected to a live chat and the YouTube API.

Unstructured Data and Its Importance

Unstructured data refers to information without a predefined format (e.g., chat messages, social media posts, emails).

Analyzing unstructured data allows companies to extract meaningful insights, detect trends, understand audience behavior, and improve decision-making.

This project shows how to structure and relate unstructured chat data to numeric metrics (views) for both static and real-time analysis.

Potential Applications in Business

This methodology is generalizable beyond reality shows:

Competitor Analysis (Retail) – Track mentions and sentiment of competitor products.

Trend Identification on Social Media (X, TikTok, Instagram) – Detect emerging topics and viral content.

Product Launch Sentiment (E-commerce) – Measure customer reactions during a launch.

Customer Feedback During Promotions (Retail) – Identify questions, complaints, and engagement in live events.

Marketing & Media Strategy – Evaluate the performance of campaigns, influencers, or ad content.

Descripción del Proyecto

Este proyecto analiza el sentimiento y la interacción del público durante el reality show Casa Alofoke, uno de los más populares en la República Dominicana. Utiliza mensajes del chat y datos de YouTube para analizar menciones de participantes, tendencias de sentimiento y engagement de la audiencia, tanto de manera histórica como en tiempo real.

Proceso ETL

1. Extracción

Python (pytchat + API de YouTube) capturó:

Mensajes de chat (casa_alofoke_livechat_data.csv)

Vistas concurrentes y totales (casa_alofoke_livechat_ss.csv)

Para el portafolio, se utiliza data estática de un rango de tiempo definido.

La API key utilizada para la extracción no se incluye.

2. Transformación

Power Query limpió y estructuró los datos no estructurados.

Se creó la columna de Participante para identificar menciones en el chat:

= Table.AddColumn(#"Changed Type", "Participante", each 
    if Text.Contains(Text.Lower([message]), "crucita") then "crucita"
    else if Text.Contains(Text.Lower([message]), "crazy") then "crazy"
    else if Text.Contains(Text.Lower([message]), "gigi") then "gigi"
    else if Text.Contains(Text.Lower([message]), "trujillo") then "trujillo"
    else if Text.Contains(Text.Lower([message]), "luise") then "luise"
    else if Text.Contains(Text.Lower([message]), "saltamonte") then "saltamonte"
    else if Text.Contains(Text.Lower([message]), "carlos") or Text.Contains(Text.Lower([message]), "carlo") then "saltamonte"
    else if Text.Contains(Text.Lower([message]), "alofoke") then "alofoke"
    else if Text.Contains(Text.Lower([message]), "carola") or Text.Contains(Text.Lower([message]), "karola") then "karola"
    else null
)

Se creó MinuteKey como llave única por minuto:

MinuteKey = 
DATE(YEAR([timestamp]), MONTH([timestamp]), DAY([timestamp])) +
TIME(HOUR([timestamp]), MINUTE([timestamp]), 0)

Relación one-to-many:

casa_alofoke_livechat_ss[MinuteKey] → casa_alofoke_livechat_data[MinuteKey]
Esto permite analizar cómo el comportamiento de los views se relaciona con menciones de los participantes.

Medidas DAX para:

Mensajes por minuto

Menciones por participante

Comportamiento de las vistas

3. Carga y Análisis en Tiempo Real

Datos cargados en Power BI.

Gracias a la estructura con MinuteKey, esta configuración permite análisis en tiempo real:

Observar picos de audiencia cuando se mencionan participantes.

Detectar tendencias de sentimiento en tiempo real.

Analizar engagement minuto a minuto.

Para el portafolio, se usa data estática, pero la misma estructura permite conexión a un live stream real y análisis en vivo.

Datos No Estructurados y su Importancia

Los datos no estructurados son información que no tiene un formato predefinido, como mensajes de chat, publicaciones en redes sociales o correos electrónicos.

Analizarlos permite extraer insights, detectar tendencias y tomar decisiones estratégicas.

Este proyecto demuestra cómo convertir datos no estructurados en métricas accionables, tanto para análisis histórico como en tiempo real.

Usos Potenciales en Negocios

Análisis de Competencia (Retail) – Seguir menciones y sentimiento sobre productos de competidores.

Identificación de Tendencias en Redes Sociales – Detectar temas virales o cambios de preferencias del consumidor.

Sentimiento de Lanzamiento de Producto (E-commerce) – Evaluar reacciones durante el lanzamiento de un producto.

Retroalimentación en Promociones de Retail – Monitorear engagement y preguntas en eventos en vivo.

Estrategias de Marketing y Medios – Medir efectividad de campañas, influencers o promociones en tiempo real.
