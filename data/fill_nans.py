import pandas as pd
import json

FILL_NANS= 1  #0 = fill with "unknown", 1 = fill with majority
STABILITY_THRESHOLD = 0.9
DATASETS_PATH = "./data/datasets/"
JSON_PATH = "./data/JSON/"
FILENAME_TO_READ ="datos_sinteticos_tabularlstm.csv"
STATISCICS = "statistics_values_sinteticos.json"
JSON_PATH = "./data/JSON/"

if FILL_NANS == 0:
    if STABILITY_THRESHOLD == 0.7:
        FILENAME_TO_SAVE = "sinteticos_unknown_7.csv"
    if STABILITY_THRESHOLD == 0.8:
        FILENAME_TO_SAVE = "sinteticos_unknown_8.csv"
    if STABILITY_THRESHOLD == 0.9:
        FILENAME_TO_SAVE = "sinteticos_unknown_9.csv"
if FILL_NANS == 1:
    if STABILITY_THRESHOLD == 0.7:
        FILENAME_TO_SAVE = "sinteticos_mayoria_7.csv"
    if STABILITY_THRESHOLD == 0.8:
        FILENAME_TO_SAVE = "sinteticos_mayoria_8.csv"
    if STABILITY_THRESHOLD == 0.9:
        FILENAME_TO_SAVE = "sinteticos_mayoria_9.csv" 

    
df = pd.read_csv(DATASETS_PATH + FILENAME_TO_READ, sep= ";")
df.drop(columns=["NHC"], inplace=True)
if FILL_NANS == 0:
    df["Extrusion"].replace(['NO MR'], "unknown", inplace=True)
    for col in df:
        df[col].fillna(value="unknown", inplace=True)
        
if FILL_NANS == 1:
    df["Extrusion"].replace(['NO MR'],df["Extrusion"].mode().iloc[0], inplace=True)
    for col in df:
        df[col].fillna(df[col].mode().iloc[0], inplace=True)

with open(JSON_PATH + STATISCICS, 'r') as f:
    data = json.load(f)
columns_to_delete = []
for entry in data:
    #quitando datos numéricos
    if entry not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular', 'Kellgren', 'Extrusion', 'lysholm score post', 'Angulo Genu Varo', 'Angulo Genu Valgo', 'Grado', 'Espacio Intraarticular (mm)', 'Unnamed: 0.1', 'Angulo']:
        if STABILITY_THRESHOLD < data[entry]['stability']:
            columns_to_delete.append(entry)
   
df = df.drop(columns=columns_to_delete)

df["Extrusion"] = df["Extrusion"].astype(float)
df["lysholm score post"] = df["lysholm score post"].astype(float)
df.to_csv(DATASETS_PATH + FILENAME_TO_SAVE, sep = ";", encoding="utf-8")