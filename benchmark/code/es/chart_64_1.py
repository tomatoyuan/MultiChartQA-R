import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
# Categorías de satisfacción
etiquetas = [
    "Muy Satisfecho", "9 Puntos", "8 Puntos", "7 Puntos", "6 Puntos",
    "5 Puntos", "4 Puntos", "3 Puntos", "2 Puntos", "Muy Insatisfecho"
]
# Datos de porcentaje
porcentajes = [22.0, 23.6, 14.6, 17.1, 16.3, 4.9, 1.6, 0, 0, 0]
# Puntuación promedio de satisfacción
puntuacion_promedio = 7.97

# Configuración de color (similar al esquema de color verde original)
color_barra = "#a5d6a7"

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(etiquetas))

barras = ax.barh(
    y,
    porcentajes,
    color=color_barra,
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

# -------------------- Agregar anotación de satisfacción promedio (Gota azul) --------------------
# Dibujar una línea vertical
ax.axvline(
    puntuacion_promedio,
    color="lightblue",
    linestyle="--",
    linewidth=2,
    label=f"Satisfacción Promedio: {puntuacion_promedio} Puntos"
)

# Dibujar una forma de gota (simplificada como un texto anotado + flecha)
ax.annotate(
    f"{puntuacion_promedio} Puntos",
    xy=(puntuacion_promedio, len(etiquetas) / 2),
    xytext=(puntuacion_promedio + 3, len(etiquetas) / 2),
    arrowprops=dict(
        arrowstyle="->",
        color="blue",
        linewidth=1
    ),
    fontsize=12,
    color="blue",
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="lightblue",
        edgecolor="blue",
        alpha=0.8
    )
)

# -------------------- Embellir el gráfico --------------------
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
    "Satisfacción con los efectos del diseño de dominio privado por comerciantes chinos en 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()