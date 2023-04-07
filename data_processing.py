import pandas as pd
import matplotlib.pyplot as plt
import json

df = pd.read_excel("./data/ESTUDIO_MENISCOS.xlsx")
print(df.columns)

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
print('Valores unicos en Sexo: ' + str(df_new["Sexo"].unique()))
column_data['Sexo'] = str((df_new["Sexo"].unique())) + '\n'

#COLUMNA LATERALIDAD
df_new = df_new.replace('derecha', 'DERECHA')
df_new = df_new.replace('Derecha', 'DERECHA')
df_new = df_new.replace('izquierda', 'IZQUIERDA')
df_new = df_new.replace('Izquierda ', 'IZQUIERDA')
df_new = df_new.replace('Izquierda', 'IZQUIERDA')
print('Valores unicos en Lateralidad: ' + str(df_new["Lateralidad"].unique()))
column_data['Lateralidad'] = str(df_new["Lateralidad"].unique()) + '\n'

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
print('Valores unicos en Cirugia: ' + str(df_new["Cirugia"].unique()))
column_data['Cirugia'] = str(df_new["Cirugia"].unique()) + '\n'

#COLUMNA TRAUMATICA
df_new = df_new.replace('si', 'SI')
df_new = df_new.replace('Si', 'SI')
df_new = df_new.replace('no', 'NO')
df_new = df_new.replace('NO ', 'NO')
print('Valores unicos en Traumatica: ' + str(df_new['Traumatica'].unique()))
column_data['Traumatica'] = str(df_new["Traumatica"].unique()) + '\n'

#COLUMNA DOLOR INTERLINEA
df_new = df_new.replace('si ', 'SI')
df_new = df_new.replace('SI ', 'SI')
print('Valores unicos en Dolor interlinea: ' + str(df_new['Dolor Interlinea'].unique()))
column_data['Dolor Interlinea'] = str(df_new["Dolor Interlinea"].unique()) + '\n'

#COLUMNa MCMurray
df_new = df_new.replace('no ', 'NO')
df_new = df_new.replace('No', 'NO')
df_new = df_new.replace(' SI', 'SI')
df_new = df_new.replace('+', 'SI')
df_new = df_new.replace('no concluyente', 'NO CONCLUYE')
print('Valores unicos en McMurray: ' + str(df_new['MCMurray'].unique()))
column_data['MCMurray'] = str(df_new["MCMurray"].unique()) + '\n'

#COLUMNA LCA
print('Valores unicos en LCA: ' + str(df_new['Cirugia Previa LCA'].unique()))
column_data['Cirugia Previa LCA'] = str(df_new["Cirugia Previa LCA"].unique()) + '\n'

#COLUMNA CIRUGIA PREVIA MENISCAL
print('Valores unicos en Cirugia meniscal previa: ' + str(df_new['Cirugia Previa Meniscal'].unique()))
column_data['Cirugia Previa meniscal'] = str(df_new["Cirugia Previa Meniscal"].unique()) + '\n'

#COLUMNA ESPACIO INTRARTICULAR 
print('Estadísticas Espacio Intraarticular: ' + str(df_new['Espacio Intraarticular (mm)'].describe()))
column_data['Espacio Intraarticular (mm)'] = str(df_new['Espacio Intraarticular (mm)'].describe()) + '\n'

#COLUMNA ESCLEROSIS SUBCONDRAL
#print('Valores unicos en Esclerosis Subcondral: ' + str(df_new['Esclerosis subcondral'].unique())) + '\n'
column_data['Escleroris subcondral'] = str(df_new['Esclerosis subcondral'].unique()) + '\n'

#COLUMNA OSTEOFITO
print('Valores unicos en Osteofito : ' + str(df_new['Osteofito'].unique()))
column_data['Osteofito'] = str(df_new['Osteofito'].unique()) + '\n'

#COLUMNA Genu Varo
print('Valores unicos en Genu Varo : ' + str(df_new['Genu varo'].unique()))
column_data['Genu varo'] = str(df_new['Genu varo'].unique()) + '\n'

#COLUMNA Genu Valgo
print('Valores unicos en Genu Vago : ' + str(df_new['Genu valgo'].unique()))
column_data['Genu valgo'] = str(df_new['Genu valgo'].unique()) + '\n'

#COLUMNA Kellgren
print('Valores unicos en Kellgren : ' + str(df_new['Kellgren'].unique()))
column_data['Kellgren'] = str(df_new['Kellgren'].unique()) + '\n'

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
print('Lateralidad 2 : ' + str(df_new['Lateralidad 2'].unique()))
column_data['Lateralidad 2'] = str(df_new['Lateralidad 2'].unique()) + '\n'

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
print('Valores unicos en Tipo de Rotura : ' + str(df_new['Tipo de Rotura'].unique()))
column_data['Tipo de Rotura'] = str(df_new['Tipo de Rotura'].unique()) + '\n'

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

print('Valores unicos en Zona Mensico : ' + str(df_new['Zona Menisco'].unique()))
column_data['Zona Menisco'] = str(df_new['Zona Menisco'].unique()) + '\n'

#COLUMNA Raiz Meniscal
print('Valores unicos en Raiz Meniscal : ' + str(df_new['Raiz Meniscal'].unique()))
column_data['Raiz Meniscal'] = str(df_new['Raiz Meniscal'].unique()) + '\n'

#COLUMNA Extrusion
df_new = df_new.replace('o,3', 0.3)
df_new = df_new.replace('rm horus', 0)
df_new['Extrusion'] = df_new['Extrusion'].replace(['SI', 'NO'], 0)
print('Estadísticas Extrusión: ' + str(df_new['Extrusion'].describe()))
column_data['Extrusion'] = str(df_new['Extrusion'].describe()) + '\n'

#COLUMNA Edema Oseo
df_new = df_new.replace('Si ', 'SI')
print('Valores unicos en Edema Óseo : ' + str(df_new['Edema Oseo'].unique()))
column_data['Edema Oseo'] = str(df_new['Edema Oseo'].unique()) + '\n'

#COLUMNA Grado
df_new['Grado'] = df_new['Grado'].replace(['III', 'iii'], 3)
df_new['Grado'] = df_new['Grado'].replace(['IV', 'iv'], 4)
df_new['Grado'] = df_new['Grado'].replace(['I', 'i'], 1)
df_new['Grado'] = df_new['Grado'].replace(['II', 'ii'], 2)
df_new['Grado'] = df_new['Grado'].replace(['II-III', 'ii\niiI'], 2.5)
df_new['Grado'] = df_new['Grado'].replace(['II-IV'], 3.5)
df_new['Grado'] = df_new['Grado'].replace(['I-II'], 1.5)


print('Estadísticas Grado: ' + str(df_new['Grado'].describe()))
column_data['Grado'] = str(df_new['Grado'].describe()) + '\n'

#COLUMNA Tipo Edema
df_new = df_new.replace('complee', 'COMPLETE')
df_new = df_new.replace('complete', 'COMPLETE')
df_new = df_new.replace('Edge', 'EDGE')
df_new = df_new.replace('edge', 'EDGE')
df_new = df_new.replace('Articular', 'ARTICULAR')
df_new = df_new.replace('articular', 'ARTICULAR')
df_new = df_new.replace('E', 'EDGE')
df_new = df_new.replace('Full', 'FULL')

print(df_new['tipo edema'].unique())
column_data['tipo edema'] = str(df_new['tipo edema'].unique()) + '\n'

#COLUMNA Condropatia
df_new = df_new.replace('sí', 'SI')
print(df_new['Condropatia'].unique())
column_data['Condropatia'] = str(df_new['Condropatia'].unique()) + '\n'

#COLUMNA Condropatía Femoropatelar
df_new = df_new.replace(' no', 'NO')
df_new = df_new.replace('ni', 'NO')
print(df_new['Condropatia Femoropatelar'].unique())
column_data['Condropatia Femoropatelar'] = str(df_new['Condropatia Femoropatelar'].unique()) + '\n'

#COLUMNA LCA
df_new = df_new.replace('PARCIAL', 'SI')
print(df_new['LCA'].unique())
column_data['LCA'] = str(df_new['LCA'].unique()) + '\n'

#COLUMNA Quiste baker
print(df_new['Quiste baker'].unique())
column_data['Quiste Baker'] = str(df_new['Quiste baker'].unique()) + '\n'

#COLUMNA Quiste parameniscal
print(df_new['Quiste parameniscal'].unique())
column_data['Quiste parameniscal'] = str(df_new['Quiste parameniscal'].unique()) + '\n'

json_object = json.dumps(column_data, indent=4)
with open("./data/column_data.json", "w") as outfile:
    outfile.write(json_object)

df_to_plot = df_new
df_to_plot.drop(columns=['lysholm score post', 'mejora con la cirugía',
       'satisfecho con la cirugía (1-4)', 'dolor actual 0-10',
       'Incorporación vida laboral', 'Deporte'], axis = 1, inplace=True)
percent_missing = df_new.isnull().sum() * 100 / len(df_to_plot)
missing_value_df = pd.DataFrame({'column_name': df_to_plot.columns,
                                 'percent_missing': percent_missing})
print(missing_value_df)
missing_value_df.plot(x='column_name', y='percent_missing', kind='bar')
plt.title('Porcentaje de valores sin rellenar de 142 filas')
plt.savefig('./data/graficas/Missing_values.png')
plt.show()