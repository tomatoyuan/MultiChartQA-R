import matplotlib.pyplot as plt
import numpy as np

# Configuración de datos
categorias = ["Más de 3 años", "2 - 3 años (incluido)", "1 - 2 años (incluido)", "6 - 12 meses (incluido)", "3 - 6 meses (incluido)", "1 - 3 meses (incluido)", "≤ 1 mes (incluido)"]
datos = [8.4, 12.5, 30.7, 22.9, 11.6, 6.5, 7.4]
# Índices de las categorías a encerrar en un cuadro (correspondientes a "Más de 3 años", "2 - 3 años (incluido)", "1 - 2 años (incluido)", con índices 0, 1, 2)
indices_encuadrar = [0, 1, 2]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(categorias))
altura_barra = 0.6
barras = ax.barh(y, datos, height=altura_barra, color="#A4C639", edgecolor="white")

# Dibujar un cuadro discontinuo azul
min_y = min(y[i] - altura_barra / 2 for i in indices_encuadrar)
max_y = max(y[i] + altura_barra / 2 for i in indices_encuadrar)
min_x = 0
max_x = max(datos[i] for i in indices_encuadrar)
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
ax.set_title("Tiempo acumulado de uso de las plataformas habituales de los usuarios", fontsize=14, fontweight="bold")

# Emprolijar el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  
plt.show()