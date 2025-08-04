import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Fuentes de poder de crecimiento
fuentes = [
    "Propio yo interior", "Apoyo parental", "Amistad", 
    "Guía del profesor", "Modelos a inspirar", "Obras favoritas", "Desarrollo nacional estable"
]
# Datos de proporción simulados (tratar de acercarse a la imagen original)
porcentajes = [32, 32, 27, 23, 21, 16, 16]
# Configuración de colores (tratar de acercarse al gradiente verde, azul y amarillo de la imagen original)
colores = ["#A8D089", "#8CC17F", "#68B26F", "#6CBAE5", "#59A5D8", "#F7D842", "#F2B73F"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras con un fondo rayado
x = np.arange(len(fuentes))
ancho_barra = 0.6
# Primero, dibujar el fondo rayado (relleno con líneas diagonales grises)
for i in range(len(fuentes)):
    ax.bar(x[i], 100, width=ancho_barra, color='white', edgecolor='lightgray', hatch='////', zorder=0)

# Luego, dibujar las barras de primer plano de colores
barras = ax.bar(x, porcentajes, width=ancho_barra, color=colores, zorder=1)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + ancho_barra/2, altura),
                xytext=(0, 3),  # Posición de la etiqueta: 3 puntos hacia arriba
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer la escala del eje y (0 - 40%)
ax.set_ylim(0, 40)
# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(fuentes, rotation=40, ha='right')  # Rotar las etiquetas para evitar solapamiento
# Establecer el título
ax.set_title("Fuentes de poder de crecimiento de los estudiantes universitarios", fontsize=14, fontweight="bold")

# Ocultar el eje y (no hay marcas en el eje y en la imagen original)
ax.yaxis.set_visible(False)

# Ocultar los bordes superior, derecho e izquierdo
for borde in ["top", "right", "left"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()