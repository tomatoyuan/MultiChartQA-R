import matplotlib.pyplot as plt
import numpy as np

# Gráfico 1: Frecuencia de cocinar en casa - Gráfico de barras horizontales + Degradado de color
etiquetas = ["Cocinar en casa \n"
             "todos los días de la\n"
             " semana laboral",
             "Cocinar en casa \n"
             "no más de 3 días \n"
             "a la semana",
             "Incluso no se \n"
             "puede garantizar\n"
             " una vez"]
valores = [38, 37, 5]

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.barh(np.arange(len(etiquetas)), valores, height=0.6,
                 color=["limegreen", "mediumseagreen", "turquoise"],
                 edgecolor='black')

# Agregar anotaciones de valores
for i, barra in enumerate(barras):
    ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height() / 2,
            f"{valores[i]}%", va='center', fontsize=12, color='black')

# Configurar el eje y
ax.set_yticks(np.arange(len(etiquetas)))
ax.set_yticklabels(etiquetas, fontsize=12)
ax.invert_yaxis()  # El valor más alto arriba

# Título del gráfico y fuente
ax.set_title("Frecuencia de cocinar en casa", fontsize=14, fontweight='bold')
plt.text(0, -0.8, "Fuente de datos: CBNData", fontsize=10)

# Eliminar líneas adicionales
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

fig.tight_layout()
plt.show()