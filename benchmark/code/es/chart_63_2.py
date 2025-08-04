import matplotlib.pyplot as plt
import numpy as np

# Datos (Nombres, Porcentajes)
etiquetas = [
    "Varias veces al día en promedio", "Una vez al día en promedio", "Una vez cada 2 - 3 días en promedio",
    "Una vez cada 4 - 6 días en promedio", "Una vez a la semana en promedio", "2 - 3 veces al mes en promedio",
    "Una vez al mes en promedio", "Casi nunca"
]
porcentajes = [8.4, 13.5, 28.2, 12.2, 12.9, 10.9, 7.2, 6.7]

# Configuración de colores (Cerca del esquema de color verde original, usar gris para "Casi nunca")
colores = ["#a5d6a7"] * 7 + ["#d3d3d3"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(etiquetas))
barras = ax.barh(y, porcentajes, color=colores, height=0.6)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height() / 2,
            f"{ancho}%", va="center", fontsize=9, color="#333")

# Dibujar un cuadro discontinuo azul (Seleccionar los tres primeros elementos)
ax.plot([0, max(porcentajes) + 5], [y[0] - 0.3, y[0] - 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max(porcentajes) + 5], [y[2] + 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([max(porcentajes) + 5, max(porcentajes) + 5], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [y[0] - 0.3, y[2] + 0.3], color="blue", linestyle="--", linewidth=1)

# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(etiquetas, fontsize=10)

# Ocultar las marcas del eje x
ax.set_xticks([])

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar un título
ax.set_title("Frecuencia de publicación de contenido original por usuarios de aplicaciones de fotografía de belleza chinas en 2022", fontsize=14, fontweight="bold", pad=20)

# Ajustar el diseño
plt.tight_layout()
plt.show()