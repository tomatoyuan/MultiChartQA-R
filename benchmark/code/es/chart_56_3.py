import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
etiquetas = ["Muy Satisfecho", "Bastante Satisfecho", "Promedio", "Algo Insatisfecho", "Completamente Insatisfecho"]
tamaños = [7.8, 37.4, 46.9, 4.6, 3.4]  # Proporción (%)
colores = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # Configuración de colores (similar a la imagen original)

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar el gráfico de pastel --------------------
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",  # Mostrar porcentaje
    startangle=140,     # Ángulo de inicio (ajustar la posición del sector)
    colors=colores,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# -------------------- Agregar anotación (Solo el 45.2% de los consumidores está satisfecho) --------------------
# Calcular la proporción de consumidores satisfechos (Muy Satisfecho + Bastante Satisfecho)
porcentaje_satisfechos = tamaños[0] + tamaños[1]
ax.annotate(
    f"Solo el {porcentaje_satisfechos:.1f}% de los consumidores está satisfecho con el producto",
    xy=(1.1, 0.8),  # Posición de la anotación (arriba a la derecha)
    xytext=(1.3, 0.9), 
    arrowprops=dict(
        facecolor="pink", 
        edgecolor="pink", 
        arrowstyle="->", 
        linewidth=1
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="pink", ec="pink", alpha=0.5)
)

# -------------------- Embelezar el gráfico --------------------
# Establecer el título
ax.set_title(
    "Nivel de satisfacción de los consumidores de comercio electrónico en directo con los productos",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar la posición de la leyenda a la derecha fuera del gráfico
ax.legend(
    loc="center left",  # Posicionar la leyenda a la derecha
    bbox_to_anchor=(1, 0.5),  # Mover la leyenda fuera del gráfico
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Optimizar el diseño
plt.tight_layout()

plt.show()