import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Años
years = ["2020", "2030e", "2040e", "2050e", "2060e"]
# Demanda de energía de hidrógeno (10,000 toneladas), los datos son consistentes con el gráfico
demand = [3342, 3715, 5276, 9690, 13030]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, demand, width=bar_width, color="#C6395A")

# Agregar etiquetas de datos
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Demanda de energía de hidrógeno en China (10,000 toneladas)")
# Establecer el título
ax.set_title("Demanda de energía de hidrógeno en China de 2020 a 2060", fontsize=14, fontweight="bold")

# Embellir el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()