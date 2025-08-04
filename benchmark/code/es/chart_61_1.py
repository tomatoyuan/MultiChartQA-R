import matplotlib.pyplot as plt
import numpy as np

# Datos
meses = [
    "2024.1", "2024.2", "2024.3", "2024.4", "2024.5", 
    "2024.6", "2024.7", "2024.8", "2024.9", "2024.10", 
    "2024.11", "2024.12", "2025.1", "2025.2", "2025.3"
]
conteo_dispositivos = [13.95, 13.98, 14.12, 14.03, 14.15, 14.12, 14.22, 14.26, 14.30, 14.32, 14.32, 14.34, 14.38, 14.38, 14.39]
tasas_de_crecimiento = [0.21, 0.15, 1.01, -0.63, 0.84, -0.19, 0.72, 0.29, 0.29, 0.14, -0.04, 0.19, 0.27, -0.03, 0.08]

# Esquema de colores
color_barra = "#a5d6a7"
color_linea = "#4dd0e1"
color_destacado = "#ffe0f0"
color_texto = "#424242"

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

x = np.arange(len(meses))

# Gráfico de barras
barras = ax1.bar(
    x, conteo_dispositivos, color=color_barra, width=0.6,
    edgecolor="white", linewidth=1,
    label="Dispositivos Independientes Mensuales (100 millones de unidades)"
)

# Gráfico de línea
ax2.plot(
    x, tasas_de_crecimiento, color=color_linea, marker="o",
    linewidth=2, markersize=5, label="Tasa de Crecimiento Mes a Mes (%)"
)

# Rango de los ejes
ax1.set_ylim(13.7, 14.6)
ax2.set_ylim(-1.5, 1.5)

# Etiquetas de texto para el gráfico de barras (encima de las barras)
for i, barra in enumerate(barras):
    altura = barra.get_height()
    ax1.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.02,
        f"{altura:.2f}",
        ha="center", va="bottom",
        fontsize=9, color=color_texto,
        fontweight="bold"
    )

# Etiquetas de texto para el gráfico de línea (evitar superposición)
for i, valor in enumerate(tasas_de_crecimiento):
    desplazamiento_y = 0.08 if valor >= 0 else -0.12
    va = "bottom" if valor >= 0 else "top"
    ax2.text(
        i, valor + desplazamiento_y,
        f"{valor:.2f}%",
        ha="center", va=va,
        fontsize=9, color=color_texto,
        fontweight="bold"
    )

# Destacar el área del primer trimestre
inicio_q1 = meses.index("2025.1")
fin_q1 = meses.index("2025.3")
ax1.axvspan(inicio_q1 - 0.3, fin_q1 + 0.3, facecolor=color_destacado, alpha=0.3, zorder=0)
ax1.text(
    (inicio_q1 + fin_q1) / 2, max(conteo_dispositivos) + 0.05,
    "Promedio del Primer Trimestre YoY +2.6%", ha="center", va="bottom",
    fontsize=10, color="red", fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc=color_destacado, ec="red", alpha=0.5)
)

# Eje X
ax1.set_xticks(x)
ax1.set_xticklabels(meses, rotation=45, ha="right", fontsize=10, color=color_texto)

# Etiquetas de los ejes Y
ax1.set_ylabel("Dispositivos Independientes Mensuales (100 millones de unidades)", fontsize=12, color=color_texto)
ax2.set_ylabel("Tasa de Crecimiento Mes a Mes (%)", fontsize=12, color=color_texto)

# Leyenda
lineas1, etiquetas1 = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax1.legend(lineas1 + lineas2, etiquetas1 + etiquetas2, loc="upper right", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Quitar bordes
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Título
ax1.set_title(
    "mUserTracker - Dispositivos Independientes Mensuales en Internet Móvil de China de 2024.1 a 2025.3",
    fontsize=14, fontweight="bold", pad=20
)

plt.tight_layout()
plt.show()