Prueba A/B de Vanguard - Equipo de Experiencia del Cliente (CX)
Introducción
Bienvenido al proyecto de Prueba A/B de Vanguard. Este proyecto explora un experimento digital lanzado por Vanguard, una compañía de gestión de inversiones con sede en EE. UU., para evaluar si una nueva interfaz de usuario (UI) más moderna y con mensajes en contexto puede mejorar las tasas de finalización del proceso en línea para los clientes.

Este proyecto fue desarrollado como parte de un bootcamp de análisis de datos, aplicando diversas técnicas como Análisis Exploratorio de Datos (EDA), Métricas de Rendimiento, Pruebas de Hipótesis y Evaluación de Experimentos.

Descripción del Proyecto
El equipo de CX de Vanguard lanzó una prueba A/B para determinar si una interfaz digital renovada resultaría en mayores tasas de finalización en el proceso de incorporación de clientes. El experimento se llevó a cabo del 15 de marzo de 2017 al 20 de junio de 2017, con dos grupos:

Grupo de Control: Los clientes interactuaron con el proceso en línea tradicional de Vanguard.
Grupo de Prueba: Los clientes utilizaron la nueva interfaz con características más modernas y mensajes en contexto.
El proceso incluyó varias etapas que todos los clientes siguieron: página inicial, tres pasos, y una página de confirmación que indica la finalización del proceso.

Objetivo
El objetivo del proyecto es:

Analizar el rendimiento de la nueva interfaz en términos de tasas de finalización.
Evaluar si el rediseño del proceso llevó a una experiencia de usuario más eficiente.
Conjuntos de Datos Utilizados
Se utilizaron tres conjuntos de datos para realizar este análisis:

Perfiles de Clientes (df_final_demo): Contiene detalles demográficos de los clientes, como edad, género, antigüedad con Vanguard y detalles de sus cuentas.
Huellas Digitales (df_final_web_data): Rastros detallados de las interacciones de los clientes con el proceso en línea, divididos en dos partes que se fusionaron para el análisis.
Registro del Experimento (df_final_experiment_clients): Información sobre qué clientes formaron parte de la prueba A/B y a qué grupo (Control o Prueba) pertenecían.
Campos Clave
client_id: Identificador único de cada cliente.
variation: Indica si el cliente estaba en el grupo de control o prueba.
process_step: La etapa del proceso digital.
clnt_age: Edad del cliente.
bal: Saldo total de las cuentas del cliente con Vanguard.
logons_6_mnth: Número de inicios de sesión en los últimos 6 meses.
Metodología
1. Análisis Exploratorio de Datos (EDA) y Limpieza de Datos
Fusión y limpieza de conjuntos de datos para preparar el análisis.
Exploración inicial de la demografía y los comportamientos de interacción de los clientes.
2. Métricas de Rendimiento
Identificación de los KPIs para medir el rendimiento de la nueva UI, centrado en las tasas de finalización y la efectividad en costos.
3. Pruebas de Hipótesis
Realización de pruebas A/B para determinar la significancia de las diferencias en las tasas de finalización entre los grupos de Control y Prueba.
Pruebas adicionales para evaluar la efectividad en costos y otros aspectos del rendimiento.
4. Evaluación del Experimento
Evaluación del diseño del experimento, su duración y posibles sesgos.
Sugerencias para experimentos futuros o datos adicionales que podrían haber mejorado el estudio.
5. Visualizaciones en Tableau
Uso de Tableau para crear visualizaciones interactivas que ilustren el rendimiento de la prueba A/B y proporcionen información sobre el comportamiento de los clientes.
Entregables
Jupyter Notebooks: Contienen el código para limpieza de datos, EDA, pruebas de hipótesis y otros análisis.
Scripts en Python: Todas las funciones reutilizables están organizadas en archivos .py para una mejor estructura.
Dashboards de Tableau: Dashboards interactivos para visualizar los hallazgos.
Presentación del Proyecto: Un conjunto de diapositivas que resume los hallazgos y presenta las conclusiones al equipo de CX de Vanguard.
Tablero Kanban: La gestión del proyecto se realizó mediante un tablero Kanban, que puede visualizarse aquí.
Instalación y Configuración
Requisitos
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias. Puedes instalarlas ejecutando:

bash
Copiar código
pip install -r requirements.txt
Ejecución del Proyecto
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/mjimcode/vanguard-ab-test.git
Ejecutar el Jupyter Notebook:

Inicia Jupyter Notebook y ejecuta el archivo EDA.ipynb para explorar los conjuntos de datos y realizar los análisis.

Ver las Visualizaciones en Tableau:

Los dashboards de Tableau pueden accederse a través del archivo de Tableau en el repositorio o mediante el enlace en la presentación.

Estructura del Proyecto
kotlin
Copiar código
vanguard-ab-test/
│
├── data/
│   ├── df_final_demo.csv
│   ├── df_final_web_data_pt_1.csv
│   ├── df_final_web_data_pt_2.csv
│   ├── df_final_experiment_clients.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── hypothesis_testing.ipynb
│
├── scripts/
│   ├── data_processing.py
│   ├── hypothesis_tests.py
│
├── tableau/
│   ├── vanguard_dashboard.twbx
│
├── requirements.txt
├── README.md
└── presentation/
    └── slides_link.txt
Trabajo en Equipo y Gestión del Proyecto
Este proyecto fue completado en parejas. Utilizamos un tablero Kanban para la gestión del proyecto, que puede visualizarse aquí. El tablero nos ayudó a dividir las tareas de manera eficiente y a seguir nuestro progreso a lo largo de las dos semanas de proyecto.

Conclusión
Nuestro análisis muestra que el nuevo diseño de la UI mejoró las tasas de finalización para los clientes de Vanguard, ofreciendo una experiencia de usuario más intuitiva. Basado en los hallazgos, recomendamos más mejoras en la UI y la realización de experimentos adicionales para explorar otras áreas potenciales de optimización.
