import matplotlib.pyplot as plt
import numpy as np

# Categorías de gastos de consumo
categorias = [
    "Alimentos y Tabaco", "Vivienda", "Transporte y Comunicación", "Educación, Cultura y Entretenimiento", 
    "Cuidado de la Salud", "Ropa", "Bienes y Servicios para el Hogar", "Otros Bienes y Servicios"
]
# Datos de proporción correspondientes (%)
datos = [29.8, 23.4, 13.1, 10.8, 8.8, 5.9, 5.9, 2.4]
# Configuración de color, similar al color verde de la imagen original
color = "#A4C639"

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(categorias))
altura_barra = 0.6
barras = ax.barh(y, datos, height=altura_barra, color=color, edgecolor="white")

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
ax.set_title("Composición del Gasto de Consumo Per Cápita de los Residentes Chinos en 2021", fontsize=14, fontweight="bold")

# Embellir el gráfico, ocultar los bordes superior, derecho e inferior
for espina in ["top", "right", "bottom"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()