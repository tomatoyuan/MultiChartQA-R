import matplotlib.pyplot as plt
import numpy as np

# Datos
años = np.array([2016, 2017, 2018, 2019, 2020, 2021])
porcentajes = np.array([1.8, 2.7, 4.6, 4.8, 5.4, 13.6])

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de área con relleno de color degradado
from matplotlib.collections import PolyCollection

# Crear coordenadas para el área rellena
verts = [(años[0], 0)] + list(zip(años, porcentajes)) + [(años[-1], 0)]
poly = PolyCollection([verts], facecolors=['#b2dfdb'], edgecolors='none', alpha=0.7)
ax.add_collection(poly)

# Superponer un gráfico de línea + puntos
ax.plot(años, porcentajes, marker='o', color='#00796B', linewidth=2.5, label='Proporción de producción de vehículos de energía renovable (%)')

# Agregar etiquetas de datos
for x, y in zip(años, porcentajes):
    ax.text(x, y + 0.5, f'{y}%', ha='center', fontsize=10, color='#004d40', fontweight='bold')

# Configurar los ejes
ax.set_xticks(años)
ax.set_ylim(0, max(porcentajes) + 3)
ax.set_ylabel("Proporción de producción de vehículos de energía renovable (%)")

# Agregar un título
ax.set_title("Proporción de producción de vehículos de energía renovable en China desde 2016 hasta 2021", fontsize=14, fontweight='bold')

# Leyenda
ax.legend(loc='upper left', fontsize=10)

# Embelezar el gráfico
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_alpha(0.2)
ax.spines["left"].set_alpha(0.2)

plt.tight_layout()
plt.show()