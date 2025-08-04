import matplotlib.pyplot as plt
from matplotlib.patches import Arc, PathPatch, Path, Rectangle, Circle
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Definir la función para dibujar la forma de una nube (versión mejorada)
def draw_cloud(ax, x, y, scale=1, color='#ffffff', edge_color='#a8d5ff', shadow=True):
    """Dibujar la forma de una nube con efecto tridimensional"""
    # Nube principal
    verts = [
        (0, 0), (1, 0), (2, 1), (3, 0), (4, 0),
        (4, 1), (3, 2), (2, 1), (1, 2), (0, 1),
        (0, 0)
    ]
    verts = np.array(verts) * scale + [x, y]
    path = Path(verts)

    # Agregar efecto de sombra
    if shadow:
        shadow_verts = verts + [0.1, -0.1]
        shadow_path = Path(shadow_verts)
        shadow_patch = PathPatch(shadow_path, facecolor='black', alpha=0.2)
        ax.add_patch(shadow_patch)

    patch = PathPatch(path, facecolor=color, edgecolor=edge_color, linewidth=1.5, alpha=0.9)
    ax.add_artist(patch)

    # Agregar brillo
    highlight_verts = [
        (1, 0.5), (2, 1.5), (1.5, 1.8), (0.5, 1), (1, 0.5)
    ]
    highlight_verts = np.array(highlight_verts) * scale * 0.6 + [x, y]
    highlight_path = Path(highlight_verts)
    highlight_patch = PathPatch(highlight_path, facecolor='white', alpha=0.6)
    ax.add_artist(highlight_patch)

    return patch

# Definir la función para dibujar la forma de una gota de lluvia (versión mejorada)
def draw_rain(ax, x, y, num_drops=3, scale=1, color='#64b5f6'):
    """Dibujar gotas de lluvia con efecto de degradado"""
    drop_verts = [(-0.2, 0), (0.2, 0), (0, -1)]
    drop_verts = np.array(drop_verts) * scale

    for i in range(num_drops):
        dx = (i - (num_drops - 1) / 2) * 0.5
        drop_path = Path(drop_verts + [x + dx, y - 0.5])

        # Crear efecto de degradado
        drop_patch = PathPatch(drop_path, facecolor=color, alpha=0.8)
        ax.add_artist(drop_patch)

        # Agregar brillo a la gota de lluvia
        highlight_verts = [(-0.05, -0.2), (0.05, -0.2), (0, -0.5)]
        highlight_verts = np.array(highlight_verts) * scale
        highlight_path = Path(highlight_verts + [x + dx, y - 0.5])
        highlight_patch = PathPatch(highlight_path, facecolor='white', alpha=0.6)
        ax.add_artist(highlight_patch)

# Definir la función para dibujar el efecto del arcoíris
def draw_rainbow(ax, x, y, width, height):
    """Dibujar el efecto del arcoíris de fondo"""
    colors = ['#ff6b6b', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
    for i, color in enumerate(colors):
        arc = Arc((x, y), width - i * 0.3, height - i * 0.3,
                  theta1=0, theta2=180, color=color, alpha=0.1)
        ax.add_artist(arc)

# Crear el lienzo y agregar el fondo degradado
fig, ax = plt.subplots(figsize=(9, 10))  # Aumentar ligeramente el ancho del lienzo
ax.set_xlim(0, 9)  # Ajustar el rango del eje x
ax.set_ylim(0, 10)
ax.axis('off')

# Crear el fondo degradado
x = np.linspace(0, 9, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = Y

cmap = LinearSegmentedColormap.from_list('sky_gradient', ['#e6f2ff', '#b3d9ff', '#80bfff'])
im = ax.imshow(Z, cmap=cmap, extent=[0, 9, 0, 10], alpha=0.8, aspect='auto')

# Agregar el arcoíris de fondo
draw_rainbow(ax, 4.5, -2, 11, 8)  # Ajustar la posición del arcoíris para adaptarse al nuevo lienzo

# Dibujar nubes decorativas pequeñas
for i in range(5):
    x_pos = np.random.uniform(0.5, 8.5)  # Adaptarse al nuevo rango del eje x
    y_pos = np.random.uniform(7, 9.5)
    draw_cloud(ax, x_pos, y_pos, scale=0.2, color='#f0f8ff', shadow=False)

# Dibujar el área del título (aumentar立体感)
title_rect_bg = Rectangle((1.75, 8.85), 6.5, 0.7, facecolor='black', alpha=0.2)  # Aumentar el ancho del fondo del título
ax.add_artist(title_rect_bg)
title_rect = Rectangle((1.8, 8.9), 6.4, 0.6, facecolor='#ffd166', edgecolor='white', linewidth=2)  # Aumentar el ancho del marco del título
ax.add_artist(title_rect)
ax.text(5, 9.2, 'Clasificación de las provincias por la atención de búsqueda de tormentas', 
        fontsize=16, color='#073b4c',  # Disminuir el tamaño de la fuente
        ha='center', va='center', fontweight='bold')

# Dibujar los títulos de los dos períodos de tiempo (agregar esquinas redondeadas y立体感)
def draw_fancy_rect(ax, x, y, width, height, color, text, font_size=10):
    """Dibujar un título rectangular con esquinas redondeadas y立体感"""
    rect_bg = Rectangle((x - 0.05, y - 0.05), width + 0.1, height + 0.1,
                        facecolor='black', alpha=0.2, edgecolor='none')
    ax.add_artist(rect_bg)

    rect = Rectangle((x, y), width, height, facecolor=color,
                     edgecolor='white', linewidth=1, alpha=0.9)
    ax.add_artist(rect)

    ax.text(x + width / 2, y + height / 2, text, fontsize=font_size,
            color='white', ha='center', va='center', fontweight='bold')

draw_fancy_rect(ax, 2.2, 8.0, 2, 0.4, '#0077b6', '1 - 7 de julio')
draw_fancy_rect(ax, 5.3, 8.0, 2, 0.4, '#0077b6', '20 de julio')  # Ajustar la posición

# Dibujar la línea de separación
divider = plt.Line2D([0, 9], [3.5, 3.5], color='#003e7e', alpha=0.2, linewidth=2)  # Adaptarse al nuevo eje x
ax.add_artist(divider)

# Dibujar las nubes de las provincias del 1 - 7 de julio (agregar colores degradados)
period1_provinces = ['Hubei', 'Shandong', 'Jiangsu', 'Anhui', 'Henan']
period1_colors = ['#ff6b6b', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
y_pos1 = np.linspace(7.2, 4.2, 5)

for i, (prov, color) in enumerate(zip(period1_provinces, period1_colors)):
    draw_cloud(ax, 3, y_pos1[i], scale=0.5, color='#ffffff', edge_color=color)
    # Agregar el fondo del nombre de la provincia
    name_bg = Rectangle((2.7, y_pos1[i] + 0.15), 0.6, 0.3, facecolor=color, alpha=0.7, edgecolor='none')
    ax.add_artist(name_bg)
    ax.text(3, y_pos1[i] + 0.3, prov, fontsize=12, color='white',
            ha='center', va='center', fontweight='bold')

# Dibujar las nubes de las provincias del 20 de julio (agregar colores degradados)
period2_provinces = ['Shandong', 'Beijing', 'Hebei', 'Henan', 'Shanxi']
period2_colors = ['#ff6b6b', '#ef476f', '#ffd166', '#06d6a0', '#118ab2']
y_pos2 = np.linspace(7.2, 4.2, 5)

for i, (prov, color) in enumerate(zip(period2_provinces, period2_colors)):
    draw_cloud(ax, 6.5, y_pos2[i], scale=0.5, color='#ffffff', edge_color=color)  # Ajustar la posición x
    # Agregar el fondo del nombre de la provincia
    name_bg = Rectangle((6.2, y_pos2[i] + 0.15), 0.6, 0.3, facecolor=color, alpha=0.7, edgecolor='none')  # Ajustar la posición
    ax.add_artist(name_bg)
    ax.text(6.5, y_pos2[i] + 0.3, prov, fontsize=12, color='white',  # Ajustar la posición
            ha='center', va='center', fontweight='bold')

# Dibujar el título "provincias menos preocupadas por las tormentas"
draw_fancy_rect(ax, 1, 2.5, 3, 0.4, '#6c757d', 'Provincias menos preocupadas por las tormentas', font_size=9)  # Aumentar el ancho y disminuir el tamaño de la fuente

# Dibujar las provincias menos preocupadas (con gotas de lluvia)
least_provinces = [('Xinjiang', 2, 1.5, 3), ('Ningxia', 3.7, 1.8, 3),
                   ('Guangdong', 5.3, 1.8, 3), ('Inner Mongolia', 7, 1.5, 3), ('Qinghai', 8.5, 1.2, 3)]  # Ajustar la posición para adaptarse al nuevo lienzo

for i, (prov, x, y, drops) in enumerate(least_provinces):
    draw_cloud(ax, x, y, scale=0.35, color='#f8f9fa', edge_color='#6c757d')
    # Agregar el nombre de la provincia
    ax.text(x, y + 0.15, prov, fontsize=9, color='#073b4c',  # Disminuir el tamaño de la fuente
            ha='center', va='center', fontweight='bold')
    # Agregar gotas de lluvia
    draw_rain(ax, x, y - 0.3, num_drops=drops, scale=0.3, color='#64b5f6')

# Agregar gotas de lluvia decorativas de fondo
for _ in range(50):
    x_pos = np.random.uniform(0, 9)  # Adaptarse al nuevo eje x
    y_pos = np.random.uniform(0, 10)
    draw_rain(ax, x_pos, y_pos, num_drops=1, scale=0.15, color='#90caf9')

plt.tight_layout()
plt.show()