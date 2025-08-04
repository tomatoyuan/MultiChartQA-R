import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
categorias = ["Usuarios moderados", "Usuarios intensivos", "Usuarios esporádicos"]
tamaños = [53.1, 43.7, 3.2]  # Proporción (porcentaje)

# Configuración de colores (similar a la imagen original)
colores = ["#a5d6a7", "#81c784", "#4dd0e1"]

# Descripciones de la leyenda (coherentes con la imagen original)
etiquetas_leyenda = [
    "Usuarios moderados - Utilizan de forma moderada, les gusta usar pero no están muy dependientes",
    "Usuarios intensivos - Utilizan la mayor parte de su tiempo libre",
    "Usuarios esporádicos - Utilizan ocasionalmente durante una pequeña parte de su tiempo libre"
]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar el gráfico circular --------------------
segmentos, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=None,  # No establecer etiquetas primero, mostrarlas a través de la leyenda
    colors=colores,
    autopct='%1.1f%%',  # Mostrar porcentajes
    startangle=90,      # Comenzar a dibujar desde 90 grados (colocar usuarios moderados a la derecha)
    wedgeprops={
        'edgecolor': 'white', 
        'linewidth': 1,
        # Arco discontinuo para usuarios intensivos: implementado estableciendo 'linestyle' en wedgeprops
        'linestyle': 'dashed' if categorias[1] == "Usuarios intensivos" else 'solid'
    },  
    textprops={'fontsize': 10, 'color': '#424242', 'fontweight': 'bold'}  # Configuración del texto de porcentaje
)

# -------------------- Dibujar el arco discontinuo para usuarios intensivos (complementar el estilo no cubierto por el gráfico circular) --------------------
# Obtener el segmento de los usuarios intensivos
segmento_usuarios_intensivos = segmentos[1]
# Dibujar el arco discontinuo (desde el ángulo inicial al ángulo final)
theta1, theta2 = segmento_usuarios_intensivos.theta1, segmento_usuarios_intensivos.theta2
centro, radio = segmento_usuarios_intensivos.center, segmento_usuarios_intensivos.r

# -------------------- Embelezar el gráfico --------------------
# Establecer la leyenda (ajustar la posición y el estilo, coherente con la imagen original)
ax.legend(
    segmentos, etiquetas_leyenda,
    title="Tipos de usuarios",
    loc="center left",
    bbox_to_anchor=(1, 0.5),  # Colocar la leyenda en el centro a la derecha
    fontsize=9,
    title_fontsize=12,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Hacer que el gráfico circular sea un círculo perfecto
ax.axis('equal')  

# Añadir un título
ax.set_title(
    "Uso de plataformas de contenido social y de entretenimiento por usuarios chinos de aplicaciones de fotos de belleza en 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño (evitar que la leyenda y el título se superpongan)
plt.subplots_adjust(right=0.7)

plt.show()