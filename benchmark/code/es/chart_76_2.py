import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# Costo de marketing por usuario activo recién agregado en el período actual (yuan/persona), los datos pueden ser aproximadamente iguales
marketing_cost = [67.6, 100.1, 154.6, 251.6, 435.7, 298.1, 474.8, 572.3]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, marketing_cost, width=bar_width, color="#A4C639", label="Costo de marketing promedio por usuario activo recién agregado \nen el período actual (yuan/persona)")

# Agregar etiquetas de datos
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Simular un borde exterior verde
for spine in ax.spines.values():
    spine.set_color('#A4C639')
    spine.set_linewidth(2)

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Costo de marketing promedio por usuario activo recién agregado \nen el período actual (yuan/persona)")
# Establecer el título
ax.set_title("Costo de marketing por usuario activo recién agregado de las principales empresas de Internet cotizadas de 2014 a 2021", fontsize=12, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='upper left')

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()