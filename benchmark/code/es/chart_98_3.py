import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021"]
# Datos de costos de baterías (yuan), [Costo de batería de iones de litio, Costo de batería de plomo-ácido]
battery_costs = np.array([[1800, 400], [1400, 400], [1300, 400], [1150, 400], [1050, 400]])

# Colores personalizados (ajustables), correspondientes a la batería de iones de litio y la batería de plomo-ácido respectivamente
colors = ["#6839C6", "#87CEEB"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras agrupadas, posiciones del eje x
x = np.arange(len(years))
# Ancho de las barras
width = 0.35

# Dibujar el gráfico de barras para los costos de las baterías de iones de litio
li_ion_bars = ax.bar(x - width/2, battery_costs[:, 0], width, color=colors[0], label="Batería de iones de litio (Yuan)")
# Dibujar el gráfico de barras para los costos de las baterías de plomo-ácido
lead_acid_bars = ax.bar(x + width/2, battery_costs[:, 1], width, color=colors[1], label="Batería de plomo-ácido (Yuan)")

# Agregar etiquetas de costo para las baterías de iones de litio
for bar in li_ion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Agregar etiquetas de costo para las baterías de plomo-ácido
for bar in lead_acid_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer el título
ax.set_title("Costos de baterías de vehículos eléctricos de dos ruedas chinos desde 2017 hasta 2021", fontsize=14, fontweight="bold")
# Agregar una leyenda
ax.legend()

# Embellecimiento: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()