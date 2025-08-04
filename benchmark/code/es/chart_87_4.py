import matplotlib.pyplot as plt
import numpy as np

# Expectativas funcionales
funciones = [
    "Alta precisión",
    "Análisis integral de los resultados de los exámenes",
    "Rápida comprensión del estado de salud ocular",
    "Alerta temprana para problemas de salud ocular",
    "Provisión de soluciones posteriores para la salud ocular",
    "Disponibilidad de archivos de seguimiento de salud",
    "Registro de cada resultado de la evaluación",
    "Métodos de examen convenientes",
    "Rápida velocidad de examen",
    "Servicio de interpretación de informes en línea",
    "Amplia gama de ítems de examen"
]
# Porcentajes correspondientes (%), los datos son consistentes con el gráfico
porcentajes = [40.9, 40.3, 37.1, 36.4, 35.8, 34.4, 33.9, 27.6, 27.0, 26.9, 22.1]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 7))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(funciones))
ancho_barra = 0.6
barras = ax.barh(y, porcentajes, height=ancho_barra, color="#395AC6")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y (ajustar el orden para que la primera función esté en la parte superior)
ax.set_yticks(y)
ax.set_yticklabels(funciones)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Expectativas de los padres sobre las funciones de los productos de salud visual de niños y adolescentes", fontsize=14, fontweight="bold")

# Embellir el gráfico ocultando los bordes superior, derecho e inferior
for espina in ["top", "right", "bottom"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()