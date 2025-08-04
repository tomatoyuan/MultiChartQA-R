import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
años = ["2006-2016", "2017", "2018", "2019", "2020", "2021", "Total"]
x = np.arange(len(años))
cantidades = [6, 7, 18, 40, 47, 76, 194]

# Preparar datos de escalón para el gráfico de escalón
x_escalon = np.repeat(x, 2)[1:]
y_escalon = np.repeat(cantidades, 2)[:-1]

# Esquema de colores (esquema de gradiente)
color_llenado = "#b2dfdb"      # Color principal del área rellena
color_linea = "#00796b"      # Color de la curva
color_punto = "#009688"     # Color del punto de marcación

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- Dibujar el gráfico de área de escalón --------------------
ax.step(x, cantidades, where='mid', color=color_linea, linewidth=2.5, label="Número anual de estaciones de reabastecimiento de hidrógeno construidas")
ax.fill_between(x_escalon, y_escalon, step='pre', alpha=0.3, color=color_llenado)

# -------------------- Agregar puntos de datos y anotaciones --------------------
ax.plot(x, cantidades, "o", color=color_punto)

for i, val in enumerate(cantidades):
    ax.text(
        x[i], val + 5,
        str(val),
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=color_punto
    )

# -------------------- Ejes y etiquetas --------------------
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11, color="#424242")
ax.set_ylabel("Número de estaciones de reabastecimiento\n de hidrógeno en China (unidades)", fontsize=11)
ax.set_ylim(0, max(cantidades) + 30)

# -------------------- Leyenda y título --------------------
ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="white")
ax.set_title("Número de estaciones de reabastecimiento de hidrógeno construidas en China de 2006 a 2021", fontsize=14, fontweight='bold', pad=20)

# -------------------- Embelezar --------------------
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()