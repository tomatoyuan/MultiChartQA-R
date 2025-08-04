import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2011, 2021)

# Datos (ejemplo, se pueden ajustar según la situación real)
# China: Costo logístico como porcentaje del PIB (%)
china_logistics = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7]
# China: Costo de almacenamiento como porcentaje del PIB (%)
china_storage = [5.1, 5.2, 5.3, 5.3, 5.1, 5.0, 4.7, 5.1, 5.0, 5.0]
# EE. UU.: Costo logístico como porcentaje del PIB (%)
usa_logistics = [7.8, 7.8, 7.8, 7.8, 7.6, 7.4, 8.0, 7.8, 7.6, 7.4]
# EE. UU.: Costo de almacenamiento como porcentaje del PIB (%)
usa_storage = [3.6, 3.9, 3.1, 3.0, 2.5, 2.4, 2.2, 2.6, 2.5, 2.5]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 20)

# Trazar la línea del porcentaje del costo logístico de China
ax.plot(years, china_logistics, marker='o', color='#8BC34A', label='China: Costo logístico como % del PIB', linewidth=2)
# Trazar la línea del porcentaje del costo logístico de EE. UU.
ax.plot(years, usa_logistics, marker='o', color='#2196F3', label='EE. UU.: Costo logístico como % del PIB', linewidth=2)
# Trazar la línea del porcentaje del costo de almacenamiento de China
ax.plot(years, china_storage, marker='o', color='#FFC107', label='China: Costo de almacenamiento como % del PIB', linewidth=2)
# Trazar la línea del porcentaje del costo de almacenamiento de EE. UU.
ax.plot(years, usa_storage, marker='o', color='#F48FB1', label='EE. UU.: Costo de almacenamiento como % del PIB', linewidth=2)

# Agregar etiquetas de datos
for y_arr, color in zip([china_logistics, usa_logistics, china_storage, usa_storage], 
                        ['#8BC34A', '#2196F3', '#FFC107', '#F48FB1']):
    for x, y in zip(years, y_arr):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(0, 3),
                    textcoords='offset points',
                    ha='center',
                    va='bottom',
                    color=color)

# Establecer los ejes y el título
ax.set_xlabel('Año')
ax.set_ylabel('Porcentaje (%)')
ax.set_title('Comparación del costo logístico como porcentaje del PIB entre China y EE. UU. de 2011 a 2020', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Agregar una leyenda
ax.legend(loc='upper right')

# Embellimiento: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()