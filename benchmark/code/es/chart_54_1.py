import matplotlib.pyplot as plt
import numpy as np

# Definición de datos (correspondiente a la estructura de la imagen original, los valores se pueden ajustar)
años = ["2018", "2019", "2020", "2021", "2022", "2023"]
ingresos = [28228, 30733, 32189, 35128, 36883, 39218]  # Datos simulados, se pueden reemplazar con valores reales

# Configuración de color (cercano al esquema de color verde de la imagen original)
color_barra = "#81c784"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras
x = np.arange(len(años))
barras = ax.bar(x, ingresos, color=color_barra, width=0.6, edgecolor="white", linewidth=1)

# Agregar anotaciones numéricas
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 500,  # Desplazamiento hacia arriba para evitar la superposición
        f"{altura}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Embellir el gráfico
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=12, color="#424242")
ax.set_ylabel("Ingreso disponible per cápita (yuan)", fontsize=12, color="#424242")

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar un título
ax.set_title(
    "Ingreso disponible per cápita nacional (yuan) desde 2018 hasta 2023",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()