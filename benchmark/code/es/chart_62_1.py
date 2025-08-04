import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
conteos_empresas = [681, 736, 1362, 1380, 1698, 1780, 2218, 2810]  # Número de empresas (unidades)
tasas_crecimiento = [8.1, 85.1, 1.3, 23.0, 4.8, 24.6, 26.7]  # Tasa de crecimiento (%)

# Configuración de colores (similar a la imagen original)
color_barra = "#a5d6a7"
color_linea = "#4dd0e1"

# -------------------- Crear lienzo y ejes dobles --------------------
fig, ax1 = plt.subplots(figsize=(8, 6))

# Crear eje y secundario (tasa de crecimiento)
ax2 = ax1.twinx()

# -------------------- Dibujar gráfico de barras (número de empresas) --------------------
x = np.arange(len(años))

ax1.bar(
    x,
    conteos_empresas,
    color=color_barra,
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Número de empresas chinas de diseño de circuitos integrados (unidades)"
)

# -------------------- Dibujar gráfico de línea (tasa de crecimiento) --------------------
# Los datos de tasa de crecimiento tienen un valor menos que el número de empresas (no hay tasa de crecimiento en 2014), se deben alinear los años
ax2.plot(
    x[1:],  # Comenzar desde 2015
    tasas_crecimiento,
    color=color_linea,
    marker="o",
    linewidth=2,
    markersize=5,
    label="Tasa de crecimiento del número de empresas chinas de diseño de circuitos integrados (%)"
)

# -------------------- Agregar etiquetas de datos --------------------
# Etiquetar el número de empresas
for i, val in enumerate(conteos_empresas):
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
        x[i + 1], val + 2,
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Mejorar la apariencia del gráfico --------------------
# Establecer etiquetas del eje x (años)
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=10, color="#424242")

# Establecer la etiqueta del eje y principal (número de empresas)
ax1.set_ylabel("Número de empresas chinas de \ndiseño de circuitos integrados (unidades)", fontsize=12, color="#424242")

# Establecer la etiqueta del eje y secundario (tasa de crecimiento)
ax2.set_ylabel("Tasa de crecimiento del número de empresas \nchinas de diseño de circuitos integrados (%)", fontsize=12, color="#424242")

# Ocultar bordes redundantes
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Combinar leyendas
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Agregar título
ax1.set_title(
    "Número de empresas chinas de diseño de circuitos integrados desde 2014 hasta 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()