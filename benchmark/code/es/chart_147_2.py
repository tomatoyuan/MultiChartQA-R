import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E"]
tamaño_del_mercado = [292.1, 282.4, 324.3, 350.2, 366.3, 387.9, 411.2, 440, 475.2, 546.5, 628.5, 710.2, 799.6]  # Tamaño del mercado (en miles de millones de yuanes)
tasas_de_crecimiento = [-3.3, 14.8, 8.0, 4.6, 5.9, 6.0, 7.0, 8.0, 15.0, 15.0, 13.0, 12.6]  # Tasa de crecimiento interanual (%), tenga en cuenta que no hay tasa de crecimiento en 2012, comenzando desde 2013

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Dibujar un gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='coral', label='Tamaño del Mercado (en miles de millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (en miles de millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar un gráfico de línea de la tasa de crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x[1:], tasas_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento Interanual (%)', linewidth=2)  # No hay tasa de crecimiento en 2012, comenzar a dibujar desde 2013
ax2.set_ylabel('Tasa de Crecimiento Interanual (%)')
ax2.legend(loc='center right')

# Añadir etiquetas numéricas para el tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 10, f'{tamaño}', ha='center', va='bottom', color='black')

# Añadir etiquetas numéricas para la tasa de crecimiento interanual (comenzando desde 2013)
for i, tasa in enumerate(tasas_de_crecimiento, start=1):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom', color='black')

ax1.set_title('Tamaño y Pronóstico del Mercado de Equipamiento de Fitness en China desde 2012 hasta 2024')
plt.tight_layout()
plt.show()