import matplotlib.pyplot as plt
import numpy as np

# Categorías de frecuencia de compra
categorias = ["Dentro de medio año", "De medio año a un año", "De un año a dos años", "Más de dos años"]
# Datos de proporción correspondientes (simulados, se pueden ajustar según la situación real)
proporciones = [24.4, 49.7, 23.6, 3.3]
# Proporción total (Dentro de medio año + De medio año a un año)
proporcion_total = sum(proporciones[:2])

# Crear un lienzo y subgráfico
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, proporciones, width=ancho_barra, color="#A4C639")

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Agregar la etiqueta de la proporción total (simular un cuadro discontinuo azul y texto)
ax.text(1, proporcion_total + 3, f'Total {proporcion_total}%',
        ha='center', va='bottom', color='lightblue', fontweight='bold')
# Dibujar un cuadro discontinuo azul (simular el rango)
x_min = x[0] - ancho_barra/2
x_max = x[1] + ancho_barra/2
y_min = 0
y_max = proporcion_total + 5
ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min],
        linestyle='--', color='lightblue', linewidth=1)

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("Frecuencia promedio de compra de productos de tazas y hervidores de alta gama por parte de los consumidores en los últimos 3 años", fontsize=14, fontweight="bold")

# Embellir el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()