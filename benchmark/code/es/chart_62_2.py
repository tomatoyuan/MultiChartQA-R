import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
escala_ventas = [1047, 1325, 1644, 2074, 2519, 3064, 3778, 4519]  # Escala de ventas (miles de millones de yuanes)
tasas_crecimiento = [26.5, 24.1, 26.1, 21.5, 21.6, 23.3, 19.6]        # Tasa de crecimiento (%)

# Configuración de colores (similar a la imagen original)
color_barra = "#a5d6a7"
color_linea = "#4dd0e1"

# -------------------- Crear un lienzo y un eje y secundario --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# Crear un eje y secundario (tasa de crecimiento)
ax2 = ax1.twinx()

# -------------------- Dibujar un gráfico de barras (escala de ventas) --------------------
x = np.arange(len(años))

ax1.bar(
    x, 
    escala_ventas, 
    color=color_barra, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Escala de Ventas de la Industria de Diseño de \nCircuitos Integrados de China (miles de millones de yuanes)"
)

# -------------------- Dibujar un gráfico de línea (tasa de crecimiento) --------------------
# Los datos de la tasa de crecimiento tienen un valor menos que la escala de ventas (no hay tasa de crecimiento en 2014), se deben alinear los años
ax2.plot(
    x[1:],  # Comenzar desde 2015
    tasas_crecimiento, 
    color=color_linea, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Tasa de Crecimiento de la Escala de Ventas de \nla Industria de Diseño de Circuitos Integrados de China (%)"
)

# -------------------- Agregar etiquetas de datos --------------------
# Etiquetar la escala de ventas
for i, val in enumerate(escala_ventas):
    ax1.text(
        i, val + 50, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Etiquetar la tasa de crecimiento
for i, val in enumerate(tasas_crecimiento):
    # La tasa de crecimiento corresponde a los años de 2015 - 2021 (x[1] a x[7])
    ax2.text(
        x[i+1], val + 0.5, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Mejorar la apariencia del gráfico --------------------
# Establecer las etiquetas del eje x (años)
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=10, color="#424242")

# Establecer la etiqueta del eje y primario (escala de ventas)
ax1.set_ylabel("Escala de Ventas de la Industria de Diseño de Circuitos\n Integrados de China (miles de millones de yuanes)", fontsize=12, color="#424242")

# Establecer la etiqueta del eje y secundario (tasa de crecimiento)
ax2.set_ylabel("Tasa de Crecimiento de la Escala de Ventas de\n la Industria de Diseño de Circuitos Integrados de China (%)", fontsize=12, color="#424242")

# Ocultar bordes redundantes
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combinar leyendas
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Agregar un título
ax1.set_title(
    "Escala de Ventas de la Industria de Diseño de Circuitos Integrados de China de 2014 - 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()