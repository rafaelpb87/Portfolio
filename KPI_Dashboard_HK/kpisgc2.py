import pandas as pd
import plotly.express as px

# Load CSVs
reportes = pd.read_csv('reportes.csv')
metas = pd.read_csv('metas.csv')
eficacia = pd.read_csv('eficaciaproc.csv')

# Parse dates
reportes['Fecha de Reporte'] = pd.to_datetime(reportes['Fecha de Reporte'], format='%m/%d/%Y')

# Month mapping
month_order = {
    'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
    'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
}
eficacia['Month_Num'] = eficacia['Mes'].map(month_order)
eficacia = eficacia.sort_values(['Proceso', 'Month_Num'])

processes = reportes['Proceso'].unique()

# Overall charts
avg_month = eficacia.groupby('Mes', sort=False)['Eficacia'].mean().reset_index()
avg_process = eficacia.groupby('Proceso')['Eficacia'].mean().reset_index()

fig_line = px.line(avg_month, x='Mes', y='Eficacia', markers=True, title='Eficacia promedio por mes')
fig_bar = px.bar(avg_process, x='Proceso', y='Eficacia', title='Eficacia promedio por proceso')

# HTML + CSS
html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Desempeño del Sistema de Gestión de la Calidad</title>
<script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
<style>
body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f9f9f9; color: #333; }
.sidebar { width: 250px; background: #2c3e50; padding: 20px; height: 100vh; position: fixed; overflow-y: auto; }
.sidebar h2 { color: #ecf0f1; }
.sidebar ul { list-style: none; padding: 0; }
.sidebar li { margin: 10px 0; }
.sidebar a { text-decoration: none; color: #ecf0f1; font-weight: bold; }
.sidebar a:hover { color: #1abc9c; }
.main { margin-left: 270px; padding: 10px 20px; width: calc(100% - 270px); overflow-x: hidden; }
.section { margin-bottom: 40px; }

/* Flex row for charts */
.chart-row { display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px; justify-content: flex-start; }
.chart-container { flex: 1 1 calc(48% - 15px); max-width: calc(48% - 15px); min-width: 300px; background: #fff; padding: 10px; border-radius: 8px;
                   box-shadow: 0 3px 8px rgba(0,0,0,0.1); box-sizing: border-box; }
.chart-container > div { width: 100% !important; height: auto !important; }
h1, h2 { margin-bottom: 15px; font-size: 1.3em; }
</style>
</head>
<body>
<div class="sidebar">
<h2>Menú</h2>
<ul>
<li><a href="#eficacia_sgc">Eficacia del Sistema de Gestión de la Calidad</a></li>
"""

for proc in processes:
    proc_id = proc.replace(' ', '_').lower()
    html += f'<li><a href="#{proc_id}">{proc}</a></li>\n'

html += """
</ul>
</div>
<div class="main">
"""

# Overall charts
fig_line.update_layout(autosize=True, height=300, margin=dict(l=20,r=20,t=30,b=20))
fig_bar.update_layout(autosize=True, height=300, margin=dict(l=20,r=20,t=30,b=20))

html += '<div id="eficacia_sgc" class="section">\n<h1>Eficacia del Sistema de Gestión de la Calidad</h1>\n'
html += '<div class="chart-row">\n'
html += f'<div class="chart-container">{fig_line.to_html(full_html=False, include_plotlyjs=False)}</div>\n'
html += f'<div class="chart-container">{fig_bar.to_html(full_html=False, include_plotlyjs=False)}</div>\n'
html += '</div>\n</div>\n'

# Sections per process
for proc in processes:
    proc_id = proc.replace(' ', '_').lower()
    html += f'<div id="{proc_id}" class="section"><h1>{proc}</h1>\n'
    df_proc = reportes[reportes['Proceso'] == proc]
    indicators = df_proc['Indicador'].unique()

    html += '<div class="chart-row">\n'
    for i, ind in enumerate(indicators):
        df_ind = df_proc[df_proc['Indicador'] == ind].sort_values('Fecha de Reporte')
        fig = px.line(df_ind, x='Fecha de Reporte', y='Resultado Reportado', title=ind, markers=True)
        fig.update_layout(autosize=True, height=280, margin=dict(l=20,r=20,t=30,b=20))

        # Add goals
        meta_row = metas[metas['Indicador'] == ind]
        if not meta_row.empty:
            meta1 = meta_row['Meta1'].values[0]
            meta2 = meta_row['Meta2'].values[0]
            tendencia = meta_row['Tendencia'].values[0]

            fig.add_hline(y=meta1, line_dash="dash", line_color="green",
                          annotation_text="Meta1", annotation_position="right")
            if pd.notna(meta2) and meta2 != '':
                fig.add_hline(y=meta2, line_dash="dash", line_color="red",
                              annotation_text="Meta2", annotation_position="right")

            colors = []
            for val in df_ind['Resultado Reportado']:
                if tendencia == 'Ascendente':
                    colors.append('green' if val >= meta1 else 'red')
                elif tendencia == 'Descendente':
                    colors.append('green' if val <= meta1 else 'red')
                elif tendencia == 'Rango' and pd.notna(meta2):
                    colors.append('green' if meta1 <= val <= meta2 else 'red')
                else:
                    colors.append('blue')
            fig.update_traces(marker=dict(color=colors))

        html += f'<div class="chart-container">{fig.to_html(full_html=False, include_plotlyjs=False)}</div>\n'

        if (i + 1) % 2 == 0 and i + 1 < len(indicators):
            html += '</div>\n<div class="chart-row">\n'

    html += '</div>\n</div>\n'

html += '</div></body></html>'

with open('sgc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML dashboard generated: sgc_dashboard.html")
