import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = [2022, 2023, 2024, 2025, 2026, 2027]

# Proporción de varios mercados (%)
juegos_móviles_eb = [51.9, 53.7, 54.5, 54.6, 54.3, 53.9]    # Proporción de juegos de deportes electrónicos móviles
juegos_pc_eb = [23.7, 23.6, 23.2, 22.7, 22.2, 21.6]  # Proporción de juegos de deportes electrónicos de PC
ecosistema_eb = [24.4, 22.7, 22.3, 22.7, 23.5, 24.5]   # Proporción del ecosistema de deportes electrónicos

# Configuración de colores (similar al esquema de colores de la imagen original)
colores = ["#a5d6a7", "#81c784", "#4dd0e1"]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Dibujar el gráfico de barras apiladas --------------------
# Proporción de juegos de deportes electrónicos móviles (capa inferior)
ax.bar(
    años, 
    juegos_móviles_eb, 
    color=colores[0], 
    label="Proporción de juegos de deportes electrónicos móviles (%)",
    edgecolor="white",
    linewidth=1
)

# Proporción de juegos de deportes electrónicos de PC (capa intermedia)
base_móvil = np.array(juegos_móviles_eb)
ax.bar(
    años, 
    juegos_pc_eb, 
    bottom=base_móvil, 
    color=colores[1], 
    label="Proporción de juegos de deportes electrónicos de PC (%)",
    edgecolor="white",
    linewidth=1
)

# Proporción del ecosistema de deportes electrónicos (capa superior)
base_torneo = base_móvil + np.array(juegos_pc_eb)
ax.bar(
    años, 
    ecosistema_eb, 
    bottom=base_torneo, 
    color=colores[2], 
    label="Proporción del ecosistema de deportes electrónicos (%)",
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar etiquetas de datos --------------------
for i, (a, m, t, e) in enumerate(zip(años, juegos_móviles_eb, juegos_pc_eb, ecosistema_eb)):
    # Proporción de deportes electrónicos móviles
    ax.text(a, m/2, f"{m}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # Proporción de deportes electrónicos de PC
    ax.text(a, m + t/2, f"{t}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    # Proporción del ecosistema de deportes electrónicos
    ax.text(a, m + t + e/2, f"{e}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")

# -------------------- Embellir el gráfico --------------------
# Establecer el rango del eje y (la proporción total es 100%)
ax.set_ylim(0, 100)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar una leyenda y moverla hacia arriba
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white",
    # Usar bbox_to_anchor para ajustar finamente la posición, el rango de (x, y) es [0, 1]
    bbox_to_anchor=(0.1, 0.2)  # Mover hacia arriba, y > 1 significa arriba del gráfico
)

# Agregar un título
ax.set_title(
    "Proporción de la escala segmentada del mercado de deportes electrónicos chino de 2022 a 2027",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño (para evitar que la leyenda se recorte)
plt.tight_layout()

# Si la posición de la leyenda excede el rango del gráfico, se puede ajustar el rango guardado a través de bbox_inches (opcional)
# plt.savefig("output.png", bbox_inches="tight")

plt.show()