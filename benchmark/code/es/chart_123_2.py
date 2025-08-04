import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Ingresos de la industria de catering (trillones de yuanes)
catering_revenue = [3.96, 4.27, 4.67, 3.95, 4.69, 4.39, 5.29]
# Variación interanual de los ingresos de la industria de catering (%)
catering_yoy = [10.7, 7.8, 9.4, -15.4, 18.6, -6.3, 20.9]
# Variación interanual de los ingresos de la industria de catering por encima del límite (%)
above_limit_yoy = [7.4, 6.4, 7.1, -14.0, 23.5, -5.9, 20.4]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras de los ingresos de la industria de catering
ax1.bar(x, catering_revenue, color='orange', label='Ingresos de la industria de catering (trillones de yuanes)')
ax1.set_ylabel('Ingresos de la industria de catering (trillones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar un gráfico de líneas de las variaciones interanuales
ax2 = ax1.twinx()
ax2.plot(x, catering_yoy, marker='o', color='brown', label='Variación interanual de los ingresos de la industria de catering (%)')
ax2.plot(x, above_limit_yoy, marker='o', color='blue', label='Variación interanual de los ingresos de la industria de catering por encima del límite (%)')
ax2.set_ylabel('Variación interanual (%)')
ax2.legend(loc='center right')

# Agregar etiquetas de valor de los ingresos de la industria de catering
for i, rev in enumerate(catering_revenue):
    ax1.text(i, rev + 0.1, f'{rev}', ha='center', va='bottom')

# Agregar etiquetas de valor de la variación interanual de los ingresos de la industria de catering
for i, yoy in enumerate(catering_yoy):
    ax2.text(i, yoy + 1, f'{yoy}%', ha='center', va='bottom')

# Agregar etiquetas de valor de la variación interanual de los ingresos de la industria de catering por encima del límite
for i, above_yoy in enumerate(above_limit_yoy):
    ax2.text(i, above_yoy + 1, f'{above_yoy}%', ha='center', va='bottom')

ax1.set_title('Ingresos de la industria de catering en China y variaciones interanuales de 2017 a 2023')

plt.tight_layout()
plt.show()