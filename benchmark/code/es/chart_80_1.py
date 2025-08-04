import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e"]
# Tamaño del mercado (en miles de millones de yuanes), los datos pueden ser aproximadamente los mismos
market_size = [352, 481, 549, 555, 499, 486, 530, 555, 628]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#C63982", label="Tamaño del mercado (en miles de millones de yuanes)")

# Agregar etiquetas de datos
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Tamaño del mercado (en miles de millones de yuanes)")
# Establecer el título
ax.set_title("Tamaño y pronóstico del mercado de pañales para bebés chinos desde 2015 hasta 2023", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()