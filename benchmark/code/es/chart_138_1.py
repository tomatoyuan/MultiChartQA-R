import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
tamaño_mercado = [2813, 3167, 3553, 3955, 4362, 4814, 5295, 4236, 4998, 5498, 5966, 6413, 6689]
tasa_crecimiento = [np.nan, 12.6, 12.2, 11.3, 10.3, 10.4, 10.0, -20.0, 18.0, 10.0, 8.5, 7.5, 4.3]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_mercado, color='red', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento año a año
ax2 = ax1.twinx()
ax2.plot(x, tasa_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento Año a Año (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento Año a Año (%)')
ax2.legend(loc='center right')

# Agregar anotaciones para los valores del tamaño del mercado
for i, tamaño in enumerate(tamaño_mercado):
    ax1.text(i, tamaño + 50, f'{tamaño}', ha='center', va='bottom')

# Agregar anotaciones para los valores de la tasa de crecimiento año a año (omitir 2013 ya que no hay datos año a año)
for i, tasa in enumerate(tasa_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de la Industria de la Cocción en Vaso en China desde 2013 hasta 2025')

plt.tight_layout()
plt.show()