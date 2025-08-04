import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
producción = [3010.6, 2995.1, 3038.9, 3109.9, 3174.9, 3008.8, 3159.9, 3179.8, 3064.0, 3038.6, 3074.6, 3201.2, 3440.1, 3683.0, 3932.0, 4197.0]
tasa_de_crecimiento = [2.2, -0.5, 1.5, 2.3, 2.1, -5.2, 5.0, 0.6, -3.6, -0.8, 1.2, 4.1, 7.5, 7.1, 6.8, 6.7]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Trazar el gráfico de barras de producción
ax1.bar(x, producción, color='orange', label='Producción (10,000 toneladas)')
ax1.set_ylabel('Producción (10,000 toneladas)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años, rotation=45)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Crecimiento año a año (%)', linewidth=2)
ax2.set_ylabel('Crecimiento año a año (%)')
ax2.legend(loc='center right')

# Agregar anotaciones de valores de producción
for i, prod in enumerate(producción):
    ax1.text(i, prod + 20, f'{prod}', ha='center', va='bottom')

# Agregar anotaciones de valores de tasa de crecimiento
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 0.2, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Producción de leche en China y crecimiento año a año desde 2008 hasta 2023')

plt.tight_layout()
plt.show()