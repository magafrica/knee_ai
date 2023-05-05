import pandas as pd
import numpy as np
import json


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

#LEER ARCHIVO NUEVO
DATASETS_PATH = "./data/datasets/"
JSON_PATH = "./data/JSON/"
FILENAME_TO_READ = "datos_procesados.csv"
FILENAME_TO_SAVE = "datos_procesados_stability.csv"
UNIQUE_VALUES = "unique_values.json"
STATISCICS = "statistics_values.json"
STABILITY_THRESHOLD = 0.8

df = pd.read_csv(DATASETS_PATH + FILENAME_TO_READ, delimiter=';')

#drop index and nhc
df.drop(columns=["Unnamed: 0", "NHC"], inplace=True)

#Unique values JSON
unique_values = {}
for col in df:
       #estoy quitando datos numericos 
       if col not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular (mm)', 'Extrusion', 'lysholm score post', 'Angulo']:
              content = df[col].unique()
              content = content.tolist()
              unique_values[str(col)] = content
  
json_object = json.dumps(unique_values, indent= 2)
with open(JSON_PATH + UNIQUE_VALUES, "w") as outfile:
    outfile.write(json_object)

#Describe values JSON
describe_values = {}   
for col in df:
       content = df[col].describe()
       content = content.to_dict()
       describe_values[str(col)] = content
       
json_describe = json.dumps(describe_values,indent=4, cls=NpEncoder)
with open(JSON_PATH + STATISCICS, "w") as outfile:
    outfile.write(json_describe)


with open(JSON_PATH + STATISCICS, 'r') as f:
    data = json.load(f)
columns_to_delete = []
for entry in data:
    #quitando datos numéricos
    if entry not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular', 'Kellgren', 'Extrusion', 'lysholm score post', 'Angulo Genu Varo', 'Angulo Genu Valgo', 'Grado', 'Espacio Intraarticular (mm)']:
        result = data[entry]['freq'] / data[entry]['count']
        data[entry]['stability'] = result
        if STABILITY_THRESHOLD < result:
            columns_to_delete.append(entry)

with open(JSON_PATH + STATISCICS, 'w') as f:
    json.dump(data, f, indent=4)
    
df_stability = df.drop(columns=columns_to_delete)
df_stability.to_csv(DATASETS_PATH + FILENAME_TO_SAVE, sep = ";", encoding="utf-8")