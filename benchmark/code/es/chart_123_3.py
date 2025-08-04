import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025E", "2026E", "2027E"]
# Tamaño del mercado (en miles de millones de yuanes)
market_size = [3013, 4597, 5980, 6680, 10036, 11161, 15254, 16357, 17469, 18503, 19567]
# Crecimiento año tras año (%)
yoy_growth = [52.6, 30.1, 16.9, 11.7, 50.2, 11.2, 36.7, 7.2, 6.8, 5.9, 5.8]
# Tasa de penetración de la industria de la entrega de comida online (%)
penetration_rate = [7.6, 10.9, 12.8, 11.7, 21.4, 25.4, 28.8, 28.0, 28.0, 28.0, 28.0]  # La tasa de penetración para algunos años debe confirmarse según el gráfico. Aquí, se asume que se mantiene en 28.0 después de 2023 y se puede ajustar según la situación real.

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras del tamaño del mercado
ax1.bar(x, market_size, color='orange', label='Tamaño del Mercado (en miles de millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (en miles de millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar los gráficos de línea del crecimiento año tras año y la tasa de penetración
ax2 = ax1.twinx()
ax2.plot(x, yoy_growth, marker='o', color='brown', label='Crecimiento Año tras Año (%)')
ax2.plot(x, penetration_rate, marker='o', color='blue', label='Tasa de Penetración de la Industria de la Entrega de Comida Online (%)')
ax2.set_ylabel('Porcentaje (%)')
ax2.legend(loc='upper right')

# Agregar etiquetas de valor para el tamaño del mercado
for i, size in enumerate(market_size):
    ax1.text(i, size + 200, f'{size}', ha='center', va='bottom')

# Agregar etiquetas de valor para el crecimiento año tras año
for i, growth in enumerate(yoy_growth):
    ax2.text(i, growth + 1, f'{growth}%', ha='center', va='bottom')

# Agregar etiquetas de valor para la tasa de penetración
for i, rate in enumerate(penetration_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Tamaño y Tasa de Penetración del Mercado de la Entrega de Comida Online en China de 2017 a 2027')

plt.tight_layout()
plt.show()