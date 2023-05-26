import pandas as pd

def atributos_fichero():
    print("Columnas del fichero")
    print("\n")
    print(f.columns)
    print("Filas del fichero")
    print("\n")
    print(f.index)

f = pd.read_csv("ARCHIVOS/air_traffic_data.csv", sep = ',')
print(f)

