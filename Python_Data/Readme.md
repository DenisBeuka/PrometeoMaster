# Análisis de Campaña de Marketing Bancaria

Este proyecto consiste en el análisis de datos de una campaña de marketing realizada por una entidad bancaria. Los datos provienen de dos fuentes: un archivo CSV principal (bank-additional.csv) y un archivo Excel complementario (customer-details.xlsx) con información de los clientes. El objetivo es limpiar, procesar y visualizar estos datos para obtener conclusiones sobre el perfil de los clientes y su respuesta ante la campaña.

Primero se importaron las librerías necesarias y se definieron las rutas de los archivos. A continuación, se cargaron los datos del CSV y se realizó una limpieza básica: se convirtieron los valores numéricos que venían con comas a punto decimal, se cambió el formato de la columna de fechas para adaptarlo al formato español y se eliminaron filas con datos nulos en columnas clave como la edad o la respuesta a la campaña. 

Luego, se cargaron todas las hojas del archivo Excel, se renombró la columna de identificación para hacer coincidir ambos conjuntos de datos y se realizó la unión de ambos DataFrames.

Una vez obtenido el conjunto de datos completo, se guardó una versión procesada en formato CSV. Después se realizaron análisis estadísticos básicos, como distribución por profesión, edad media, estado civil, nivel educativo, tipo de vivienda y si los clientes tienen préstamos. También se imprimió el número de personas que aceptaron o rechazaron la campaña.

En general se puede ver en el código los pasos y las explicaciones de cada linea

Para completar el trabajo, se incluyeron varias visualizaciones que ayudan a entender mejor los datos. Se generó un histograma con la distribución de edades, un gráfico de barras para mostrar la aceptación de la campaña según la profesión, un diagrama de caja para comparar la edad de quienes aceptaron y no aceptaron, y una matriz de correlación para observar las relaciones entre las variables numéricas.

Todo el proyecto está realizado con un enfoque claro, utilizando Python y librerías como pandas, seaborn y matplotlib. 
