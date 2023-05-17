import csv
import pandas as pd
# Nombre de los archivos CSV
DATASET_PATH = "./data/datasets/"
sinteticos = DATASET_PATH + 'sinteticos_mayoria_9.csv'  # CSV con 5000 filas
datos_procesados= DATASET_PATH + 'datos_procesados_mayoria_9.csv'  # CSV con 167 filas

# Nombre de los archivos de salida
train_csv = DATASET_PATH + 'train_mayoria_9.csv'    # CSV con 5000 filas
test_csv = DATASET_PATH + 'test_mayoria_9.csv'      # CSV con 67 filas

df = pd.read_csv(sinteticos, sep=';')
print(df.head())
df.drop(columns=['Unnamed: 0','Unnamed: 0.1'], inplace=True)
df.to_csv(sinteticos, sep=';')
df = pd.read_csv(datos_procesados, sep=';')
print(df.head())
df.drop(columns=['Unnamed: 0'], inplace=True)
df.to_csv(datos_procesados, sep=';')
# Leer el contenido del primer archivo CSV

datos1 = []
with open(sinteticos, 'r') as archivo:
    lector = csv.reader(archivo)
    cabecero = next(lector)
    for fila in lector:
        datos1.append(fila)

# Leer el contenido del segundo archivo CSV
datos2 = []
with open(datos_procesados, 'r') as archivo:
    lector = csv.reader(archivo)
    cabecero2 = next(lector)
    for fila in lector:
        datos2.append(fila)
print(cabecero)
print(cabecero2)
# Separar los datos en train.csv y test.csv
train_datos = [cabecero] + datos1 + datos2[:100]
test_datos = [cabecero] + datos2[100:]

# Escribir los datos en los archivos de salida
with open(train_csv, 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    for fila in train_datos:
        escritor.writerow(fila)

with open(test_csv, 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    for fila in test_datos:
        escritor.writerow(fila)

print("Archivos CSV generados con éxito.")
