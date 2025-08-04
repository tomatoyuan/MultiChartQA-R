import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# Categorías y datos correspondientes
categorias = ["Pañales", "Pañales de tiro", "Folletos de pañales desechables"]
datos = [78.2, 76.4, 51.6]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras horizontales
x = np.arange(len(categorias))
ancho_barra = 0.4
barras = ax.barh(x, datos, height=ancho_barra, color="#C63982")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(x)
ax.set_yticklabels(categorias)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Categorías de productos de pañales para bebés compradas por consumidores chinos en 2022", fontsize=12, fontweight="bold")

# Embelezar el gráfico ocultando los bordes superior, derecho e inferior
for espina in ["top", "right", "bottom"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()