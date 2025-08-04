import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
años = ["2019", "2020", "2021"]
x = np.arange(len(años))
escala_consumo = [100, 200, 300]

# Interpolar los datos en una curva suave (preparación para el ajuste del gráfico de área)
x_suave = np.linspace(x.min(), x.max(), 300)
y_suave = np.interp(x_suave, x, escala_consumo)

# -------------------- Crear el Canvas --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- Dibujar el Gráfico de Área --------------------
ax.plot(x, escala_consumo, marker='o', color="#4dd0e1", linewidth=3, label="Escala de Consumo")
ax.fill_between(x_suave, np.interp(x_suave, x, escala_consumo), color="#b2ebf2", alpha=0.6)

# -------------------- Agregar Anotaciones de Datos --------------------
for i, val in enumerate(escala_consumo):
    ax.text(
        x[i], val + 10,
        f"{val}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight="bold",
        color="#00796b"
    )

# -------------------- Configuración de los Ejes --------------------
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11, color="#424242")

ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# -------------------- Agregar Título y Leyenda --------------------
ax.set_title(
    "Tendencia de la Escala de Consumo de 'Botanas Funcionales' en Tmall Global de 2019 a 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

ax.legend(loc="upper left", fontsize=10, frameon=True, facecolor="white", edgecolor="white")

# -------------------- Diseño y Visualización --------------------
plt.tight_layout()
plt.show()