import matplotlib.pyplot as plt
import numpy as np

# Texto de las categorías
etiquetas = ["Suplementación diaria regular requerida", "Suplementación periódica es suficiente, por ejemplo, en la infancia, vejez o embarazo", "Suplementación solo necesaria cuando está enfermo o presenta síntomas"]
# Datos correspondientes
tamaños = [51, 17, 16]
# Colores para diferentes categorías, intentando ser un gradiente en el esquema de color similar al verde de la imagen original
colores = ["#A4C639", "#A4C639", "#6E8B3D"]

x = np.arange(len(etiquetas))  # Se utiliza para establecer la posición del eje x
ancho_barra = 0.5  # Ancho del gráfico de barras

fig, ax = plt.subplots()
# Dibujar el gráfico de barras. Un gráfico de barras horizontal se asemeja más a la forma de visualización de la imagen original, por lo que se usa barh
barras = ax.barh(x, tamaños, height=ancho_barra, color=colores, edgecolor="white")

# Agregar etiquetas de datos
for i, barra in enumerate(barras):
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Distancia horizontal de la etiqueta desde el gráfico de barras
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y para que las etiquetas sean más claras
ax.set_yticks(x)
ax.set_yticklabels(etiquetas)
# Establecer el título del gráfico
ax.set_title("Top 3 de conciencia sobre suplementos para la salud de mascotas", fontsize=14, fontweight="bold")

# Embelezar el gráfico ocultando los bordes superior y derecho
for espina in ["top", "right", "bottom", "left"]:
    ax.spines[espina].set_visible(False)

# Ajustar el rango del eje x para que las etiquetas se muestren más adecuadamente
ax.set_xlim(0, max(tamaños) + 5)
# Ocultar las marcas del eje x
ax.set_xticks([])

plt.show()