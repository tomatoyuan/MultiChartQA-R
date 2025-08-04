import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2020", "2021", "2022e", "2023e", "2024e", "2025e"]
# Tamaño total del mercado de servicios en la nube (en miles de millones de yuanes)
market_size = [2256, 3280, 4769, 6812, 9550, 12683]
# Tasa de crecimiento del mercado total de servicios en la nube (%)
growth_rate = [39.9, 45.4, 42.8, 40.2, 32.8, 30.6]

# Crear un lienzo y subgráficos con un eje y doble
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 26000)
ax2.set_ylim(0, 55)

# Dibujar un gráfico de barras del tamaño total del mercado de servicios en la nube
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="Tamaño total del mercado de servicios en la nube (en miles de millones de yuanes)")

# Dibujar un gráfico de línea de la tasa de crecimiento del mercado total de servicios en la nube
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="Tasa de crecimiento del mercado total de servicios en la nube (%)", linewidth=2)

# Añadir etiquetas de datos para el tamaño del mercado
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Ajustar la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom')

# Añadir etiquetas de datos para la tasa de crecimiento
for x_val, y_val in zip(x, growth_rate):
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
ax1.set_ylabel("Tamaño total del mercado de servicios en la nube (en miles de millones de yuanes)", color="#A4C639")
ax2.set_ylabel("Tasa de crecimiento del mercado total de servicios en la nube (%)", color="#64B5F6")
# Establecer el título
ax1.set_title("Consenso en la nube: Tamaño y tasa de crecimiento del mercado total de servicios en la nube de China de 2020 a 2025", fontsize=14, fontweight="bold")

# Combinar las leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Hacer más bonito el gráfico ocultando los bordes superior y derecho (para ax1 y ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()