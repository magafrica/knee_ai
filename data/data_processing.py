import pandas as pd

DATASETS_PATH = "./data/datasets/"
FILENAME_TO_READ = "MENISCOS_FILTRADO.xlsx"
FILENAME_TO_SAVE = "datos_procesados.csv"
df = pd.read_excel(DATASETS_PATH + FILENAME_TO_READ)


######################################################## RENAME INVALID NAME COLUMNS ########################################################
                                                 
df.rename( columns = {'\nNacionalidad': 'NACIONALIDAD', 'CIRUGÍA': 'Cirugia','TRAUMÁTICA': 'Traumatica',
       'DOLOR INTERLÍNEA': 'Dolor Interlinea', 'MCMURRAY +': 'MCMurray',
      'Anticoagulación': 'Anticoagulacion', 'Cáncer': 'Cancer', 
       'Cirugía Previa meniscal':'Cirugia Previa Meniscal' , 'Espacio Intraarticular (nm)': 'Espacio Intraarticular',
        'Ángulo 1': 'Angulo 1', 'Ángulo': 'Angulo', '\nLateralidad' : 'Lateralidad 2', '\nTipo de Rotura': 'Tipo de Rotura',
        'Raíz Meniscal': 'Raiz Meniscal', '\nExtrusion ( mm )': 'Extrusion', '\nEdema óseo': 'Edema Oseo',
        '\n\nCondropatía ': 'Condropatia', '\nGrado': 'Grado', '\nZona': 'Zona Condropatia',
       '\nCondropatía Femoropatelar': 'Condropatia Femoropatelar'}, inplace=True)

 
df = df.drop(columns = ['NACIONALIDAD', 'Trabajo', 'Zona Condropatia', 'Dolor en cuclilla', 'Reincorporación a vida laboral', 'Tratamiento', 'Unnamed: 56'
                                ,'Unnamed: 57', 'Reintervención',
       'Causa reintervención', 'Fracaso de tratamiento',
       'tiempo desde fracaso (meses)', 'Unnamed: 63', 'RMN POST',
       'Unnamed: 65', 'SUTURA VS MENISCECTOMIA', 'fecha de cirugía', 'Incorporación vida laboral', 'Deporte', 'satisfecho con la cirugía (1-4)', 'dolor actual 0-10', 'mejora con la cirugía'] )       


######################################################## UNIFY VALUES ########################################################
#COLUMNA SEXO
df_new = df.replace(['mujer', 'MUJER ', 'Mujer'], 'MUJER')
df_new = df_new.replace('varón', 'HOMBRE')
df_new = df_new.replace('Varón', 'HOMBRE')
df_new = df_new.replace('VARÓN', 'HOMBRE')
df_new = df_new.replace('VARON', 'HOMBRE')
df_new = df_new.replace('varon', 'HOMBRE')
df_new = df_new.replace('Varon', 'HOMBRE')
df_new = df_new.replace('hombre', 'HOMBRE')


#COLUMNA LATERALIDAD
df_new = df_new.replace('derecha', 'DERECHA')
df_new = df_new.replace('Derecha', 'DERECHA')
df_new = df_new.replace('izquierda', 'IZQUIERDA')
df_new = df_new.replace('Izquierda ', 'IZQUIERDA')
df_new = df_new.replace('Izquierda', 'IZQUIERDA')

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

#SIES Y NOES
df_new = df_new.replace(['si', 'Si', 'si ', 'SI ', ' SI', '+', 'sí', 'Sí', 'Si ', 'PARCIAL'], 'SI')
df_new = df_new.replace(['no', 'ni', ' no', 'no ', 'No', 'Ninguna', 'NO '], 'NO')
df_new = df_new.replace('no', 'NO')
df_new = df_new.replace('NO ', 'NO')


#COLUMNA Lateralidad
df_new = df_new.replace('Medial', 'MEDIAL')
df_new = df_new.replace('medial', 'MEDIAL')
df_new = df_new.replace('externo', 'EXTERNO')
df_new = df_new.replace('interno', 'INTERNO')
df_new = df_new.replace('Lateral', 'LATERAL')
df_new = df_new.replace('ambos', 'AMBOS')
df_new = df_new.replace('Medial + lateral', 'AMBOS')
df_new = df_new.replace('bilateral', 'LATERAL')

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

#COLUMNA Extrusion
df_new = df_new.replace('o,3', 0.3)
df_new = df_new.replace('rm horus', 0)
df_new['Extrusion'] = df_new['Extrusion'].replace(['SI', 'NO'], 0)
#column_data['Extrusion'] = list(df_new['Extrusion'].describe())

#COLUMNA Grado
df_new['Grado'] = df_new['Grado'].replace(['III', 'iii'], 3)
df_new['Grado'] = df_new['Grado'].replace(['IV', 'iv'], 4)
df_new['Grado'] = df_new['Grado'].replace(['I', 'i'], 1)
df_new['Grado'] = df_new['Grado'].replace(['II', 'ii'], 2)
df_new['Grado'] = df_new['Grado'].replace(['II-III', 'ii\niiI'], 2.5)
df_new['Grado'] = df_new['Grado'].replace(['II-IV'], 3.5)
df_new['Grado'] = df_new['Grado'].replace(['I-II'], 1.5)
df_new['Grado'].fillna(value=0, inplace=True)
#column_data['Grado'] = list(df_new['Grado'].describe())

#COLUMNA Genu Varo
df_new['Genu varo'].fillna(value='NO', inplace=True)

#COLUMNA Angulo Genu Varu
df.loc[df['Genu varo'] == 'NO', 'Angulo Genu Varo'] = 0
df_new['Angulo Genu Varo'].fillna(value= 0, inplace=True)

#COLUMNA genu Valgo
df.loc[df['Genu valgo'] == 'SI', 'Genu Valgo'] = 'NO'

#COLUMNA Kellgren
df_new['Kellgren'].fillna(value=0, inplace=True)

#COLUMNA Tipo Edema
df_new = df_new.replace('complee', 'COMPLETE')
df_new = df_new.replace('complete', 'COMPLETE')
df_new = df_new.replace('Edge', 'EDGE')
df_new = df_new.replace('edge', 'EDGE')
df_new = df_new.replace('Articular', 'ARTICULAR')
df_new = df_new.replace('articular', 'ARTICULAR')
df_new = df_new.replace('E', 'EDGE')
df_new = df_new.replace('Full', 'FULL')

df_new = df_new.replace('no tele', 0)
df_new = df_new.replace(['no rx', 'no rx en carga'], 0)
#Columna Zona
df_new = df_new.replace(['cóndilo', 'CFI', 'CFE', 'condilo', 'compartimento interno'], 'CONDILO')
df_new = df_new.replace(['meseta', 'Meseta interna', 'Meseta', 'meseta ', 'meseta interna\n', 'meseta interna'], 'MESETA')
df_new = df_new.replace(['CFI + MTI', 'TIBIA + cóndilo'], 'AMBOS')

df_new.to_csv(DATASETS_PATH + FILENAME_TO_SAVE, sep = ";", encoding="utf-8")

