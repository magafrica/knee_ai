import pandas as pd

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

        
print(df.columns)

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
#print(df_new["Sexo"].unique())

#COLUMNA LATERALIDAD
df_new = df_new.replace('derecha', 'DERECHA')
df_new = df_new.replace('Derecha', 'DERECHA')
df_new = df_new.replace('izquierda', 'IZQUIERDA')
df_new = df_new.replace('Izquierda ', 'IZQUIERDA')
df_new = df_new.replace('Izquierda', 'IZQUIERDA')
#print(df_new["Lateralidad"].unique())

#COLUMNA CIRUGÍA
df_new = df_new.replace('MENISCECTOMIA PARCIAL', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('sutura', 'SUTURA')
df_new = df_new.replace('SUTURA A MURO', 'SUTURA')
df_new= df_new.replace('menisectomía', 'MENISECTOMIA')
df_new= df_new.replace('menisectomia', 'MENISECTOMIA')
df_new= df_new.replace('meniscectomia', 'MENISECTOMIA')
df_new= df_new.replace('meniscectomía', 'MENISECTOMIA')
df_new = df_new.replace('MENISECTOMÍA PARCIAL', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('menisectomia parcial', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('meniscectomia parcial', 'MENISECTOMIA PARCIAL')
df_new = df_new.replace('menisectomía parcial', 'MENISECTOMIA PARCIAL')
#print(df_new["Cirugia"].unique())

#COLUMNA TRAUMATICA
df_new = df_new.replace('si', 'SI')
df_new = df_new.replace('Si', 'SI')
df_new = df_new.replace('no', 'NO')
df_new = df_new.replace('NO ', 'NO')
#print(df_new['Traumatica'].unique())

#COLUMNA DOLOR INTERLINEA
df_new = df_new.replace('si ', 'SI')
df_new = df_new.replace('SI ', 'SI')
#print(df_new['Dolor Interlinea'].unique())

#COLUMNa MCMurray
df_new = df_new.replace('no ', 'NO')
df_new = df_new.replace('No', 'NO')
df_new = df_new.replace(' SI', 'SI')
df_new = df_new.replace('+', 'SI')
df_new = df_new.replace('no concluyente', 'NO CONCLUYE')
#print(df_new['MCMurray'].unique())

#COLUMNA HTA
#print(df_new['Cirugia Previa LCA'].unique())

#COLUMNA CIRUGIA PREVIA MENISCAL
#print(df_new['Cirugia Previa Meniscal'].unique())

#COLUMNA ESPACIO INTRARTICULAR
#print(df_new['Espacio Intraarticular (mm)'].unique())

#COLUMNA ESCLEROSIS SUBCONDRAL
#print(df_new['Esclerosis subcondral'].unique())

#COLUMNA OSTEOFITO
#print(df_new['Osteofito'].unique())

#COLUMNA Genu Varo
#print(df_new['Genu varo'].unique())

#COLUMNA Genu Valgo
#print(df_new['Genu valgo'].unique())

#COLUMNA Kellgren
#print(df_new['Kellgren'].unique())

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
#print(df_new['Lateralidad 2'].unique())

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
#print(df_new['Tipo de Rotura'].unique())

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

#print(df_new['Zona Menisco'].unique())

#COLUMNA Raiz Meniscal
#print(df_new['Raiz Meniscal'].unique())

#COLUMNA Extrusion
df_new = df_new.replace('o,3', 0.3)
df_new = df_new.replace('rm horus', 0)
df_new['Extrusion'] = df_new['Extrusion'].replace(['SI', 'NO'], 0)
#print(df_new['Extrusion'].unique())

#COLUMNA Edema Oseo
df_new = df_new.replace('Si ', 'SI')
#print(df_new['Edema Oseo'].unique())

#COLUMNA Grado
df_new['Grado'] = df_new['Grado'].replace(['III', 'iii'], 3)
df_new['Grado'] = df_new['Grado'].replace(['IV', 'iv'], 4)
df_new['Grado'] = df_new['Grado'].replace(['I', 'i'], 1)
df_new['Grado'] = df_new['Grado'].replace(['II', 'ii'], 2)
df_new['Grado'] = df_new['Grado'].replace(['II-III', 'ii\niiI'], 2.5)
df_new['Grado'] = df_new['Grado'].replace(['II-IV'], 3.5)
df_new['Grado'] = df_new['Grado'].replace(['I-II'], 1.5)


#print(df_new['Grado'].unique())

#COLUMNA Tipo Edema
df_new = df_new.replace('complee', 'COMPLETE')
df_new = df_new.replace('complete', 'COMPLETE')
df_new = df_new.replace('Edge', 'EDGE')
df_new = df_new.replace('edge', 'EDGE')
df_new = df_new.replace('Articular', 'ARTICULAR')
df_new = df_new.replace('articular', 'ARTICULAR')
df_new = df_new.replace('E', 'EDGE')
df_new = df_new.replace('Full', 'FULL')

#print(df_new['tipo edema'].unique())

#COLUMNA Condropatia
df_new = df_new.replace('sí', 'SI')
#print(df_new['Condropatia'].unique())


#COLUMNA Zona
print(df_new['Zona Condropatia'].unique())

#COLUMNA Zona
#print(df_new['Condropatia Fermopatelar'].unique())

#COLUMNA LCA
#print(df_new['LCA'].unique())

#COLUMNA Quiste baker
#print(df_new['Quiste baker'].unique())

#COLUMNA Quiste parameniscal
#print(df_new['Quiste parameniscal'].unique())