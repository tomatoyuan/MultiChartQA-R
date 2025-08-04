import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
tamaño_mercado = [1606, 1693, 1867, 1950, 2133, 2029, 2308, 2565, 2804, 3014, 3186]
tasa_crecimiento = [np.nan, 5.4, 10.3, 4.4, 9.4, -4.9, 13.8, 11.1, 9.3, 7.5, 5.7]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_mercado, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar el gráfico de línea del crecimiento año a año
ax2 = ax1.twinx()
ax2.plot(x, tasa_crecimiento, marker='o', color='gold', label='Crecimiento Año a Año (%)', linewidth=2)
ax2.set_ylabel('Crecimiento Año a Año (%)')
ax2.legend(loc='lower right')

# Agregar anotaciones para los valores del tamaño del mercado
for i, tamaño in enumerate(tamaño_mercado):
    ax1.text(i, tamaño + 30, f'{tamaño}', ha='center', va='bottom')

# Agregar anotaciones para los valores del crecimiento año a año (omitir 2015 ya que no hay datos de crecimiento año a año)
for i, tasa in enumerate(tasa_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.2, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de la Industria de Cuidado de la Piel en China desde 2015 hasta 2025')

plt.tight_layout()
plt.show()