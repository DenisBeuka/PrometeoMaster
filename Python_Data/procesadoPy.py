# importamos lo necesario
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns # para gráficos
import os

# aqui se encuentra todas las rutas
base_path = os.path.dirname(__file__)  # ruta del archivo actual
csv_path = os.path.join(base_path, "datos", "bank-additional.csv")  # ruta del CSV principal

excel_path = os.path.join(base_path, "datos", "customer-details.xlsx")  # ruta del Excel
output_path = os.path.join(base_path, "procesado")  # ruta para guardar el CSV limpio
os.makedirs(output_path, exist_ok=True)  # crea carpeta si no existe

df = pd.read_csv(csv_path, encoding="utf-8")

# cambio para mejor legibilidad
df['cons.price.idx'] = df['cons.price.idx'].astype(str).str.replace(",", ".").astype(float)  # cambio coma por punto

df['cons.conf.idx'] = df['cons.conf.idx'].astype(str).str.replace(",", ".").astype(float)

df['euribor3m'] = pd.to_numeric(df['euribor3m'].astype(str).str.replace(",", "."), errors='coerce')  # convertir a número

# para nulos
df = df.dropna(subset=['age', 'y'])

# pongo las fechas a formato de españa
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y", errors='coerce')





#  (primero defino xls, luego lo uso)
xls = pd.ExcelFile(excel_path)  # defino el archivo Excel

customer_df = pd.concat([xls.parse(sheet) for sheet in xls.sheet_names])  # concateno todas las hojas del Excel




# renombro la columna "ID" a "id_" para poder hacer el merge
customer_df.rename(columns={"ID": "id_"}, inplace=True)
# uno ambos datasets por la columna "id_"
df_merged = df.merge(customer_df, on="id_", how="left")

# aqui se guarfa el dataset limpio
df_merged.to_csv(os.path.join(output_path, "data_limpia.csv"), index=False)

# analisis de datos extenso

print("-----------------------------------------------------------------")
print("Cantidad de clientes por educación:", df_merged['education'].value_counts())
print("-----------------------------------------------------------------")
print("Cantidad de clientes por tipo de vivienda:", df_merged['housing'].value_counts())
print("-----------------------------------------------------------------")
print("Cantidad de clientes por tipo de crédito:", df_merged['loan'].value_counts())
print("-----------------------------------------------------------------")
print("Distribución por profesión:", df_merged['job'].value_counts())
print("-----------------------------------------------------------------")
print("Edad media de los profesionales:", df_merged['age'].mean().round(2)) #para que no me de demasiados decimales y llene de ruido
print("-----------------------------------------------------------------")

print("Cantidad de clientes por estado civil:", df_merged['marital'].value_counts())
print("-----------------------------------------------------------------")

print("Clientes que aceptaron la campaña:", df_merged['y'].value_counts())
print("-----------------------------------------------------------------")

#  de edad por respuesta a la campaña

plt.figure(figsize=(12, 5))  # ---> tamaño de la figura
sns.boxplot(data=df_merged, x="y", y="age", palette={"yes": "purple", "no": "gold"})  # ---> colores personalizados
plt.title("Comoportamiento de la edad por respuesta a la campaña")
plt.xlabel("Respuesta (y)")

plt.ylabel("Edad")
plt.tight_layout()  # ---> ajusta el diseño
plt.show()
  


# GRÁFICO de aceptación por profesión
plt.figure(figsize=(12, 6))
sns.countplot(data=df_merged, x="job", hue="y", palette={"yes": "green", "no": "red"})  
plt.title("Aceptación de la campaña por profesión")
plt.ylabel("Cantidad")

plt.xticks(rotation=0, ha='center')  
plt.tight_layout()
plt.show()



# MATRIZ DE CORRELACIÓN
corr_df = df_merged.select_dtypes(include=['float64', 'int64'])  # selecciono columnas numéricas
corr_df = corr_df.loc[:, ~corr_df.columns.str.contains('^Unnamed')]  # elimino columnas automáticas si hay

plt.figure(figsize=(14, 10))  # tamaño grande para que se vea bien
sns.heatmap(corr_df.corr(), annot=True, fmt=".2f", cmap="plasma", linewidths=0.5, annot_kws={"size": 7})  # colores chulos
plt.title("Matriz de correlación", fontsize=12)

plt.xticks(rotation=90, ha='right', fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.show()

# HISTOGRAMA DE EDADES
sns.set_theme(style="darkgrid")  # estilo de gráfico
plt.figure(figsize=(8, 4))  # tamaño medio

df_merged['age'].hist(bins=20, color='purple', edgecolor='gold')  # bins = número de barras
plt.title("Distribución de edades")
plt.xlabel("Edad")

plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()
