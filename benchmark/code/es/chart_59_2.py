import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
años = [2018, 2019, 2020, 2021, 2022]
tasas = [53.60, 50.20, 52.70, 52.60, 51.90]  # Tasa de miopía (%)

# Configuración de color (similar al verde de la imagen original)
color_linea = "#a5d6a7"

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar el gráfico de líneas --------------------
ax.plot(
    años,
    tasas,
    color=color_linea,
    marker="o",
    linewidth=2,
    markersize=5,
    label="Tasa"
)

# -------------------- Agregar anotaciones de datos --------------------
for i, val in enumerate(tasas):
    ax.text(
        años[i], val + 0.2,
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Embellir el gráfico --------------------
# Establecer las etiquetas del eje x (años)
ax.set_xticks(años)
ax.set_xticklabels(años, fontsize=10, color="#424242")

# Establecer el rango del eje y (49 - 55%, ajustado según los datos)
ax.set_ylim(49, 55)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar la leyenda
ax.legend(
    loc="upper right",
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Agregar el título
ax.set_title(
    "Tasa nacional de miopía en niños y adolescentes de 2018 a 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()