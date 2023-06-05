import pandas as pd
import numpy as np

# Definir los nombres de las ciudades
nombres_ciudades = ['Madrid', 'Barcelona', 'Tokyo', 'Roma', 'Paris']

# Generar la matriz de temperaturas
temperaturas = np.random.uniform(-5.0, 43.0, size=(365, 5))

# Modificar los nombres de las columnas
temperaturas_df = pd.DataFrame(temperaturas, columns=nombres_ciudades)

# Calcular la temperatura máxima por ciudad
temperaturas_maximas = temperaturas_df.max()

# Calcular la temperatura promedio por día
temperaturas_promedio = temperaturas_df.mean(axis=1)

# Encontrar el día con la temperatura más baja por ciudad
dias_temperatura_minima = temperaturas_df.idxmin()

# Imprimir los resultados
print("Temperatura máxima por ciudad:")
print(temperaturas_maximas)
print("\nTemperatura promedio por día:")
print(temperaturas_promedio)
print("\nDía con temperatura más baja según la ciudad:")
print(dias_temperatura_minima)