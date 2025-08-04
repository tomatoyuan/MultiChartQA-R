import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
tamaño_del_mercado = [1181, 1543, 1905, 2264, 2556, 2961, 3492, 3834, 4237, 4631, 5033]
tasa_de_crecimiento = [30.7, 23.5, 18.8, 12.9, 15.8, 17.9, 9.8, 10.5, 9.3, 8.7]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento año tras año
ax2 = ax1.twinx()
ax2.plot(x[1:], tasa_de_crecimiento, marker='o', color='brown', label='Crecimiento Año tras Año (%)', linewidth=2)  # No hay datos de crecimiento año tras año para 2015, comenzar desde 2016
ax2.set_ylabel('Crecimiento Año tras Año (%)')
ax2.legend(loc='center right')

# Añadir etiquetas de valor del tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 50, f'{tamaño}', ha='center', va='bottom')

# Añadir etiquetas de valor del crecimiento año tras año (no hay datos para 2015, comenzar desde 2016)
for i, tasa in enumerate(tasa_de_crecimiento, start=1):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de la Industria de las Tiendas de Conveniencia Chinas de 2015 a 2025')

plt.tight_layout()
plt.show()