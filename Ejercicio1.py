import pandas as pd
import numpy as np


# 1
df = pd.read_csv('mpg.csv')
print(df.head(3))
print(df.tail(5))

# Traducción de las columnas al castellano
traducciones = {
    'mpg': 'Consumo de millas por galón',
    'cylinders': 'Cilindros',
    'displacement': 'Desplazamiento',
    'horsepower': 'Potencia',
    'weight': 'Peso',
    'acceleration': 'Aceleración',
    'model_year': 'Año_modelo',
    'origin': 'Origen',
    'car_name': 'Nombre_coche'
}
df = df.rename(columns=traducciones)

# 2
print(df.dtypes)
columnas_numericas = df.select_dtypes(include=['float', 'int'])
print(columnas_numericas.describe())

#3

def conditional_mean(df, column, condition):
    return np.mean(df.loc[condition, column])

# 4

print('Media de rendimiento de combustible en coches de antes del año 75:', conditional_mean(df, 'Consumo de millas por galón', df['Año_modelo'] < 75))
print('Media de rendimiento de combustible en coches de después del año 75:', conditional_mean(df, 'Consumo de millas por galón', df['Año_modelo'] > 75))