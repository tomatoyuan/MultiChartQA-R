import matplotlib.pyplot as plt
import numpy as np

# Datos
fechas = [
    "22 abr", "23 abr", "24 abr", "25 abr", "26 abr", 
    "27 abr", "28 abr", "29 abr", "30 abr", "1 may", 
    "2 may", "3 may", "4 may", "5 may"
]
valores_2024 = [112.1, 118.4, 102.0, 119.4, 91.9, 119.5, 122.3, 130.0, 132.0, 66.7, 61.7, 58.8, 62.9, 101.1]
valores_2025 = [76.7, 71.7, 68.8, 101.1, 132.1, 120.0, 102.0, 120.4, 88.9, 119.5, 122.3, 130.3, 133.5, 136.2]

color_2024 = "#4dd0e1"
color_2025 = "#a5d6a7"

x = np.arange(len(fechas))

# Crear sub - gráficos superior e inferior
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'hspace': 0.3})

# Trazar el gráfico de línea para 2024
ax1.plot(x, valores_2024, color=color_2024, marker='o', linewidth=2, label="2024")
for i, val in enumerate(valores_2024):
    ax1.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2024)

ax1.set_title("Tendencia de inversión en publicidad en 2024", fontsize=12, fontweight="bold", color=color_2024)
ax1.set_ylabel("Índice de publicidad", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.2)

# Trazar el gráfico de línea para 2025
ax2.plot(x, valores_2025, color=color_2025, marker='o', linewidth=2, label="2025")
for i, val in enumerate(valores_2025):
    ax2.text(i, val + 2, f"{val}", ha="center", fontsize=9, color=color_2025)

ax2.set_title("Tendencia de inversión en publicidad en 2025", fontsize=12, fontweight="bold", color=color_2025)
ax2.set_ylabel("Índice de publicidad", fontsize=11)
ax2.set_xticks(x)
ax2.set_xticklabels(fechas, rotation=45, ha="right")
ax2.grid(True, linestyle="--", alpha=0.2)

# Título general
fig.suptitle(
    "Comparación de AdTracker de las tendencias de inversión en publicidad en parques/parques de atracciones\ndel 22 de abril al 5 de mayo de 2024 y 2025",
    fontsize=14, fontweight="bold", y=1.03
)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()