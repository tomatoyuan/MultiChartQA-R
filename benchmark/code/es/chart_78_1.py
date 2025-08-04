import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e", "2024e", "2025e", "2026e"]
# Tamaño del mercado global de educación profesional (en miles de millones de dólares estadounidenses), los datos pueden ser aproximadamente los mismos
market_size = [491, 520, 558, 585, 604, 647, 684, 720, 751, 779, 803]
# Tasa de crecimiento interanual del mercado de educación profesional (%), los datos pueden ser aproximadamente los mismos
yoy = [5.8, 7.4, 4.7, 3.4, 7.0, 5.8, 5.2, 4.4, 3.7, 3.1]

# Crear un lienzo y subgráficos con un eje y doble
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 1600)
ax2.set_ylim(-5, 10)

# Dibujar un gráfico de barras del tamaño del mercado global de educación profesional
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="Tamaño del Mercado Global de Educación Profesional (Miles de Millones de USD)")

# Dibujar un gráfico de línea de la tasa de crecimiento interanual del mercado de educación profesional (Nota: Los datos de yoy tienen un valor menos que los años porque no hay datos de comparación de crecimiento para 2016, y aquí se corresponden con los años a partir de 2017)
line_x = x[1:]  # El eje x del gráfico de línea se corresponde con los años de 2017 a 2026e
line, = ax2.plot(line_x, yoy, marker='o', color="#64B5F6", label="Tasa de Crecimiento Interanual del Mercado de Educación Profesional (%)", linewidth=2)

# Agregar etiquetas de datos al gráfico de barras del tamaño del mercado global de educación profesional
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos al gráfico de línea de la tasa de crecimiento interanual del mercado de educación profesional
for x_val, y_val in zip(line_x, yoy):
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
ax1.set_ylabel("Tamaño del Mercado Global de Educación Profesional (Miles de Millones de USD)", color="#A4C639")
ax2.set_ylabel("Tasa de Crecimiento Interanual del Mercado de Educación Profesional (%)", color="#64B5F6")
# Establecer el título
ax1.set_title("Tamaño y Tasa de Crecimiento del Mercado Global de Educación Profesional de 2016 a 2026", fontsize=14, fontweight="bold")

# Combinar las leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Embelezar el gráfico ocultando los bordes superior y derecho (tanto para ax1 como para ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()