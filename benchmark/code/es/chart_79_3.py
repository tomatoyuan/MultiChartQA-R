import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Bubalina", "Arándano", "Mora azul", "Fruto de arándano", "Frutos silvestres"]
# Capacidad antioxidante (contenido de VE mg/100g), los datos pueden ser aproximadamente iguales
capacidad_antioxidante = [1.52, 0.91, 0.45, 0.33, 0.27]

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(6, 5))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, capacidad_antioxidante, width=ancho_barra, color="#399CC6", label="Capacidad antioxidante (contenido de VE mg/100g)")

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Establecer la etiqueta del eje y
ax.set_ylabel("Capacidad antioxidante (contenido de VE mg/100g)")
# Establecer el título
ax.set_title("Capacidad antioxidante de la bubalina", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embellir el gráfico, ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()