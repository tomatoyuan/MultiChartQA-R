import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
años = [2022, 2023, 2024, 2025, 2026, 2027]

# Tamaños de diversos mercados (en miles de millones de yuanes)
mercado_movil_esports = [819, 911, 975, 1020, 1060, 1095]    # Mercado de juegos de e - sports móvil
mercado_pc_esports = [375, 400, 415, 424, 432, 438]  # Mercado de juegos de e - sports de PC
ecosistema_esports = [385, 386, 400, 424, 458, 497]   # Mercado del ecosistema de e - sports

# Tasas de crecimiento general (%)
tasas_crecimiento = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]  # Se calcularán según los datos reales, aquí es un marcador de posición

# Configuración de colores (similar al esquema de colores de la imagen original)
colores = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Dibujar el gráfico de barras apiladas --------------------
# Mercado de juegos de e - sports móvil (capa inferior)
ax.bar(
    años, 
    mercado_movil_esports, 
    color=colores[0], 
    label="Tamaño del mercado de juegos de e - sports móvil (en miles de millones de yuanes)",
    edgecolor="white",
    linewidth=1
)

# Mercado de juegos de e - sports de PC (capa intermedia)
base_movil = np.array(mercado_movil_esports)
ax.bar(
    años, 
    mercado_pc_esports, 
    bottom=base_movil, 
    color=colores[1], 
    label="Tamaño del mercado de juegos de e - sports de PC (en miles de millones de yuanes)",
    edgecolor="white",
    linewidth=1
)

# Mercado del ecosistema de e - sports (capa superior)
base_pc = base_movil + np.array(mercado_pc_esports)
ax.bar(
    años, 
    ecosistema_esports, 
    bottom=base_pc, 
    color=colores[2], 
    label="Tamaño del mercado del ecosistema de e - sports (en miles de millones de yuanes)",
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar anotaciones de datos --------------------
# Anotar valores para cada capa
for i, (a, m, p, e) in enumerate(zip(años, mercado_movil_esports, mercado_pc_esports, ecosistema_esports)):
    # E - sports móvil
    ax.text(a, m/2, f"{m}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # E - sports de PC
    ax.text(a, m + p/2, f"{p}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # Ecosistema de e - sports
    ax.text(a, m + p + e/2, f"{e}", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- Embellir el gráfico --------------------
# Establecer la etiqueta del eje y
ax.set_ylabel("Tamaño del mercado (en miles de millones de yuanes)", fontsize=10, color="#424242")

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar leyenda
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Agregar título
ax.set_title(
    "Tamaño total del mercado de e - sports en China desde 2022 hasta 2027",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()