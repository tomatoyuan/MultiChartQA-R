import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2022", "2023", "2024", "2025P", "2026P", "2027P", "2028P"]
# Tamaño del mercado (en miles de millones de yuanes)
market_size = [11.5, 79.3, 471.7, 805.8, 1665.3, 2317.6, 2767.4]
# Tasa de crecimiento (%)
growth_rate = [589.6, 494.8, 70.8, 106.7, 39.2, 19.4]  # Nota: La tasa de crecimiento de 2022 - 2023 corresponde al cambio del año anterior al siguiente año. Aquí se dispone según los puntos de la línea en el gráfico. La correspondencia debe ser confirmada.

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, market_size, color='coral', label='Tamaño (en miles de millones de yuanes)')
ax1.set_ylabel('Tamaño (en miles de millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento (Nota: La correspondencia entre los puntos de datos de la tasa de crecimiento y los años puede necesitar ser ajustada)
ax2 = ax1.twinx()
# Los datos de la tasa de crecimiento corresponden al cambio de 2023 - 2028P, por lo que el índice del eje x comienza en 1
ax2.plot(x[1:], growth_rate, marker='o', color='gold', label='Tasa de crecimiento (%)')
ax2.set_ylabel('Tasa de crecimiento (%)')
ax2.legend(loc='center right')

# Agregar anotaciones para los valores del tamaño del mercado
for i, size in enumerate(market_size):
    ax1.text(i, size + 50, f'{size}', ha='center', va='bottom')

# Agregar anotaciones para los valores de la tasa de crecimiento (correspondientes a los puntos de la línea)
for i, rate in enumerate(growth_rate):
    # La tasa de crecimiento corresponde al índice del año i + 1 (a partir de 2023)
    ax2.text(x[i + 1], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Tamaño y pronóstico del mercado central de AIGC en China desde 2022 - 2028')

plt.tight_layout()
plt.show()