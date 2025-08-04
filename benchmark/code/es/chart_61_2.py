import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
meses = ["Ene", "Feb", "Mar"]
años = ["2023", "2024", "2025"]

# Datos: [2023, 2024, 2025] (minutos)
datos = np.array([
    [286.5, 267.9, 265.5],  # Ene
    [288.3, 272.6, 267.9],  # Feb
    [300.6, 278.9, 268.0],  # Mar
])

# Mejora del estilo de color
colores = ["#7CB342", "#66BB6A", "#00ACC1"]  # Corresponde a 2023/2024/2025
marcadores = ["o", "s", "D"]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(9, 5.5))

# -------------------- Dibujar múltiples líneas --------------------
x = np.arange(len(meses))
for i in range(len(años)):
    y = datos[:, i]
    ax.plot(
        x, y, marker=marcadores[i], linewidth=2.5, 
        label=años[i], color=colores[i]
    )
    # Agregar etiquetas de datos
    for j, val in enumerate(y):
        ax.text(
            x[j], val + 3,
            f"{val}", ha='center', fontsize=9,
            color=colores[i], fontweight='bold'
        )

# -------------------- Etiquetas de tasa de crecimiento interanual (2024→2025) --------------------
for i in range(len(meses)):
    tasa = datos[i][2] - datos[i][1]
    tasa_pct = round((tasa / datos[i][1]) * 100, 1)
    color = "red" if tasa_pct < 0 else "green"
    ax.text(
        x[i] + 0.05, datos[i][2] + 10,
        f"{tasa_pct:+}%", color=color,
        fontsize=9, ha="left", va="center", fontweight="bold"
    )

# -------------------- Embellecer el gráfico --------------------
ax.set_xticks(x)
ax.set_xticklabels(meses, fontsize=11)
ax.set_ylabel("Tiempo efectivo diario por máquina (minutos)", fontsize=11)
ax.set_title("mUserTracker - Tiempo efectivo diario por máquina en el primer trimestre de 2023 - 2025", fontsize=14, fontweight="bold", pad=15)

# Líneas de cuadrícula
ax.grid(alpha=0.2)

# Leyenda
ax.legend(loc="upper right", fontsize=9, frameon=True)

# Eliminar bordes redundantes
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()