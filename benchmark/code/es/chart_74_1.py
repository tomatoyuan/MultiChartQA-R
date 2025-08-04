import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021e"]
# Escala económica de las "Nuevas Tres" (en miles de millones de yuanes), los datos pueden ser aproximadamente iguales
economic_scale = [113719, 129578, 145369, 161927, 169254, 197170]
# Proporción en el PIB (%), los datos pueden ser aproximadamente iguales
gdp_ratio = [15.3, 15.7, 16.1, 16.3, 17.1, 17.2]

# Crear un lienzo y subgráficos con un eje y doble
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 400000)
ax2.set_ylim(10, 18)

# Dibujar un gráfico de barras de la escala económica de las "Nuevas Tres"
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, economic_scale, width=bar_width, color="#A4C639", label="Escala económica de las \"Nuevas Tres\" (en miles de millones de yuanes)")

# Dibujar un gráfico de línea de la proporción en el PIB
line, = ax2.plot(x, gdp_ratio, marker='o', color="#64B5F6", label="Proporción en el PIB (%)", linewidth=2)

# Agregar etiquetas de datos para la escala económica de las "Nuevas Tres"
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Ajustar la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom')

# Agregar etiquetas de datos para la proporción en el PIB
for x_val, y_val in zip(x, gdp_ratio):
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
ax1.set_ylabel("Escala económica de las \"Nuevas Tres\" (en miles de millones de yuanes)", color="#A4C639")
ax2.set_ylabel("Proporción en el PIB (%)", color="#64B5F6")
# Establecer el título
ax1.set_title("Escala de la nueva economía de China y proporción en el PIB de 2016 a 2021", fontsize=14, fontweight="bold")

# Combinar las leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Embellir el gráfico ocultando los bordes superior y derecho (para ax1 y ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()