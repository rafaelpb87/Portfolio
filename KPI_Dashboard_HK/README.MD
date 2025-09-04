**Process Indicators Dashboard / Dashboard de Indicadores de Procesos**

English:
This project demonstrates my ability to transform semi-structured and unstructured data into actionable insights. I built an interactive KPI dashboard in Python + Plotly, replicating the structure of a corporate webpage. Unlike static reports or BI tools limited by licensing, this dashboard runs on any browser, updates automatically with fresh data, and integrates seamlessly with advanced analytics.

Español:
Este proyecto demuestra mi capacidad para transformar datos semi-estructurados y no estructurados en información accionable. Creé un dashboard interactivo de KPIs en Python + Plotly, que replica la estructura de una página corporativa. A diferencia de reportes estáticos o herramientas BI con licenciamiento, este dashboard se abre en cualquier navegador, se actualiza automáticamente con nuevos datos y se integra fácilmente con analítica avanzada.

**Project Overview**

English:
The dashboard centralizes process KPIs, automates data extraction from diverse sources, and provides interactive visualizations for stakeholders.

Español:
El dashboard centraliza KPIs de procesos, automatiza la extracción de datos de diversas fuentes y entrega visualizaciones interactivas para las partes interesadas.

Note / Nota:

Indicator names were modified.

Data was altered for privacy.

**Tech Stack**

Python 3.11 → Core programming language

Pandas → Data manipulation

Datetime / OS → Parsing + file handling

Plotly → Interactive charts

HTML + CSS → Dashboard structure

📚 Libraries Used: pandas, plotly, datetime, os

**Main Challenge**

English:
The hardest part was capturing data from multiple sources, most of them unstructured.

The Sales to Clients process data was extracted from SQL Server via query.

Other indicators came from reporting tools.

Example: For the % of legal services completed on time, I built a Power Automate app that fed a SharePoint list with internal client requests.

To ensure data integrity, a Python-based ETL pipeline was built to extract, consolidate, and validate the data automatically, reducing manual errors.

In this portfolio, the centralized datasets are shown:

reportes.csv → raw centralized reports.

metas.csv → goals and thresholds for KPIs.

eficaciaproc.csv → process performance over time.

Español:
El mayor reto fue capturar datos de múltiples fuentes, en su mayoría no estructuradas.

El proceso de Ventas a Clientes se extrajo desde SQL Server con un query.

Otros indicadores provenían de herramientas de reporte.

Ejemplo: Para el % de servicios legales completados en plazo, se creó una app en Power Automate que alimentaba una lista de SharePoint con solicitudes de clientes internos.

Para garantizar la integridad de los datos, se construyó un pipeline ETL en Python que extraía, consolidaba y validaba los datos automáticamente, reduciendo errores manuales.

En este portafolio se muestran las tablas centralizadas:

reportes.csv → reportes centralizados.

metas.csv → metas y umbrales de KPIs.

eficaciaproc.csv → desempeño de procesos por mes.

**Features**

KPIs loaded from .csv files

Goal lines (Meta1, Meta2) included automatically

Dynamic coloring of results (green/red based on compliance)

Sidebar navigation by process and indicator

Automatic ETL: running the Python script extracts, transforms, and loads new data into the dashboard

Hoshin Kanri Alignment

English:
The project was designed within the framework of Hoshin Kanri (Policy Deployment) — a strategic planning methodology that aligns an organization’s long-term vision (True North) with annual objectives, KPIs, and daily operations.
By centralizing KPIs and automating their validation, this dashboard ensures data integrity and provides stakeholders with reliable insights to monitor strategic execution.

Español:
El proyecto fue diseñado en el marco de Hoshin Kanri (Despliegue de Políticas), una metodología de planeación estratégica que alinea la visión de largo plazo (True North) con objetivos anuales, KPIs y operaciones diarias.
Al centralizar KPIs y automatizar su validación, este dashboard asegura la integridad de los datos y brinda a las partes interesadas información confiable para monitorear la ejecución de la estrategia.

**Benefits**
Why Python + Plotly instead of Power BI?

English:
While Power BI is a strong BI tool, Python + Plotly offers:

Handles semi-structured and unstructured data (APIs, logs, live chats, SharePoint)

Automated ETL: just run the program, and the dashboard refreshes with new data

No licenses required: dashboards run in any browser as .html

Advanced analytics ready: integrates with ML, NLP, and statistics libraries

Full design control beyond Power BI’s format limitations

Best for:

Heterogeneous or semi-structured data sources

Fully automated reporting pipelines

Companies avoiding Power BI licensing costs

Dashboards that need predictive/advanced analytics

Español:
Aunque Power BI es excelente, Python + Plotly ofrece ventajas:

Manejo de data semi-estructurada y no estructurada (APIs, logs, chats en vivo, SharePoint)

ETL automatizado: basta con ejecutar el programa y el dashboard se refresca con nueva data

Sin licencias: los dashboards funcionan en cualquier navegador como .html

Analítica avanzada lista: integración con ML, NLP y librerías estadísticas

Control total de diseño más allá de las restricciones de Power BI

Especialmente útil cuando:

Las fuentes son heterogéneas o semi-estructuradas

Se necesita automatizar reportes de principio a fin

Se quiere evitar costos de licencias Power BI

Se deben integrar modelos predictivos o analítica avanzada
