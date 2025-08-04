import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
cantidad_tiendas = [895.0, 1100.0, 1410.0, 1802.0, 2138.0, 2446.0, 2705.0, 2770.0, 2690.0, 2619.0, 2651.0, 2651.0]
tasa_crecimiento = [np.nan, 22.9, 28.2, 27.8, 18.6, 14.4, 10.8, 2.4, -2.9, -2.6, 1.2, 0.0]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras de la cantidad de tiendas conceptuales
ax1.bar(x, cantidad_tiendas, color='orange', label='Cantidad de Tiendas Conceptuales')
ax1.set_ylabel('Cantidad de Tiendas Conceptuales')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='lower left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_crecimiento, marker='o', color='coral', label='Tasa de Crecimiento (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='upper right')

# Agregar etiquetas numéricas para la cantidad de tiendas conceptuales
for i, cantidad in enumerate(cantidad_tiendas):
    ax1.text(i, cantidad + 30, f'{cantidad}', ha='center', va='bottom')

# Agregar etiquetas numéricas para la tasa de crecimiento (omitir 2012 ya que no hay datos año a año)
for i, tasa in enumerate(tasa_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.2, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Cantidad de Tiendas Conceptuales de Pandora y Tasa de Crecimiento desde 2012 hasta 2023')

plt.tight_layout()
plt.show()