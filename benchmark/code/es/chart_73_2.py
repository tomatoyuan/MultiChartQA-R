import matplotlib.pyplot as plt
import numpy as np

# Configuración de datos
categorias = ["5 veces o más al mes", "3 - 4 veces al mes", "1 - 2 veces al mes", "1 - 2 veces por trimestre", "1 - 2 veces al año"]
datos = [8.0, 33.0, 41.5, 14.5, 3.0]
# Los índices de las categorías a enmarcar (correspondientes a "3 - 4 veces al mes", "1 - 2 veces al mes", "1 - 2 veces por trimestre", con índices 1, 2, 3)
indices_enmarcados = [1, 2, 3]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(categorias))
altura_barra = 0.6
barras = ax.barh(y, datos, height=altura_barra, color="#A4C639", edgecolor="white")

# Dibujar un cuadro discontinuo azul
min_y = min(y[i] - altura_barra / 2 for i in indices_enmarcados)
max_y = max(y[i] + altura_barra / 2 for i in indices_enmarcados)
min_x = 0
max_x = max(datos[i] for i in indices_enmarcados)
rect = plt.Rectangle((min_x, min_y), max_x, max_y - min_y, 
                     fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Frecuencia de uso de las plataformas de entrega inmediata más utilizadas por los usuarios", fontsize=14, fontweight="bold")

# Hacer el gráfico más bonito, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  
plt.show()