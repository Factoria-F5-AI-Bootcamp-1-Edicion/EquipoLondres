import pandas as pd

path_to_data = "london_airbnb.csv"
df = pd.read_csv(path_to_data)
    
# Comienzo la limpieza de datos no definitiva
df.drop(["host_id", "name", "host_name", ], axis=1, inplace=True)
df.dropna(how='any')

# guardamos los datos para usar

for i in range(len(df['price'])):

    if 250 >= df['price'][i] < 1000 :
        print(df['price'][i])