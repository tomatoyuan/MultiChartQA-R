import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
tamaño_del_mercado = [3181.0, 3396.0, 3656.0, 3942.0, 4256.0, 3958.0, 4553.0, 4858.1, 5169.0, 5458.0, 5791.0]
tasa_de_crecimiento = [np.nan, 6.8, 7.7, 7.8, 8.0, -7.0, 15.0, 6.7, 6.4, 5.6, 6.1]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras para el tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea para la tasa de crecimiento año tras año
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento Año tras Año (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento Año tras Año (%)')
ax2.legend(loc='center right')

# Añadir anotaciones para el tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 50, f'{tamaño}', ha='center', va='bottom')

# Añadir anotaciones para la tasa de crecimiento año tras año (omitir 2015 ya que no hay datos año tras año)
for i, tasa in enumerate(tasa_de_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.2, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Previsión de la Industria de Cosméticos en China de 2015 a 2025')

plt.tight_layout()
plt.show()