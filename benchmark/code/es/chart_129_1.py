import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P", "2026P", "2027P", "2028P"]
tamaño_del_mercado = [1946.6, 2157.4, 2396.0, 2626.6, 2910.3, 3210.0, 3511.8, 3838.4, 4164.6, 4527.0, 4902.7, 5309.6]
tasa_de_crecimiento = [10.8, 11.1, 10.0, 9.6, 10.8, 10.3, 9.4, 9.3, 8.5, 8.7, 8.3, 8.1]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (100 millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (100 millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento (%)')
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='upper right')

# Agregar anotaciones para los valores del tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 50, f'{tamaño}', ha='center', va='bottom')

# Agregar anotaciones para los valores de la tasa de crecimiento
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 0.2, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de la Industria del Té en China de 2017 a 2028')

plt.tight_layout()
plt.show()