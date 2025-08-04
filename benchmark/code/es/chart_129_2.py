import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
produccion = [68.33, 70.17, 74.51, 76.75, 83.52, 91.82, 100.92, 117.05, 127.59, 137.16, 148.54, 160.76, 176.39, 188.71, 204.94, 228.01, 231.72, 246.04, 259.01, 274.26, 293.18, 312.32, 334.21, 355.00]
tasa_de_crecimiento = [np.nan, 2.7, 6.2, 3.0, 8.7, 11.9, 10.0, 13.9, 7.2, 7.6, 8.3, 9.9, 9.6, 7.1, 8.6, 11.1, 1.6, 6.4, 6.1, 6.4, 5.6, 7.9, 5.6, 6.2]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(16, 9))

# Trazar el gráfico de barras de producción
ax1.bar(x, produccion, color='orange', label='Producción (10,000 toneladas)')
ax1.set_ylabel('Producción (10,000 toneladas)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años, rotation=45)
ax1.legend(loc='upper left')

# Crear un eje gemelo y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento (%)')
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='center right')

# Añadir etiquetas de valores de producción
for i, prod in enumerate(produccion):
    ax1.text(i, prod + 5, f'{prod}', ha='center', va='bottom')

# Añadir etiquetas de valores de tasa de crecimiento (omitir el año 2000 ya que no hay tasa de crecimiento)
for i, rate in enumerate(tasa_de_crecimiento):
    if i > 0:
        ax2.text(i, rate + 0.2, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Producción y Tasa de Crecimiento del Té en China desde 2000 hasta 2023')

plt.tight_layout()
plt.show()