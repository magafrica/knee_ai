import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import Counter
import numpy as np

df = pd.read_excel("./data/ESTUDIO_MENISCOS.xlsx")
df.rename( columns = {'\nNacionalidad': 'NACIONALIDAD', 'CIRUGÍA': 'Cirugia','TRAUMÁTICA': 'Traumatica',
       'DOLOR INTERLÍNEA': 'Dolor Interlinea', 'MCMURRAY +': 'MCMurray',
      'Anticoagulación': 'Anticoagulacion', 'Cáncer': 'Cancer', 
       'Cirugía Previa meniscal':'Cirugia Previa Meniscal' , 'Espacio Intraarticular (mm)': 'Espacio Intraarticular (mm)',
        'Ángulo 1': 'Angulo 1', 'Ángulo': 'Angulo', '\nLateralidad' : 'Lateralidad 2', '\nTipo de Rotura': 'Tipo de Rotura',
        'Raíz Meniscal': 'Raiz Meniscal', '\nExtrusión ( mm )': 'Extrusion', '\nEdema óseo': 'Edema Oseo',
        '\n\nCondropatía ': 'Condropatia', '\nGrado': 'Grado', '\nZona': 'Zona Condropatia',
       '\nCondropatía Femoropatelar': 'Condropatia Femoropatelar'}, inplace=True)

 
df = df.drop(columns = ['NACIONALIDAD', 'Trabajo', 'Zona Condropatia', 'Dolor en cuclilla', 'Reincorporación a vida laboral', 'Tratamiento', 'Unnamed: 56'
                                ,'Unnamed: 57', 'Reintervención',
       'Causa reintervención', 'Fracaso de tratamiento',
       'tiempo desde fracaso (meses)', 'Unnamed: 63', 'RMN POST',
       'Unnamed: 65', 'SUTURA VS MENISCECTOMIA'])       
#print(df.columns)
column_data = {}
#COLUMNA SEXO
#print(df["Sexo"].unique())
df_new = df.replace('mujer', 'MUJER')
df_new = df_new.replace('MUJER ', 'MUJER')
df_new = df_new.replace('Mujer', 'MUJER')
df_new = df_new.replace('varón', 'HOMBRE')
df_new = df_new.replace('Varón', 'HOMBRE')
df_new = df_new.replace('VARÓN', 'HOMBRE')
df_new = df_new.replace('VARON', 'HOMBRE')
df_new = df_new.replace('varon', 'HOMBRE')
df_new = df_new.replace('Varon', 'HOMBRE')
df_new = df_new.replace('hombre', 'HOMBRE')
column_data['Sexo'] = list((df_new['Sexo'].unique()))

#COLUMNA EDAD
#column_data["Edad"] = list(df_new["Edad"].describe())

#COLUMNA LATERALIDAD
df_new = df_new.replace('derecha', 'DERECHA')
df_new = df_new.replace('Derecha', 'DERECHA')
df_new = df_new.replace('izquierda', 'IZQUIERDA')
df_new = df_new.replace('Izquierda ', 'IZQUIERDA')
df_new = df_new.replace('Izquierda', 'IZQUIERDA')
column_data['Lateralidad'] = list(df_new['Lateralidad'].unique())

#COLUMNA CIRUGÍA
df_new = df_new.replace('MENISCECTOMIA PARCIAL', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('sutura', 'SUTURA')
df_new = df_new.replace('SUTURA - REANCLAJE', 'SUTURA')
df_new = df_new.replace('desbridamiento lesiones condrales', 'SUTURA')
df_new = df_new.replace('SUTURA A MURO', 'SUTURA')
df_new= df_new.replace('menisectomía', 'MENISECTOMIA')
df_new= df_new.replace('menisectomia', 'MENISECTOMIA')
df_new= df_new.replace('meniscectomia', 'MENISECTOMIA')
df_new= df_new.replace('meniscectomía', 'MENISECTOMIA')
df_new = df_new.replace('MENISECTOMÍA PARCIAL', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('menisectomia parcial', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('meniscectomia parcial', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('menisectomía parcial', 'MENISECTOMIA PARCIAL')
column_data['Cirugia'] = list(df_new['Cirugia'].unique())

#COLUMNA TRAUMATICA
df_new = df_new.replace('si', 'SI')
df_new = df_new.replace('Si', 'SI')
df_new = df_new.replace('no', 'NO')
df_new = df_new.replace('NO ', 'NO')
column_data['Traumatica'] = list(df_new['Traumatica'].unique())

#COLUMNA DOLOR INTERLINEA
df_new = df_new.replace('si ', 'SI')
df_new = df_new.replace('SI ', 'SI')
column_data['Dolor Interlinea'] = list(df_new['Dolor Interlinea'].unique()) 

#COLUMNa MCMurray
df_new = df_new.replace('no ', 'NO')
df_new = df_new.replace('No', 'NO')
df_new = df_new.replace(' SI', 'SI')
df_new = df_new.replace('+', 'SI')
df_new = df_new.replace('no concluyente', 'NO CONCLUYE')
column_data['MCMurray'] = list(df_new['MCMurray'].unique())

#COLUMNA IMC
#column_data["IMC"] = list(df_new["IMC"].describe())

#COLUMNA HTA
column_data["HTA"] = df_new['HTA'].unique()

#COLUMNA Cirugia Isquemica
column_data['C. Isquemica'] = list(df_new['C. Isquemica'].unique())

#COLUMNA Arritmia
column_data['Arritmia'] = list(df_new['Arritmia'].unique())

#COLUMNA Displemia
column_data['Dislipemia'] = list(df_new['Dislipemia'].unique())

#COLUMNA Anticoagulacion
column_data['Anticoagulacion'] = list(df_new['Anticoagulacion'].unique())

#COLUMNA Fumador
column_data['Fumador'] = list(df_new['Fumador'].unique())

#COLUMNA DM
column_data['DM'] = list(df_new['DM'].unique())

#COLUMNA Insulina
column_data['Insulina'] = list(df_new['Insulina'].unique())

#COLUMNA Cancer
column_data['Cancer'] = list(df_new['Cancer'].unique())

#COLUMNA Insuficiencia Renal
column_data['Insuficiencia renal'] = list(df_new['Insuficiencia renal'].unique())

#COLUMNA SAOS
column_data['SAOS'] = list(df_new['SAOS'].unique())

#COLUMNA Anticoagulacion
column_data['Parkinson'] = list(df_new['Parkinson'].unique())

#COLUMNA Sd. Ansioso Depresivo
column_data['Sd. Ansioso Depresivo'] = list(df_new['Sd. Ansioso depresivo'].unique())

#COLUMNA Fibromialgia
column_data['Fibromialgia'] = list(df_new['Fibromialgia'].unique())

#COLUMNA LCA
column_data['Cirugia Previa LCA'] = list(df_new['Cirugia Previa LCA'].unique())

#COLUMNA CIRUGIA PREVIA MENISCAL
column_data['Cirugia Previa meniscal'] = list(df_new['Cirugia Previa Meniscal'].unique())

#COLUMNA ESPACIO INTRARTICULAR 
#column_data['Espacio Intraarticular (mm)'] = list(df_new['Espacio Intraarticular (mm)'].describe())

#COLUMNA ESCLEROSIS SUBCONDRAL
#print('Valores unicos en Esclerosis Subcondral: ' + list(df_new['Esclerosis subcondral'].unique())) + '\n'
column_data['Escleroris subcondral'] = list(df_new['Esclerosis subcondral'].unique())

#COLUMNA OSTEOFITO
column_data['Osteofito'] = list(df_new['Osteofito'].unique())

#COLUMNA Genu Varo
column_data['Genu varo'] = list(df_new['Genu varo'].unique())

#COLUMNA Angulo 1
#column_data['Angulo 1'] = list(df_new['Angulo 1'].describe())

#COLUMNA Genu Valgo
column_data['Genu valgo'] = list(df_new['Genu valgo'].unique())

#COLUMNA Angulo
#column_data['Angulo'] = list(df_new['Angulo'].describe())

#COLUMNA Kellgren
column_data['Kellgren'] = list(df_new['Kellgren'].unique())

#COLUMNA Lateralidad
#print(df_new['Lateralidad'].unique())
df_new = df_new.replace('Medial', 'MEDIAL')
df_new = df_new.replace('medial', 'MEDIAL')
df_new = df_new.replace('externo', 'EXTERNO')
df_new = df_new.replace('interno', 'INTERNO')
df_new = df_new.replace('Lateral', 'LATERAL')
df_new = df_new.replace('ambos', 'AMBOS')
df_new = df_new.replace('Medial + lateral', 'AMBOS')
df_new = df_new.replace('Ninguna', 'NO')
df_new = df_new.replace('bilateral', 'LATERAL')
df_new['Lateralidad 2']= df_new['Lateralidad 2'].replace(['DERECHA', 'IZQUIERDA'], 'LATERAL')
column_data['Lateralidad 2'] = list(df_new['Lateralidad 2'].unique())

#COLUMNA Tipo de Rotura
df_new = df_new.replace('compleja', 'COMPLEJA')
df_new = df_new.replace('Compleja', 'COMPLEJA')
df_new = df_new.replace('HORIZONTAL COMPLEJA', 'COMPLEJA')
df_new = df_new.replace('Oblicua', 'OBLICUA')
df_new = df_new.replace('oblicua', 'OBLICUA')
df_new = df_new.replace('horizontal', 'HORIZONTAL')
df_new = df_new.replace('degenerativa', 'DEGENERATIVA')
df_new = df_new.replace('Degenerativa', 'DEGENERATIVA')
df_new = df_new.replace('Degenerativa ', 'DEGENERATIVA')
df_new = df_new.replace('raiz + asa de cubo', 'COMPLEJA')
df_new = df_new.replace('radial', 'RADIAL')
df_new = df_new.replace('Radial', 'RADIAL')
df_new = df_new.replace('asa DE CUBO', 'ASA DE CUBO')
df_new = df_new.replace('Asa de cubo', 'ASA DE CUBO')
df_new = df_new.replace('asa de cubo', 'ASA DE CUBO')
df_new = df_new.replace('Horizontal', 'HORIZONTAL')
df_new = df_new.replace('pico de loro', 'PICO DE LORO')
df_new = df_new.replace('Pico de loro', 'PICO DE LORO')
column_data['Tipo de Rotura'] = list(df_new['Tipo de Rotura'].unique())

#COLUMNA Zona Menisco
df_new = df_new.replace('Cuerno posterior', 'CUERNO POSTERIOR')
df_new = df_new.replace('cuerno posterior', 'CUERNO POSTERIOR')
df_new = df_new.replace('Cuerno posterior ', 'CUERNO POSTERIOR')
df_new = df_new.replace('CUERNO POSTERIOR ', 'CUERNO POSTERIOR')
df_new = df_new.replace('Cuerno anterior', 'CUERNO ANTERIOR')
df_new = df_new.replace('cuerno anterior', 'CUERNO ANTERIOR')
df_new = df_new.replace('cuerpo', 'CUERPO')
df_new = df_new.replace('Cuerpo', 'CUERPO')
df_new = df_new.replace('CUERNO POSTERIOR + CUERPO', 'DOS')
df_new = df_new.replace('CAME y cuerpo', 'DOS')
df_new = df_new.replace('Cuerno posterior ME', 'DOS')
df_new = df_new.replace('cuerno posterior y cuerpo', 'DOS')
df_new = df_new.replace('cuerpo y cuerno posterior', 'DOS')
df_new = df_new.replace('Cuerpo-cuerno posterior', 'DOS')

column_data['Zona Menisco'] = list(df_new['Zona Menisco'].unique())

#COLUMNA Raiz Meniscal
column_data['Raiz Meniscal'] = list(df_new['Raiz Meniscal'].unique())

#COLUMNA Extrusion
df_new = df_new.replace('o,3', 0.3)
df_new = df_new.replace('rm horus', 0)
df_new['Extrusion'] = df_new['Extrusion'].replace(['SI', 'NO'], 0)
#column_data['Extrusion'] = list(df_new['Extrusion'].describe())

#COLUMNA Edema Oseo
df_new = df_new.replace('Si ', 'SI')
column_data['Edema Oseo'] = list(df_new['Edema Oseo'].unique())

#COLUMNA Grado
df_new['Grado'] = df_new['Grado'].replace(['III', 'iii'], 3)
df_new['Grado'] = df_new['Grado'].replace(['IV', 'iv'], 4)
df_new['Grado'] = df_new['Grado'].replace(['I', 'i'], 1)
df_new['Grado'] = df_new['Grado'].replace(['II', 'ii'], 2)
df_new['Grado'] = df_new['Grado'].replace(['II-III', 'ii\niiI'], 2.5)
df_new['Grado'] = df_new['Grado'].replace(['II-IV'], 3.5)
df_new['Grado'] = df_new['Grado'].replace(['I-II'], 1.5)
#column_data['Grado'] = list(df_new['Grado'].describe())

#COLUMNA Tipo Edema
df_new = df_new.replace('complee', 'COMPLETE')
df_new = df_new.replace('complete', 'COMPLETE')
df_new = df_new.replace('Edge', 'EDGE')
df_new = df_new.replace('edge', 'EDGE')
df_new = df_new.replace('Articular', 'ARTICULAR')
df_new = df_new.replace('articular', 'ARTICULAR')
df_new = df_new.replace('E', 'EDGE')
df_new = df_new.replace('Full', 'FULL')

column_data['tipo edema'] = list(df_new['tipo edema'].unique())

#COLUMNA Condropatia
df_new = df_new.replace('sí', 'SI')
column_data['Condropatia'] = list(df_new['Condropatia'].unique())

#COLUMNA Condropatía Femoropatelar
df_new = df_new.replace(' no', 'NO')
df_new = df_new.replace('ni', 'NO')
column_data['Condropatia Femoropatelar'] = list(df_new['Condropatia Femoropatelar'].unique())

#COLUMNA LCA
df_new = df_new.replace('PARCIAL', 'SI')
column_data['LCA'] = list(df_new['LCA'].unique()) 

#COLUMNA Quiste baker
column_data['Quiste Baker'] = list(df_new['Quiste baker'].unique())

#COLUMNA Quiste parameniscal
column_data['Quiste parameniscal'] = list(df_new['Quiste parameniscal'].unique())


json_dic = {}
for col in df_new:
       if col not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular (mm)', 'Kellgren', 'Extrusion', 'lysholm score post', 'Cancer', 'Grado']:
              content = str(df_new[col].unique())
       json_dic[str(col)] = content
  
#df_new.to_csv("./data/datos_procesados.csv", sep = ";", encoding="utf-8")
json_object = json.dumps(json_dic, indent=4)
with open("./data/unique_values.json", "w") as outfile:
    outfile.write(json_object)
    
json_describe = df_new.describe()
json_describe = json_describe.to_json()
print(json_describe)
json_describe = json.dumps(json_describe,indent=4 )
with open("./data/statistis.json", "w") as outfile:
    outfile.write(json_describe)

df_to_plot = df_new
df_to_plot.drop(columns=['lysholm score post', 'mejora con la cirugía',
       'satisfecho con la cirugía (1-4)', 'dolor actual 0-10',
       'Incorporación vida laboral', 'Deporte'], axis = 1, inplace=True)
percent_missing = df_new.isnull().sum() * 100 / len(df_to_plot)
missing_value_df = pd.DataFrame({'column_name': df_to_plot.columns,
                                 'percent_missing': percent_missing})
#print(missing_value_df)
missing_value_df.plot(x='column_name', y='percent_missing', kind='bar')
plt.title('Porcentaje de valores sin rellenar de 142 filas')
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
plt.hist(ordered_data, bins=4, edgecolor='black')
plt.xticks(category_order)
plt.xlabel('Rango')
plt.ylabel('Frecuencia')
plt.title('Lysholm Score')
plt.savefig("./data/graficas/lysholm_categories.png")
plt.show()