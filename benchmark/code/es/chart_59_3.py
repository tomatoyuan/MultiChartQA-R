import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
tamaño_del_mercado = [804, 802, 850, 777, 862, 944, 1029, 1117, 1210]  # Tamaño del mercado (miles de millones de yuanes)
tasa_de_crecimiento = [6.0, -0.2, 6.0, -8.6, 10.9, 9.5, 9.0, 8.6, 8.3]  # Tasa de crecimiento (%)

# Configuración de colores
color_de_barras = "#a5d6a7"
color_de_linea = "#4dd0e1"

# -------------------- Crear dos subgráficos (arriba y abajo) --------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True,
                               gridspec_kw={'height_ratios': [2, 1], 'hspace': 0.15})

x = np.arange(len(años))

# -------------------- Dibujar un gráfico de barras --------------------
ax1.bar(
    x, 
    tamaño_del_mercado, 
    color=color_de_barras, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Tamaño del mercado minorista de productos de óptica chinos (miles de millones de yuanes)"
)

# Añadir etiquetas de datos del tamaño del mercado
for i, val in enumerate(tamaño_del_mercado):
    ax1.text(
        i, val + 10, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax1.set_ylabel("Tamaño del mercado (miles de millones de yuanes)", fontsize=12, color="#424242")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")
ax1.set_title("Tamaño del mercado minorista de la industria de óptica china desde 2019 - 2027e", fontsize=14, fontweight="bold", pad=10)

# -------------------- Dibujar un gráfico de línea --------------------
ax2.plot(
    x, 
    tasa_de_crecimiento, 
    color=color_de_linea, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Tasa de crecimiento (%)"
)

# Añadir etiquetas de datos de la tasa de crecimiento
for i, val in enumerate(tasa_de_crecimiento):
    ax2.text(
        i, val + 0.5, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

ax2.set_ylabel("Tasa de crecimiento (%)", fontsize=12, color="#424242")
ax2.set_ylim(min(tasa_de_crecimiento) - 5, max(tasa_de_crecimiento) + 5)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Establecer etiquetas del eje x
ax2.set_xticks(x)
ax2.set_xticklabels(años, fontsize=10, color="#424242", rotation=0)

# -------------------- Ajustar el diseño --------------------
plt.tight_layout()
plt.show()