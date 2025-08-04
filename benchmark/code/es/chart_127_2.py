import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
utilidad_neta = [791.30, 646.83, 432.49, 417.85, 486.40, 567.37, 659.31]
tasa_de_crecimiento = [-0.4, -18.3, -33.1, -3.4, 16.4, 16.6, 16.2]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras de la utilidad neta atribuible a la empresa matriz
barras = ax1.bar(x, utilidad_neta, color='orange', label='Utilidad neta atribuible a la empresa matriz (100 millones de yuanes)', width=0.4)
ax1.set_ylabel('Utilidad neta atribuible a la empresa matriz (100 millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='center left')

# Añadir etiquetas para la utilidad neta atribuible a la empresa matriz
for i, utilidad in enumerate(utilidad_neta):
    ax1.text(i, utilidad + 10, f'{utilidad}', ha='center', va='bottom')

# Crear un eje y secundario y dibujar el gráfico de línea de la tasa de crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de crecimiento interanual (%)', linewidth=2)
ax2.set_ylabel('Tasa de crecimiento interanual (%)')
ax2.legend(loc='center right')

# Añadir etiquetas para la tasa de crecimiento interanual
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 1, f'{tasa}%', ha='center', va='bottom', color='red')

ax1.set_title('Utilidad neta atribuible a la empresa matriz de empresas fabricantes de vehículos eléctricos nuevos cotizadas en el mercado de acciones A de China desde 2017 hasta 2023')

plt.tight_layout()
plt.show()