import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
categorias = [
    "Actividades de intercambio académico",
    "Oportunidades de investigación",
    "Acceso a recursos académicos",
    "Herramientas y métodos de investigación",
    "Tendencias de la frontera disciplinar",
    "Completamente no interesado en contenido académico"
]

valores = [67.2, 52.6, 51.4, 40.6, 37.1, 0.9]

# Esquema de color verde similar a la imagen original
colores = [
    "#a5d6a7", "#81c784", "#c8e6c9", 
    "#e8f5e9", "#b9f6ca", "#f5f5f5"
]

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(categorias))

# Dibujar el gráfico de barras básico
barras = ax.barh(
    y, 
    valores, 
    color=colores, 
    edgecolor='white',
    linewidth=1
)

# Agregar etiquetas numéricas
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f'{ancho}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# -------------------- Embelezar el gráfico --------------------
# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=12, color='#424242')

# Ocultar el eje x
ax.set_xticks([])

# Ocultar los bordes
for spine in ax.spines.values():
    spine.set_visible(False)

# Ajustar la posición del eje y (hacer que el gráfico de barras esté más cerca de la izquierda)
ax.tick_params(axis='y', left=False)

# Agregar un título
ax.set_title(
    "Interés de los estudiantes universitarios en el contenido académico", 
    fontsize=14, 
    fontweight='bold', 
    pad=20
)

# Ajustar el diseño
plt.subplots_adjust(left=0.3, right=0.9, top=0.85, bottom=0.2)

plt.show()