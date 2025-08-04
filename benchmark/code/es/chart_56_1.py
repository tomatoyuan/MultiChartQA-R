import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = ["2020", "2021", "2022", "2023", "2024", "2025e", "2026e", "2027e"]
tamaño_del_mercado = [12379.2, 27365.3, 36369.2, 49168.4, 57863.8, 68048.4, 78086.4, 87871.0]  # Tamaño del mercado (en miles de millones de yuanes)
tasa_de_crecimiento = [121.1, 32.9, 35.2, 17.7, 17.6, 14.8, 12.5]  # Tasa de crecimiento (%)

# Configuración de colores (similar a la imagen original)
color_de_barras = "#a5d6a7"
color_de_linea = "#4dd0e1"

# -------------------- Crear un lienzo y ejes dobles --------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# Crear un eje y secundario (tasa de crecimiento)
ax2 = ax1.twinx()

# -------------------- Dibujar un gráfico de barras (tamaño del mercado) --------------------
x = np.arange(len(años))

ax1.bar(
    x, 
    tamaño_del_mercado, 
    color=color_de_barras, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Tamaño del Mercado de Comercio Electrónico por Transmisión en Vivo en China (en miles de millones de yuanes)"
)

# -------------------- Dibujar un gráfico de línea (tasa de crecimiento) --------------------
ax2.plot(
    x[:-1],  # Los datos de tasa de crecimiento tienen un elemento menos que los años (no hay tasa de crecimiento para 2027e)
    tasa_de_crecimiento, 
    color=color_de_linea, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Tasa de Crecimiento (%)"
)

# -------------------- Agregar etiquetas de datos --------------------
# Etiquetar el tamaño del mercado
for i, val in enumerate(tamaño_del_mercado):
    ax1.text(
        i, val + 1000, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Etiquetar la tasa de crecimiento
for i, val in enumerate(tasa_de_crecimiento):
    ax2.text(
        i, val + 2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Embelezar el gráfico --------------------
# Establecer las etiquetas del eje x (años)
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=10, color="#424242")

# Establecer la etiqueta del eje y primario (tamaño del mercado)
ax1.set_ylabel("Tamaño del Mercado (en miles de millones de yuanes)", fontsize=12, color="#424242")

# Establecer la etiqueta del eje y secundario (tasa de crecimiento)
ax2.set_ylabel("Tasa de Crecimiento (%)", fontsize=12, color="#424242")

# Ocultar bordes redundantes
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combinar leyendas (ajustar la posición, moverla hacia arriba)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines1 + lines2, 
    labels1 + labels2, 
    loc="upper left", 
    bbox_to_anchor=(0, 1.2),  # Mover la leyenda hacia arriba
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Agregar un título
ax1.set_title(
    "Tamaño y Tasa de Crecimiento del Mercado de Comercio Electrónico por Transmisión en Vivo en China",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()