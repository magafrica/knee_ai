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


df = pd.read_csv('./data/datos_procesados.csv', delimiter=';')
df.drop(columns=["Unnamed: 0", "NHC"], inplace=True)



#Unique values JSON
unique_values = {}
for col in df:
       if col not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular (mm)', 'Kellgren', 'Extrusion', 'lysholm score post', 'Grado', 'Angulo']:
              content = df[col].unique()
              content = content.tolist()
              unique_values[str(col)] = content
  
json_object = json.dumps(unique_values, indent= 2)
with open("./data/unique_values.json", "w") as outfile:
    outfile.write(json_object)

#Describe values JSON
describe_values = {}   
for col in df:
       content = df[col].describe()
       content = content.to_dict()
       describe_values[str(col)] = content
       
json_describe = json.dumps(describe_values,indent=4, cls=NpEncoder)
with open("./data/statistics.json", "w") as outfile:
    outfile.write(json_describe)


with open('./data/statistics.json', 'r') as f:
    data = json.load(f)

for entry in data:
    print(data[entry])
    if entry not in ['Edad', 'Angulo 1', 'IMC', 'Espacio Intraarticular (mm)', 'Kellgren', 'Extrusion', 'lysholm score post', 'Grado', 'Angulo']:
        result = data[entry]['freq'] / data[entry]['count']
        print("result")
        data[entry]['stability'] = result

with open('./data/statistics.json', 'w') as f:
    json.dump(data, f, indent=4)