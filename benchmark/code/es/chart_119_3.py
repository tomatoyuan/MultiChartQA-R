import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2020", "2021", "2022", "2023", "2024", "2025P", "2026P", "2027P", "2028P", "2029P"]
# Tamaño del mercado (en miles de millones de yuanes)
market_size = [350.7, 425.2, 445.2, 594.9, 713.9, 833.1, 1083.0, 1245.5, 1413.6, 1563.5, 1763.6, 1925.8]
# Tasa de crecimiento (%)
growth_rate = [21.2, 6.8, -8.7, 33.6, 20.0, 16.7, 30.0, 15.0, 13.5, 10.6, 12.8, 9.2]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, market_size, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Tasa de Crecimiento (%)')
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='upper right')

# Añadir etiquetas numéricas para el tamaño del mercado
for i, size in enumerate(market_size):
    ax1.text(i, size + 20, f'{size}', ha='center', va='bottom')

# Añadir etiquetas numéricas para la tasa de crecimiento
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

plt.title('Tamaño y Pronóstico del Mercado Central de Deportes de Hielo y Nieve en China de 2016 a 2029')
plt.tight_layout()
plt.show()