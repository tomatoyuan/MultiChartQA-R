import matplotlib.pyplot as plt
import numpy as np

# Definición de datos (correspondiente a la estructura de la imagen original, los valores numéricos se pueden ajustar)
grupos_edad = ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "≥60"]
porcentajes = [23.3, 17.3, 17.3, 13.3, 10.2, 7.6, 5.3, 2.8, 2.8]  # Datos de porcentaje
tgis = [159, 119, 93, 90, 89, 76, 69, 63, 75]  # Datos de TGI

# Configuración de color (similar al esquema de color verde de la imagen original)
color_barra = "#81c784"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(grupos_edad))
barras = ax.barh(y, porcentajes, color=color_barra, height=0.6, edgecolor="white", linewidth=1)

# Agregar etiquetas de valores de porcentaje
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height() / 2,
        f"{ancho}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Agregar etiquetas de TGI (en el lado izquierdo de las barras, simulando el diseño de la imagen original)
for i, (edad, tgi) in enumerate(zip(grupos_edad, tgis)):
    ax.text(
        -3,  # Desplazamiento hacia la izquierda, se puede ajustar según la situación real
        y[i] + barra.get_height() / 2,
        f"TGI: {tgi}",
        va="center",
        ha="right",
        fontsize=9,
        color="#424242"
    )

# Embellir el gráfico
ax.set_yticks(y)
ax.set_yticklabels(grupos_edad, fontsize=12, color="#424242")
ax.set_xticks([])  # Ocultar las marcas de graduación del eje x

# Ocultar el marco
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de graduación del eje y

# Agregar un título
ax.set_title(
    "Leche en polvo proteica: Grupos de edad",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño (centrar el contenido y dejar espacio para las etiquetas de TGI del lado izquierdo)
plt.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.1)

plt.show()