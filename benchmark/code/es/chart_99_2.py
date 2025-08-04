import matplotlib.pyplot as plt
import numpy as np

# Categorías de frecuencia de consumo de alimentos
frecuencias = [
    "Una vez al día o más", "Una vez cada dos o tres días", 
    "Una vez cada cuatro o cinco días", "Una vez a la semana", 
    "Una vez cada dos semanas", "Menos de una vez cada dos semanas"
]
# Datos de proporción simulados (cercanos al gráfico original)
porcentajes = [54.9, 27.7, 11.6, 4.1, 1.1, 0.1]
# Esquema de colores libre (ajustable, el ejemplo usa azul)
color_barra = "#87CEEB"  # Puede ser reemplazado por otros colores como "#FF8C00"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(frecuencias))
altura_barra = 0.6
barras = ax.barh(y, porcentajes, height=altura_barra, color=color_barra)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra/2),
                xytext=(5, 0),  # Posición de la etiqueta: desplazamiento de 5 hacia la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(frecuencias)
# Establecer las marcas del eje x (0 - 60%)
ax.set_xlim(0, 60)
# Establecer el título
ax.set_title("Frecuencia de consumo de frutas", fontsize=14, fontweight="bold")

# Embelezar: Ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()