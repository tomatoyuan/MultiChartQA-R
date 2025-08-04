import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2019", "2020", "2021", "2022", "2023", "2024Q1-Q3"]
# Ingresos operativos totales (en cientos de millones de yuanes)
total_revenue = [86624, 98514, 119064, 121805, 129515, 99668]
# Ingresos operativos en el nuevo formato (en cientos de millones de yuanes)
new_format_revenue = [19868, 31425, 39623, 43860, 52395, 41616]
# Proporción (%)
proportion = [22.9, 31.9, 33.3, 36.0, 40.5, 41.8]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras de los ingresos operativos totales
ax1.bar(x, total_revenue, color='lightcoral', label='Ingresos operativos totales (en cientos de millones de yuanes)', width=0.3)
# Trazar el gráfico de barras de los ingresos operativos en el nuevo formato (desplazado hacia la derecha para evitar superposición)
ax1.bar(x + 0.3, new_format_revenue, color='coral', label='Ingresos operativos en el nuevo formato (en cientos de millones de yuanes)', width=0.3)
ax1.set_ylabel('Ingresos operativos (en cientos de millones de yuanes)')
ax1.set_xlabel('Años')
ax1.set_xticks(x + 0.15)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la proporción
ax2 = ax1.twinx()
ax2.plot(x, proportion, marker='o', color='gold', label='Proporción (%)')
ax2.set_ylabel('Proporción (%)')
ax2.legend(loc='upper right')

# Agregar etiquetas de valor para los ingresos operativos totales
for i, rev in enumerate(total_revenue):
    ax1.text(i, rev + 1000, f'{rev}', ha='center', va='bottom')

# Agregar etiquetas de valor para los ingresos operativos en el nuevo formato
for i, new_rev in enumerate(new_format_revenue):
    ax1.text(i + 0.3, new_rev + 1000, f'{new_rev}', ha='center', va='bottom')

# Agregar etiquetas de valor para la proporción
for i, prop in enumerate(proportion):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')

ax1.set_title('Ingresos operativos de los nuevos formatos culturales en China desde 2019 hasta 2024')

plt.tight_layout()
plt.show()