import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P", "2026P", "2027P"]
tamaño_del_mercado = [2776, 3498, 4400, 5762, 6975, 8782, 10149, 10890, 11641, 12270, 12847, 13386, 13855]
tasa_de_crecimiento = [26.0, 25.8, 31.0, 21.1, 25.9, 15.6, 7.3, 6.9, 5.4, 4.7, 4.2, 3.5, 2.9]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (100 millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (100 millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años, rotation=45)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento (%)')
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='center right')

# Añadir etiquetas de valor del tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 100, f'{tamaño}', ha='center', va='bottom')

# Añadir etiquetas de valor de la tasa de crecimiento
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño y Tasa de Crecimiento del Mercado de Servicios Domésticos en China desde 2015 hasta 2027 y Pronóstico')

plt.tight_layout()
plt.show()