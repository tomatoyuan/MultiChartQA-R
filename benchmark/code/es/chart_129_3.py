import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
volumen_total = [133.8, 150.3, 167.9, 171.1, 181.7, 191.1, 202.6, 220.2, 230.2, 239.8, 240.4]
tasa_de_crecimiento = [np.nan, 12.3, 11.8, 1.9, 6.2, 5.1, 6.0, 8.7, 4.5, 4.2, 0.3]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Dibujar el gráfico de barras del volumen total de ventas internas
barras = ax1.bar(x, volumen_total, color='orange', label='Volumen Total de Ventas Internas (10,000 toneladas)')
ax1.set_ylabel('Volumen Total de Ventas Internas (10,000 toneladas)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Añadir anotaciones para el volumen total de ventas internas
for i, vol in enumerate(volumen_total):
    ax1.text(i, vol + 2, f'{vol}', ha='center', va='bottom')

# Crear un eje y secundario y dibujar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='center right')

# Añadir anotaciones para la tasa de crecimiento (omitir 2013 ya que no hay tasa de crecimiento)
for i, tasa in enumerate(tasa_de_crecimiento):
    if i > 0:
        ax2.text(i, tasa + 0.3, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Volumen Total de Ventas Internas y Tasa de Crecimiento del Té Chino de 2013 a 2023')

plt.tight_layout()
plt.show()