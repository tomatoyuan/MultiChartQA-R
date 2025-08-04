import matplotlib.pyplot as plt
import numpy as np

# Factores principales
factores = [
    "Fácil de tomar",
    "Buen efecto",
    "Portátil",
    "No se siente como 'tomar medicina'",
    "Novedoso",
    "Bonito empaque"
]
# Porcentajes correspondientes (%), los datos son consistentes con el gráfico
porcentajes = [65.0, 56.0, 45.0, 38.0, 30.0, 23.0]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras (gráfico de barras horizontales, ajustado para ser consistente con la dirección del gráfico original)
y = np.arange(len(factores))
ancho_barra = 0.6
barras = ax.barh(y, porcentajes, height=ancho_barra, color="#A4C639")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y (ajustar el orden para que el primer factor esté en la parte superior)
ax.set_yticks(y)
ax.set_yticklabels(factores)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Factores principales para que los consumidores elijan 'snacks funcionales' en 2021", fontsize=14, fontweight="bold")

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()