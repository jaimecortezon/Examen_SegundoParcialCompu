import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1
df = pd.read_csv('mpg.csv')
print(df['cylinders'].value_counts())
vehiculo_potencia_mas_alta = df[df['horsepower'] == df['horsepower'].max()]['name'].values[0]
print(vehiculo_potencia_mas_alta)

# 2

columnas_numericas = df.select_dtypes(include=['float', 'int'])
matriz_correlacion = columnas_numericas.corr()
print(matriz_correlacion)

# 3 y 4

fig, ax = plt.subplots()

for cyl in df['cylinders'].unique():
    mpg = df.loc[df['cylinders'] == cyl, 'mpg']
    ax.hist(mpg, alpha=0.5, label=f'Cilindro {cyl}')

# 5

ax.set_title('Histograma de rendimiento de combustible por tipo de cilindro')
ax.set_xlabel('Rendimiento de combustible (mpg)')
ax.set_ylabel('Frecuencia')
ax.legend(loc='upper right')

plt.show()