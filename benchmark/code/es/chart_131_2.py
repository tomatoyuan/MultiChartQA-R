import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Población de 65 años y mayores (en diez miles de personas)
poblacion_mayores = [12777, 13262, 13902, 14524, 15037, 15961, 16724, 17767, 19064, 20056, 20978, 21676]

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, poblacion_mayores, color='green')

# Agregar etiquetas numéricas
for i, poblacion in enumerate(poblacion_mayores):
    ax.text(i, poblacion + 200, f'{poblacion}', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Población de 65 años y mayores (en diez miles de personas)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)

ax.set_title('Población de 65 años y mayores en China desde 2012 hasta 2023')

plt.tight_layout()
plt.show()