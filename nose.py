import pandas as pd

def columnas_fichero():
    print("Columnas del fichero")
    print("\n")
    print(f.columns)

#Leer el archivo

f = pd.read_csv("ARCHIVOS/air_traffic_data.csv", sep = ',')
print(f.head())

#Ver los nombres de las columnas
print(columnas_fichero())

#Ver los tipos de datos que hay en las columnas
print(f.dtypes)

#Para ver los valores nulos que hay en las columnas 
