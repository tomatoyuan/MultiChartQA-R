import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Bubbles de pescado", "Agua de ácido hialurónico"]
# Proporción de contenido de ácido hialurónico (mg/100g), los datos pueden ser aproximadamente iguales
acido_hialuronico = [230.0, 19.8]

# Crear un lienzo y subgráficos
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, acido_hialuronico, width=ancho_barra, color="#C6395C", label="Proporción de contenido de ácido hialurónico (mg/100g)")

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
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("Contenido de ácido hialurónico en bubbles de pescado", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()