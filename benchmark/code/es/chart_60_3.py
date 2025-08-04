import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
categorias = ["Ciclo de reemplazo"]
etiquetas = ["Menos de 1 año", "1 - 2 años", "2 - 3 años", "3 - 5 años", "Más de 5 años"]
tamaños = [5.7, 41.4, 39.3, 11.1, 2.6]  # Proporción (%)
colores = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # Configuración de colores

# Crear un lienzo: aumentar la altura y disminuir el ancho para hacer el gráfico más alto y delgado
fig, ax = plt.subplots(figsize=(6, 5))  # Ajustar a ancho 6 y altura 5

# Dibujar un gráfico de barras segmentadas (eliminar el parámetro de altura incorrecto)
inicio = 0
for i in range(len(tamaños)):
    ax.bar(
        categorias, 
        tamaños[i], 
        bottom=inicio, 
        color=colores[i], 
        edgecolor="white",
        linewidth=1,
        label=etiquetas[i]
    )
    # Agregar etiquetas de datos
    ax.text(
        categorias[0], 
        inicio + tamaños[i]/2, 
        f"{tamaños[i]}%",
        ha="center", 
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )
    inicio += tamaños[i]

# Ocultar el eje y (solo mantener las categorías del eje x)
ax.set_yticks([])

# Ocultar los bordes superior, derecho e izquierdo
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Establecer etiquetas del eje x
ax.set_xticklabels(categorias, fontsize=10, color="#424242")

# Agregar una leyenda (ajustar la posición a la parte inferior y organizarla horizontalmente)
ax.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.25),  # Ajustar finamente la posición de la leyenda
    ncol=len(etiquetas),            # Organizar horizontalmente
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Agregar un título
ax.set_title(
    "Ciclo de reemplazo de gafas de marco",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño (hacer espacio para la leyenda)
plt.subplots_adjust(bottom=0.25)

plt.show()