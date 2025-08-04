import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
tamaño_del_mercado = [401, 500, 600, 773, 977, 1207, 1461, 1750, 2046]
tasa_de_crecimiento = [np.nan, 24.7, 20.0, 28.8, 26.4, 23.5, 21.0, 15.2, 13.0]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de cambio año a año
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='coral', label='Tasa de Cambio Año a Año (%)', linewidth=2)
ax2.set_ylabel('Tasa de Cambio Año a Año (%)')
ax2.legend(loc='center right')

# Agregar etiquetas numéricas para el tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 20, f'{tamaño}', ha='center', va='bottom')

# Agregar etiquetas numéricas para la tasa de cambio año a año (omitir 2017 ya que no hay datos año a año)
for i, tasa in enumerate(tasa_de_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño del Mercado y Pronóstico de Medicina Estética No Quirúrgica en China de 2017 a 2025')

plt.tight_layout()
plt.show()