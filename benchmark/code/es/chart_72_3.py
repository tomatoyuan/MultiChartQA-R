import matplotlib.pyplot as plt
import numpy as np

# Categorías de estado de atención
categorias = ["Aumento de la atención", "Sin cambio significativo, siempre muy preocupados", "Menos preocupados"]
# Datos de proporción correspondientes (%)
datos = [76.0, 19.0, 5.0]
# Configuración de color, similar al color a base de verde en la imagen original
color = "#8239C6"

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(categorias))
altura_barra = 0.6
barras = ax.barh(y, datos, height=altura_barra, color=color, edgecolor="white")

# Agregar un borde discontinuo rojo a "Aumento de la atención"
rect = plt.Rectangle((0, y[0] - altura_barra/2), datos[0], altura_barra, fill=False, edgecolor='red', linestyle='--')
ax.add_patch(rect)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("La atención de los consumidores hacia la naturaleza premium de los ingredientes/formulas de la leche en polvo", fontsize=14, fontweight="bold")

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()