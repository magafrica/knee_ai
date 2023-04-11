import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

df = pd.read_csv('./data/datos_procesados.csv', delimiter=';')
df_to_plot = df.drop(columns=["Unnamed: 0", "NHC", 'lysholm score post'])



percent_missing = df_to_plot.isnull().sum() * 100 / len(df_to_plot)
missing_value_df = pd.DataFrame({'column_name': df_to_plot.columns,
                                 'Porcentaje': percent_missing,
                                  })
percent_missing = percent_missing.to_list()
columns = df_to_plot.columns.to_list()       
threshold = 50

# Asignar colores basado en el umbral
colors = np.where(missing_value_df['Porcentaje'] >= threshold, '#d34040', '#4090d3')
        
#print(missing_value_df)
missing_value_df.plot(x='column_name', y='Porcentaje', kind='barh', color=colors)
plt.title('Porcentaje de valores sin rellenar')
plt.savefig('./data/graficas/Missing_values.png')
plt.show()

lysholm_score_list = list(df["lysholm score post"])
for i in range(len(lysholm_score_list)):
       lysholm_score_list[i] = int(lysholm_score_list[i])
       
for i in range(len(lysholm_score_list)):
       if lysholm_score_list[i] < 65:
              lysholm_score_list[i] = "poor"
       elif lysholm_score_list[i] >= 65 and lysholm_score_list[i]< 83:
              lysholm_score_list[i] = "fair"
       elif lysholm_score_list[i] >= 83 and lysholm_score_list[i]< 95:
              lysholm_score_list[i] = "good"
       else:
              lysholm_score_list[i] = "excellent"

category_order = ['poor', 'fair', 'good', 'excellent']

# Define los datos
data = ['poor', 'fair', 'good', 'excellent', 'excellent' , 'poor', 'poor', 'excellent', 'good', 'excellent', 'good', 'excellent', 'excellent', 'poor', 'excellent', 'good', 'poor', 'excellent', 'good', 'poor', 'fair', 'good', 'poor', 'poor', 'poor', 'fair', 'excellent', 'fair', 'good', 'poor', 'excellent', 'fair', 'excellent', 'excellent', 'excellent', 'excellent', 'poor', 'poor', 'fair', 'excellent', 'good', 'poor', 'poor', 'poor', 'poor', 'good', 'fair', 'poor', 'poor', 'poor', 'excellent', 'poor', 'excellent', 'poor', 'excellent', 'poor', 'poor', 'good', 'poor', 'poor', 'excellent', 'fair', 'excellent', 'excellent', 'good', 'fair', 'poor', 'excellent', 'good', 'good', 'poor', 'poor', 'good', 'excellent', 'excellent', 'excellent', 'poor', 'excellent', 'poor', 'good', 'poor', 'good', 'good', 'good', 'excellent', 'fair', 'good', 'good', 'poor', 'poor', 'good', 'poor', 'poor', 'fair', 'poor', 'poor', 'fair', 'poor', 'good', 'good', 'poor', 'good', 'poor', 'good', 'excellent', 'fair', 'fair', 'poor', 'poor', 'poor', 'fair', 'poor', 'excellent', 'poor', 'fair', 'poor', 'poor', 'good', 'poor', 'excellent', 'poor', 'poor', 'good', 'poor', 'excellent', 'excellent', 'excellent', 'good', 'excellent', 'poor', 'poor', 'excellent', 'poor', 'fair', 'poor', 'excellent', 'fair', 'good', 'poor', 'poor', 'excellent', 'poor']

# Crea un objeto de categoría y ordena los valores
cat_data = pd.Categorical(data, categories=category_order, ordered=True)
ordered_data = pd.Series(cat_data)

# Grafica el histograma ordenado
plt.hist(ordered_data, bins=4, color= '#4090d3', edgecolor='black')
plt.xticks(category_order)
plt.xlabel('Rango')
plt.ylabel('Frecuencia')
plt.title('Lysholm Score')
#plt.savefig("./data/graficas/lysholm_categories.png")
plt.show()

#GRAFICA ESTABILIIDAD
with open('./data/statistics.json', 'r') as f:
    data = json.load(f)
    
column_name = []
stability = []   
for entry in data:
    print(data[entry])
    if entry not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular', 'Kellgren', 'Extrusion', 'lysholm score post', 'Angulo Genu Varo', 'Angulo Genu Valgo', 'Grado', 'Espacio Intraarticular (mm)']:
        column_name.append(entry)
        stability.append(data[entry]["stability"])
        

stability_value_df = pd.DataFrame({'column_name': column_name,
                                 'Estabilidad': stability,
                                  })
            
#print(missing_value_df)
# Establecer umbral
threshold = 0.85

# Asignar colores basado en el umbral
colors = np.where(stability_value_df['Estabilidad'] >= threshold, '#d34040', '#4090d3')

# Graficar
stability_value_df.plot(x='column_name', y='Estabilidad', kind='barh', color=colors)

# Mostrar la grafica
plt.title('Estabilidad de los Atributos')
plt.savefig('./data/graficas/Stability_values.png')
plt.show()