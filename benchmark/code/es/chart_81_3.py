import matplotlib.pyplot as plt
import numpy as np

# Países/Regiones
paises = ["Japón", "EE. UU.", "China"]
# Área per cápita de bienes raíces logísticas (metros cuadrados por persona), los datos pueden ser aproximadamente los mismos
area = [4.0, 3.7, 0.7]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras
x = np.arange(len(paises))
ancho_barra = 0.6
barras = ax.bar(x, area, width=ancho_barra, color="#C63982", label="Área per cápita de bienes raíces logísticas (m²/persona)")

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
ax.set_xticklabels(paises)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("Comparación del área per cápita de bienes raíces logísticas modernas en China, EE. UU. y Japón en 2019", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='center right')

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()