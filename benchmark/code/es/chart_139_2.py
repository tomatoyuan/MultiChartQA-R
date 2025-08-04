import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P"]
tamaño_mercado = [216.3, 234.6, 240.9, 250.3, 259.3, 230.5, 235.3, 253.4, 270.9, 304.3, 335.0, 364.1, 387.8]
tasa_crecimiento = [8.5, 2.7, 3.9, 3.6, -11.1, 2.1, 7.7, 6.9, 12.3, 10.1, 8.7, 6.5]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_mercado, color='orange', label='Tamaño del Mercado (100 millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (100 millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea del crecimiento año tras año
ax2 = ax1.twinx()
ax2.plot(x[1:], tasa_crecimiento, marker='o', color='brown', label='Crecimiento Año tras Año (%)', linewidth=2)  # No hay datos de crecimiento año tras año para 2012, comenzar desde 2013
ax2.set_ylabel('Crecimiento Año tras Año (%)')
ax2.legend(loc='lower right')

# Agregar etiquetas de valor del tamaño del mercado
for i, tamaño in enumerate(tamaño_mercado):
    ax1.text(i, tamaño + 5, f'{tamaño}', ha='center', va='bottom')

# Agregar etiquetas de valor del crecimiento año tras año (no hay datos para 2012, comenzar desde 2013)
for i, tasa in enumerate(tasa_crecimiento, start=1):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de la Industria de Supermercados de Membresía de Almacén Chinos desde 2012 hasta 2024')

plt.tight_layout()
plt.show()