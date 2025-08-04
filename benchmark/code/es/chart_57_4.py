import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# -------------------- Definición de Datos --------------------
años = ["2025p", "2026p", "2027p"]
tamaño_del_mercado = [8.1, 9.4, 10.9]  # Tamaño del mercado (en miles de millones de yuanes)
tasa_de_crecimiento = [13.9, 16.6, 15.9]  # Tasa de crecimiento (%)

# Configuración de colores (similar a la imagen original)
color_de_barra = "#a5d6a7"
color_de_linea = "#4dd0e1"
color_de_cagr = "#a5d6a7"  # Color de la línea de tendencia CAGR

# -------------------- Cargar ilustración (simulación simplificada, se puede reemplazar con imagen precisa) --------------------
# Aquí usamos formas simples para la simulación. Si se necesitan ilustraciones precisas, reemplácela con la ruta de la imagen real.
# img = mpimg.imread('phone_illustration.png')  # Ruta real de la ilustración
# Temporalmente usamos bloques de color para simular la posición de la ilustración
ilustración = plt.Circle((0, 0), 1, color='lightblue')

# -------------------- Crear el lienzo y los ejes duales --------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# Crear el eje y secundario (tasa de crecimiento)
ax2 = ax1.twinx()

# -------------------- Dibujar el gráfico de barras (tamaño del mercado) --------------------
x = np.arange(len(años))

ax1.bar(
    x, 
    tamaño_del_mercado, 
    color=color_de_barra, 
    width=0.6,
    edgecolor="white",
    linewidth=1,
    label="Tamaño del Mercado de la SaaS de Marketing de Influenciadores Extranjeros de China (en miles de millones de yuanes)"
)

# -------------------- Dibujar el gráfico de línea (tasa de crecimiento) --------------------
ax2.plot(
    x, 
    tasa_de_crecimiento, 
    color=color_de_linea, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Tasa de Crecimiento (%)"
)

# -------------------- Dibujar la línea de tendencia CAGR y la anotación --------------------
# Calcular CAGR (simplificado para la ilustración, el cálculo real requiere una fórmula)
cagr = 15.0
ax1.annotate(
    f"CAGR≈{cagr}%",
    xy=(2, 10.9),  # Punto de inicio de la flecha (parte superior de la barra de 2027p)
    xytext=(2.2, 10.9), 
    arrowprops=dict(
        facecolor=color_de_cagr, 
        edgecolor=color_de_cagr, 
        arrowstyle="->", 
        linewidth=2
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.5)
)

# -------------------- Agregar anotaciones de datos --------------------
# Anotar el tamaño del mercado
for i, val in enumerate(tamaño_del_mercado):
    ax1.text(
        i, val + 0.2, 
        f"{val}",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# Anotar la tasa de crecimiento
for i, val in enumerate(tasa_de_crecimiento):
    ax2.text(
        i, val + 0.5, 
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

# Combinar las leyendas
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="center left", fontsize=9, frameon=True, facecolor="white", edgecolor="white")

# Agregar el título
ax1.set_title(
    "Predicción del Tamaño del Mercado y la Tasa de Crecimiento de la SaaS de Marketing de Influenciadores Extranjeros de China de 2025 a 2027",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()