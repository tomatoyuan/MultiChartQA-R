import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Nombres de los proyectos
items = ["Educación", "Salud", "Bienes de gran valor", "Cultura y entretenimiento social", "Compra de vivienda", "Viajes", "Seguros"]
# Datos correspondientes (proporción)
data = [28.1, 27.4, 18.7, 18.1, 16.9, 15.2, 13.9]
# Configuración de colores, azul para viajes, verde para el resto, similar a la imagen original
colors = ["#A4C639"] * len(items)
colors[items.index("Viajes")] = "#64B5F6"

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(items))
bar_height = 0.6
max_data = max(data)
for i in range(len(items)):
    # Dibujar la barra de fondo (efecto de borde verde)
    rect = Rectangle((0, y[i] - bar_height / 2), max_data, bar_height, facecolor="white", edgecolor="#A4C639", linewidth=1.5)
    ax.add_patch(rect)
    # Dibujar la barra del primer plano
    bar = ax.barh(y[i], data[i], height=bar_height, color=colors[i], edgecolor="white", label=items[i])
    # Agregar etiquetas de datos
    ax.annotate(f'{data[i]}%',
                xy=(data[i], y[i]),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center',
                fontweight='bold')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(items)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Proyectos para aumentar el gasto en los próximos tres meses", fontsize=14, fontweight="bold")

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()