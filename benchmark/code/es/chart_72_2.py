import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# Precios minoristas de la leche en polvo para bebés doméstica (yuan/jin), los datos pueden ser aproximadamente los mismos
domestic_prices = [166.3, 171.9, 179.8, 189.5, 204.3, 211.6]
# Precios minoristas de la leche en polvo para bebés internacional (yuan/jin), los datos pueden ser aproximadamente los mismos
international_prices = [214.3, 220.7, 228.0, 235.5, 250.5, 257.8]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Trazar el gráfico de línea de los precios de la marca doméstica
domestic_line, = ax.plot(years, domestic_prices, marker='o', color="#A4C639", label="Leche en polvo para bebés doméstica (yuan/jin)", linewidth=2)
# Trazar el gráfico de línea de los precios de la marca internacional
international_line, = ax.plot(years, international_prices, marker='o', color="#64B5F6", label="Leche en polvo para bebés internacional (yuan/jin)", linewidth=2)

# Agregar etiquetas de datos para las marcas domésticas
for x, y in zip(years, domestic_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Agregar etiquetas de datos para las marcas internacionales
for x, y in zip(years, international_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# Establecer la etiqueta del eje y
ax.set_ylabel("Precio minorista (yuan/jin)")
# Establecer el título
ax.set_title("Tendencia de los precios minoristas de la leche en polvo para bebés en China desde 2016 hasta 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()