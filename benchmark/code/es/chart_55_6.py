import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
grupos_de_consumo = [
    "Por debajo de 1000 yuanes",
    "De 1001 a 2000 yuanes",
    "De 2001 a 3000 yuanes",
    "De 3001 a 5000 yuanes",
    "De 5001 a 8000 yuanes",
    "De 8001 a 10000 yuanes",
    "Por encima de 10000 yuanes"
]
porcentajes = [8.1, 15.8, 25.9, 27.1, 14.7, 4.0, 4.5]  # Porcentaje (%)

# Configuración de color (similar al verde de la imagen original)
color_barra = "#a5d6a7"

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(grupos_de_consumo))

barras = ax.barh(
    y, 
    porcentajes, 
    color=color_barra, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar etiquetas de porcentaje --------------------
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f"{ancho}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# -------------------- Embellir el gráfico --------------------
# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(grupos_de_consumo, fontsize=12, color="#424242")

# Ocultar el eje x
ax.set_xticks([])

# Ocultar los bordes
for espina in ax.spines.values():
    espina.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de graduación del eje y

# Agregar una leyenda (simular el estilo de la leyenda de la imagen original)
ax.legend(
    ["Porcentaje de gasto de consumo mensual de los usuarios"],
    loc="upper right", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Agregar un título
ax.set_title(
    "Nivel de consumo personal mensual de los usuarios de deportes electrónicos chinos en 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()