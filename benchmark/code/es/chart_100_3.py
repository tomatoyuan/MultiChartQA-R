import matplotlib.pyplot as plt
import numpy as np

# Clasificación por generación
generaciones = ["Post - 00s", "Post - 90s", "Post - 80s", "Post - 70s", "Post - 60s+"]
# Simular datos de puntuación de sueño (cerca de la imagen original)
puntuaciones = [81.7, 82.7, 83.0, 83.3, 83.5]
# Combinación de colores libre (puede ajustarse, usando la gama verde como ejemplo)
color_barra = "#A4C639"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras
x = np.arange(len(generaciones))
ancho_barra = 0.5
barras = ax.bar(x, puntuaciones, width=ancho_barra, color=color_barra)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width()/2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(generaciones)
# Establecer las marcas del eje y (80 - 85, adaptado a los datos)
ax.set_ylim(80, 85)
# Establecer el título
ax.set_title("Puntuaciones de sueño de diferentes generaciones", fontsize=14, fontweight="bold")

# Embellir: Ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()