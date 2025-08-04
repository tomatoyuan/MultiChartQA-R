import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022.7"]
# Número total de financiaciones (veces)
total_financing = [10, 11, 12, 12, 14, 6, 9]
# Número de financiaciones por encima de 100 millones de yuanes (veces)
billion_financing = [2, 3, 2, 3, 3, 3, 2]

# Ancho de las barras
bar_width = 0.35
# Configuración de colores, similares al verde y azul de la figura original
colors = ["#49C639", "#F664D9"]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar el gráfico de barras para el número total de financiaciones
x = np.arange(len(years))
total_bars = ax.bar(x - bar_width/2, total_financing, width=bar_width, color=colors[0], label="Número total de financiaciones (veces)")
# Dibujar el gráfico de barras para el número de financiaciones por encima de 100 millones de yuanes
billion_bars = ax.bar(x + bar_width/2, billion_financing, width=bar_width, color=colors[1], label="Número de financiaciones por encima de 100 millones de yuanes (veces)")

# Agregar etiquetas de datos para el número total de financiaciones
for bar in total_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos para el número de financiaciones por encima de 100 millones de yuanes
for bar in billion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Número de financiaciones (veces)")
# Establecer el título
ax.set_title("Número de eventos de financiación de bajo código en China desde 2016 hasta julio de 2022", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico ocultando los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()