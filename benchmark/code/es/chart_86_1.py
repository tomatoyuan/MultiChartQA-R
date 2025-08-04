import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = ["2019", "2020", "2021"]
cantidad = [12, 14, 17]
x = np.arange(len(años))

# Tamaño y color de las burbujas
tamaños = np.array(cantidad) ** 2.5 * 5  # Ajusta el exponente para ampliar la diferencia
colores = ["#90caf9", "#ce93d8", "#f48fb1"]  # Esquema de colores degradado azul - púrpura - rosa

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- Dibujar un gráfico de burbujas --------------------
for i in range(len(x)):
    ax.scatter(
        x[i], cantidad[i],
        s=tamaños[i],
        color=colores[i],
        alpha=0.7,
        edgecolors="white",
        linewidth=2
    )
    # Agregar etiquetas de datos
    ax.text(
        x[i], cantidad[i] + 0.5,
        f"{cantidad[i]}",
        ha='center', va='bottom',
        fontsize=14,
        fontweight='bold',
        color='white'
    )

# -------------------- Configurar los ejes --------------------
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11, color="#424242")
ax.set_yticks([])  # No mostrar las marcas del eje y
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylim(0, max(cantidad) + 5)

# -------------------- Título y decoración --------------------
ax.set_title(
    "Tendencia del número de programas de variedades y programas de variedades orientados a mujeres desde 2019 hasta 2021 en SVC",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Decorar el borde
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()