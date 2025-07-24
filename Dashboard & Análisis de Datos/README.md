Proyecto: Análisis del Mercado Laboral en el sector IT del nicho de la inteligencia artificial
-----------------------------------------------------------------------------------------------
Este proyecto tiene como objetivo explorar el mercado laboral a través del análisis de datos reales. Para ello, se ha realizado un proceso completo de limpieza, transformación y análisis visual mediante Google Sheets, con el fin de presentar conclusiones claras y útiles sobre la situación actual en distintos países.
Los datos fueron obtenidos de un conjunto abierto de un enlace proporcionado en formato CSV. Para facilitar el análisis, he reducido el tamaño del csv a 2030 filas de las más 50.000 que tenia el archivo original. Que sigue cumpliendo el requisito de una extensión de mínimo 10 columnas y al menos 2000 filas

**Limpieza y transformación de los datos**
De los DATOS_CRUDOS extraje los DATOS_TRANSFORMADOS.
Durante esta etapa se realizaron los siguientes cambios:
Se cambiaron los nombres de las columnas para que fueran más claros y estuvieran en español.
Se tradujeron siglas y abreviaturas a términos completos y comprensibles (por ejemplo, EN se cambió a "Principiante", EX a "Experto").
Se eliminó información redundante, como la columna de moneda (moneda_salario), ya que todos los salarios estaban en dólares.
Las fechas se transformaron al formato español (dd/mm/aaaa) y se convirtieron a tipo fecha
Se ocultaron columnas vacías o que no aportaban valor al análisis.
Y se ha revisado si existen datos faltantes 

**Análisis descriptivo**

Se elaboró una hoja de resumen con estadísticas agrupadas por país, que incluye:
Total de personas trabajadoras.
Salario medio (en dólares estadounidenses).
Porcentaje de trabajo remoto.
Nivel de estudios y experiencia predominantes.
Tipo de contrato más común.
Cantidad y porcentaje de profesionales con doctorado.
Tamaño típico de empresa.
Este resumen permite comparar fácilmente la situación laboral en diferentes regiones.

 Dashboard visual (Google Sheets)
Para facilitar la interpretación de los resultados, se creó un dashboard interactivo con los siguientes cinco gráficos clave:
Mapa geográfico por pais: muestra los años de experiencia más común en cada territorio. En la que se divide en tres grupos y que marco en la leyenda
Gráfico combinado: representa en barras el número total de trabajadores por país y en línea el porcentaje de trabajo remoto.
Gráfico de rosquilla 3D: visualiza la distribución del porcentaje de doctorados por país.
Gráfico circular: presenta el recuento de los tipos de contrato más habituales.
Análisis comparativo por país: empleo, salarios y nivel educativo combinados en un solo gráfico para entender mejor el mercado laboral en cada nación.

**Acceso al documento**

El proyecto completo,aqui tambine incluye los datos en crudos , los transformados, el resumen y el dashboard:

https://docs.google.com/spreadsheets/d/1Fzytm0NqA3wLZcH_JxI8PLCYss9PKCxipClp9n4C6jE/edit?usp=sharing
En acceso en modo lectura como me indican

Conclusiones:
Según lo observado , el empleo promedio suele ser de medio tiempo (40%)
Tienen un nivel de trabajadores remotos que rondan el 50% en cada país
El número de doctorados respecto a los diferentes niveles educativos no superan el 30% del computo total
Y suelen tener un sueldo que oscilan entre 85.000 dolares mensuales hasta los 166.600