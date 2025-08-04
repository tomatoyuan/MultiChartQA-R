import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e"]
# Tamaño del mercado (trillones de yuanes)
market_size = [3, 3, 4, 4, 4, 5, 4, 5, 5, 6]
# Tasa de crecimiento interanual (%)
growth_rate = [11.7, 10.8, 10.7, 7.7, 9.4, -15.4, 18.9, 14.2, 12.4]
# División de etapas
stages = ["Período de crecimiento estable"] * 5 + ["Período de recesión"] + ["Período de recuperación"] + ["Período de nueva vitalidad"] * 2
stage_x = [0, 4, 5, 6, 7, 9]  # Límites de las coordenadas X para dibujar los fondos de las etapas, deben coincidir con el número de años. Aquí es un ejemplo simple y se puede refinar.
stage_y = [-0.5] * len(stage_x)
stage_height = [1] * len(stage_x)
stage_colors = ["#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD"]  # Simular colores de las etapas

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras (tamaño del mercado)
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#A4C639", label="Tamaño del mercado de catering en China (trillones de yuanes)")

# Dibujar un gráfico de línea (tasa de crecimiento interanual)
ax2 = ax.twinx()
ax2.plot(x[:-1], growth_rate, marker='o', color="#87CEEB", label="Tasa de crecimiento interanual (%)", linewidth=2)  # Los datos de la tasa de crecimiento son uno menos que los años, prestar atención al corte.

# Agregar anotaciones del tamaño del mercado
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Agregar anotaciones de la tasa de crecimiento
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%',
                 xy=(x[i], rate),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Dibujar fondos de las etapas (simulación simple. Si se necesitan posiciones precisas, se deben refinar las coordenadas.)
for i in range(len(stages)):
    ax.axvspan(i, i + 1, facecolor=stage_colors[i], alpha=0.3)

# Agregar manualmente textos de las etapas (debido a que el diseño automático es complejo, aquí se coloca simplemente y se puede ajustar según la situación real.)
stage_texts = ["Período de crecimiento estable", "Período de recesión", "Período de recuperación", "Período de nueva vitalidad"]
ax.text(1, -0.5, stage_texts[0], ha='center', va='top', fontweight='bold')
ax.text(4.5, -0.5, stage_texts[1], ha='center', va='top', fontweight='bold')
ax.text(6.5, -0.5, stage_texts[2], ha='center', va='top', fontweight='bold')
ax.text(8.3, -0.5, stage_texts[3], ha='center', va='top', fontweight='bold')

# Establecer las marcas del eje X
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer el rango del eje Y (tamaño del mercado)
ax.set_ylim(0, 7)
# Establecer el título
ax.set_title("Tamaño del mercado de catering en China desde 2014 hasta 2023", fontsize=14, fontweight="bold")

# Combinar leyendas
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Embelezar: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()