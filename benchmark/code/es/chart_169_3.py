import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# Datos
generaciones = ['Post - 2005', 'Post - 2000', 'Post - 1995', 'Post - 1990', 'Post - 1985', 'Post - 1980', 'Antes de 1980']
valores = [105, 73, 115, 115, 110, 80, 80]

# Función para generar gradiente
def rectangulo_gradiente(ax, x, y, ancho, alto, color1, color2, vertical=True):
    cmap = LinearSegmentedColormap.from_list("gradiente_personalizado", [color1, color2])
    n = 100
    for i in range(n):
        if vertical:
            yi = y + i * alto / n
            hi = alto / n
            rect = Rectangle((x, yi), ancho, hi, color=cmap(i / n), linewidth=0)
        else:
            xi = x + i * ancho / n
            wi = ancho / n
            rect = Rectangle((xi, y), wi, alto, color=cmap(i / n), linewidth=0)
        ax.add_patch(rect)

# Crear la gráfica
fig, ax = plt.subplots(figsize=(12, 6))
ancho_barra = 0.5
x = np.arange(len(generaciones))

# Dibujar el gráfico de barras con gradiente
for i, val in enumerate(valores):
    if val >= 100:
        rectangulo_gradiente(ax, x[i] - ancho_barra / 2, 100, ancho_barra, val - 100, '#f99bc5', '#c7008d', vertical=True)
    else:
        rectangulo_gradiente(ax, x[i] - ancho_barra / 2, val, ancho_barra, 100 - val, '#fddde6', '#fdaecf', vertical=True)

# Agregar línea auxiliar y texto
ax.axhline(100, color='gray', linestyle='--')
for i, v in enumerate(valores):
    va = -10 if v < 100 else 5
    ax.text(x[i], v + va, str(v), color='black', ha='center', va='bottom' if v < 100 else 'top', fontsize=12)

# Configurar etiquetas de los ejes
ax.set_xticks(x)
ax.set_xticklabels(generaciones, fontsize=12)
ax.set_ylabel('TGI')
ax.set_ylim(60, 130)
ax.set_title('Encuesta de atención de las mujeres de diferentes generaciones hacia la salud oral\n(TGI>100 indica alta atención)', fontsize=14)

# Mostrar la gráfica
plt.tight_layout()
plt.show()