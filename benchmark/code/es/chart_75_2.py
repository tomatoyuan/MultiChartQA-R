import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021"]
# Producción de granos de café verde de la provincia de Yunnan (en 10,000 toneladas), los datos pueden ser aproximadamente los mismos
production = [16.5, 15.1, 14.5, 13.5, 14.0]
# Tasa de crecimiento de la producción (%), los datos pueden ser aproximadamente los mismos
growth_rate = [-8.2, -4.1, -6.8, 3.8]

# Crear un lienzo y subgráficos con un eje y dual
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 32)
ax2.set_ylim(-40, 20)

# Dibujar un gráfico de barras de la producción de granos de café verde
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, production, width=bar_width, color="#A4C639", label="Producción de granos de café verde de la provincia de Yunnan (10,000 toneladas)")

# Dibujar un gráfico de línea de la tasa de crecimiento de la producción (Nota: Hay un punto de datos de tasa de crecimiento menos que el número de años porque no hay datos de comparación de tasa de crecimiento para 2017, por lo que comienza a corresponderse a partir de 2018)
line_x = x[1:]  # El eje x del gráfico de línea corresponde a los años de 2018 a 2021
line, = ax2.plot(line_x, growth_rate, marker='o', color="#64B5F6", label="Tasa de crecimiento de la producción de granos de café verde de la provincia de Yunnan (%)", linewidth=2)

# Agregar etiquetas de datos de producción
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Ajustar la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom')

# Agregar etiquetas de datos de tasa de crecimiento
for x_val, y_val in zip(line_x, growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Ajustar la posición de la etiqueta
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#64B5F6")

# Establecer las marcas y etiquetas del eje x
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Establecer las etiquetas del eje y
ax1.set_ylabel("Producción de granos de café verde de la provincia de Yunnan (10,000 toneladas)", color="#A4C639")
ax2.set_ylabel("Tasa de crecimiento de la producción de granos de café verde de la provincia de Yunnan (%)", color="#64B5F6")
# Establecer el título
ax1.set_title("Producción de granos de café verde de la provincia de Yunnan en China de 2017 a 2021", fontsize=14, fontweight="bold")

# Combinar leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Embellir el gráfico, ocultar los bordes superior y derecho (para ax1 y ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()