import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
# Categorías de frecuencia de toma de fotos
etiquetas = [
    "Más de 5 veces al día en promedio", "De 2 a 5 veces al día en promedio", "Una vez al día en promedio",
    "De 4 a 6 veces a la semana en promedio", "De 2 a 3 veces a la semana en promedio", "Una vez a la semana en promedio",
    "Menos de una vez a la semana en promedio"
]
# Datos de porcentaje
porcentajes = [6.4, 27.1, 18.7, 20.9, 15.7, 5.9, 5.4]

# Índices de grupo (Los primeros tres elementos son "Toman fotos al menos una vez al día en promedio")
indices_grupo = [0, 1, 2]  # Índices de los primeros tres elementos

# Configuración de colores (Similar al esquema de color verde de la imagen original)
colores_barras = ["#a5d6a7"] * len(etiquetas)

# Texto de anotación (Caja azul en la esquina superior derecha)
texto_anotacion = "Los usuarios que toman fotos al menos una vez al día en promedio\nrepresentan el 52.2%"
caja_anotacion = {
    "boxstyle": "round,pad=0.5",
    "facecolor": "lightblue",
    "edgecolor": "blue",
    "alpha": 0.8
}

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(etiquetas))

barras = ax.barh(
    y, 
    porcentajes, 
    color=colores_barras, 
    height=0.6
)

# -------------------- Agregar anotaciones de datos --------------------
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1, 
        barra.get_y() + barra.get_height() / 2,
        f"{ancho}%",
        va="center", 
        fontsize=9, 
        color="#424242",
        fontweight="bold"
    )

# -------------------- Dibujar una caja discontinua para el grupo --------------------
# Encontrar las coordenadas y mínimas y máximas del grupo
min_y = min([y[i] for i in indices_grupo]) - 0.3
max_y = max([y[i] for i in indices_grupo]) + 0.3
max_ancho = max([porcentajes[i] for i in indices_grupo]) + 3  # Ancho de la caja discontinua

# Dibujar la caja discontinua
ax.plot([0, max_ancho], [min_y, min_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, max_ancho], [max_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([max_ancho, max_ancho], [min_y, max_y], color="blue", linestyle="--", linewidth=1)
ax.plot([0, 0], [min_y, max_y], color="blue", linestyle="--", linewidth=1)

# -------------------- Agregar una anotación en la esquina superior derecha --------------------
ax.text(
    max_ancho - 2,  # Posición horizontal
    max_y + 0.5,    # Posición vertical (Por encima de la caja discontinua)
    texto_anotacion,
    fontsize=9,
    color="blue",
    fontweight="bold",
    bbox=caja_anotacion
)

# -------------------- Emprolijar el gráfico --------------------
# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(etiquetas, fontsize=10)

# Ocultar las marcas del eje x
ax.set_xticks([])

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar un título
ax.set_title(
    "Frecuencia de toma de fotos de retrato por usuarios chinos de aplicaciones de maquillaje virtual en 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()