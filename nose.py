import pandas as pd
'''#Para leer el csv:

spark = SparkSession.builder.appName("Read CSV File into DataFrame").getOrCreate()

autor = spark.read.csv('C:\Users\Usuario\Documents\GitHub\TrabajoFinalBigData\ARCHIVOS\air_traffic_data.csv' , sep = ',', inferSchema = True, header = True)

df = autor.toPandas()
df.head()'''



f = pd.re