import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
categorias = ["Uso de Internet", "Aprendizaje y Entrenamiento", "Cultura, Ocio y Entretenimiento", "Deportes y Fitness"]
años = ["2008", "2018", "2024"]

# Datos: [2008, 2018, 2024] (minutos)
datos = [
    [14, 162, 363],    # Uso de Internet: 14→162→363 (minutos)
    [27, 107, 287],    # Aprendizaje y Entrenamiento: 27→107→287 (minutos)
    [40, 105, 153],    # Cultura, Ocio y Entretenimiento: 40→105→153 (minutos)
    [23, 31, 35]       # Deportes y Fitness: 23→31→35 (minutos)
]

# Configuración de colores (similar a la imagen original)
colores = ["#a5d6a7", "#81c784", "#4dd0e1"]  # Colores correspondientes a 2008, 2018, 2024

# Configuración de anotaciones (tasa de crecimiento)
anotaciones = [
    {"año": "2018→2024", "crecimiento": 125.9, "pos": (2, 363 + 10)},
    {"año": "2008→2018", "crecimiento": 260.0, "pos": (1, 107 + 10)}
]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Dibujar el gráfico de barras agrupadas --------------------
x = np.arange(len(categorias))
ancho_barra = 0.25

for i in range(len(años)):
    ax.bar(
        x + i * ancho_barra, 
        [d[i] for d in datos], 
        width=ancho_barra, 
        color=colores[i], 
        label=años[i],
        edgecolor="white",
        linewidth=1
    )

# -------------------- Agregar anotaciones de datos (minutos) --------------------
for i in range(len(categorias)):
    for j in range(len(años)):
        valor = datos[i][j]
        ax.text(
            x[i] + j * ancho_barra, 
            valor + 5, 
            f"{valor} minutos",
            ha="center", 
            va="bottom",
            fontsize=9,
            color="#424242",
            fontweight="bold"
        )

# -------------------- Embellir el gráfico --------------------
# Establecer las etiquetas del eje x (tipos de actividad)
ax.set_xticks(x + ancho_barra)
ax.set_xticklabels(categorias, fontsize=11, color="#424242", rotation=15, ha="right")

# Establecer el rango del eje y (0 - 400 minutos, ajustado según los datos)
ax.set_ylim(0, 400)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar la leyenda
ax.legend(
    loc="upper left", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Agregar el título
ax.set_title(
    "Duración promedio diaria de actividades de los residentes nacionales",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()