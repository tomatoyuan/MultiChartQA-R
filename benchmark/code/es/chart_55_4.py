import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
grupos_edad = ["Menos de 25", "26 - 30", "31 - 35", "Más de 36"]
porcentajes = [35.5, 33.0, 17.6, 13.9]  # Porcentaje (%)

# Configuración de color (similar al verde de la imagen original)
color_barra = "#a5d6a7"

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(grupos_edad))

barras = ax.barh(
    y, 
    porcentajes, 
    color=color_barra, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar anotaciones de porcentaje --------------------
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
ax.set_yticklabels(grupos_edad, fontsize=12, color="#424242")

# Ocultar el eje x
ax.set_xticks([])

# Ocultar los bordes
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de graduación del eje y

# Agregar una leyenda (simular el estilo de la leyenda de la imagen original)
ax.legend(
    ["Porcentaje de usuarios de e - deportes por edad"],
    loc="upper right", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Agregar un título
ax.set_title(
    "Distribución por edad de los usuarios de e - deportes chinos en 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()