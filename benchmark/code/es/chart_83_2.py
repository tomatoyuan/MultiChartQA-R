import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# -------------------- Definición de Datos --------------------
años = ["2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e"]
tamaño_del_mercado = [667, 817, 1011, 1266, 1618, 2079, 2686]
x = np.arange(len(años))
ancho_de_la_barra = 0.3

# -------------------- Esquema de Colores (Degradado + Estilo Lindo) --------------------
colores = ['#A5D6A7', '#81C784', '#4DD0E1', '#4FC3F7', '#9575CD', '#BA68C8', '#F48FB1']

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# Establecer un rango adecuado en el eje y para evitar que las barras sean demasiado altas y salgan de la imagen
altura_maxima = max(tamaño_del_mercado)
ax.set_ylim(0, altura_maxima * 1.15)  # 115% del valor máximo

# -------------------- Dibujar barras de rectángulos redondeados --------------------
for i in range(len(x)):
    altura_de_la_barra = tamaño_del_mercado[i]
    color_de_la_barra = colores[i % len(colores)]
    # Usar FancyBboxPatch para dibujar un rectángulo redondeado (barra)
    rect = FancyBboxPatch(
        (x[i] - ancho_de_la_barra / 2, 0),     # Esquina inferior izquierda
        ancho_de_la_barra, altura_de_la_barra,         # Ancho y altura
        boxstyle="round,pad=0.02,rounding_size=6",  # Configuración de la esquina redondeada
        linewidth=0,
        facecolor=color_de_la_barra,
        edgecolor=None
    )
    ax.add_patch(rect)

    # Agregar etiquetas de datos
    ax.text(
        x[i], altura_de_la_barra + 50,
        f"{altura_de_la_barra}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=color_de_la_barra
    )

# -------------------- Ejes y Decoración --------------------
# Establecer el eje x
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11, color="#424242")
# Establecer la etiqueta del eje y
ax.set_ylabel("Tamaño y Espacio del Mercado de los Servicios \nMédicos de Rehabilitación en China (Miles de Millones de Yuan)", fontsize=11)

# Agregar la etiqueta de CAGR (esquina superior izquierda)
ax.text(
    0.05, 0.93,
    "CAGR = 38.5%",
    transform=ax.transAxes,
    fontsize=12,
    fontweight="bold",
    color="#F06292",
    bbox=dict(facecolor="#ffe0f0", alpha=0.6, boxstyle="round,pad=0.3", edgecolor='none')
)

# Agregar el título
ax.set_title("Tamaño y Espacio del Mercado de los Servicios Médicos de Rehabilitación en China de 2019 - 2025", fontsize=14, fontweight="bold", pad=20)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Diseño automático
plt.tight_layout()
plt.show()