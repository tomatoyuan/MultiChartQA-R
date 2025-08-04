import matplotlib.pyplot as plt

# -------------------- Definición de datos --------------------
etiquetas = ["Compró suplementos dietéticos en el último año", "No compró suplementos dietéticos en el último año"]
tamaños = [70.6, 29.4]  # Proporción (%)

# Configuración de colores (similar al esquema de colores de la imagen original)
colores = ["#a5d6a7", "#dcdcdc"]

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Dibujar un gráfico circular --------------------
porciones, etiquetas_texto, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",  # Mostrar porcentaje
    startangle=90,      # Ángulo de inicio (colocar la parte de "Compró" a la derecha)
    colors=colores,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "linewidth": 2, 
        "edgecolor": "white"
    }
)

# -------------------- Embellir el gráfico --------------------
# Establecer el título
ax.set_title(
    "Proporción de personas que compraron suplementos dietéticos en el último año",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar la posición de la leyenda (simular el diseño de la imagen original)
ax.legend(
    loc="upper left", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Optimizar el diseño
plt.tight_layout()

plt.show()