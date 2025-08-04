import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# Etiquetas y datos (correspondientes a la versión de los chicos de la lógica de desprecio: Intuitividad - Tasa de uso masculino)
labels = [
    "Emoticonos de texto", "Emoticonos de ancianos", "Emoticonos de celebridades",
    "Emoji", "Emoticonos integrados de QQ/WeChat", "Emoticonos de cómic"
]
values = [28, 31, 45, 64, 67, 72]

# Generar un esquema de colores degradados
def get_gradient_colors(base_color, num_layers, lightness_range=(0.6, 1.0)):
    """Generar un degradado de oscuro a claro"""
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.colors as mcolors

    # Convertir color hexadecimal a RGB
    rgb = mcolors.hex2color(base_color)

    # Crear un mapa de colores degradado
    cmap = LinearSegmentedColormap.from_list(
        f'custom_{base_color}',
        [(rgb[0]*lightness_range[0], rgb[1]*lightness_range[0], rgb[2]*lightness_range[0]),
         (rgb[0]*lightness_range[1], rgb[1]*lightness_range[1], rgb[2]*lightness_range[1])]
    )

    return [cmap(i/num_layers) for i in range(num_layers)]

# Usar el esquema de color verde como base
base_color = '#2c6f66'
colors = get_gradient_colors(base_color, len(labels))

# Parámetros del gráfico
num_layers = len(labels)
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Coordenadas del vértice inferior
bottom_x = 0.5
bottom_y = 0.05

# Ancho superior (el lado superior del triángulo invertido completo)
top_left = (0.1, 0.95)
top_right = (0.9, 0.95)

# Altura de cada capa (dividida uniformemente)
layer_height = (top_left[1] - bottom_y) / num_layers

# Dibujar el degradado de fondo
gradient_bg = np.zeros((100, 100, 3))
for i in range(100):
    for j in range(100):
        y_norm = i / 100
        # El color de fondo cambia de verde claro a verde aún más claro
        gradient_bg[i, j] = [0.95 - y_norm*0.1, 0.98 - y_norm*0.1, 0.95 - y_norm*0.05]
ax.imshow(gradient_bg, extent=[0, 1, 0, 1], aspect='auto', zorder=0)

# Agregar efecto de sombra
shadow_offset = 0.015
for i in range(num_layers):
    # Coordenadas y superiores e inferiores
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # Calcular las coordenadas x de los límites izquierdo y derecho del triángulo a la altura correspondiente
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # Construir la forma de la sombra
    shadow_points = [
        (x_left_top + shadow_offset, y_top - shadow_offset),
        (x_right_top + shadow_offset, y_top - shadow_offset),
        (x_right_bottom + shadow_offset, y_bottom - shadow_offset),
        (x_left_bottom + shadow_offset, y_bottom - shadow_offset)
    ]
    shadow = Polygon(shadow_points, closed=True, facecolor='black', alpha=0.15, zorder=i+1)
    ax.add_patch(shadow)

# Dibujar el gráfico principal
for i in range(num_layers):
    # Coordenadas y superiores e inferiores
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # Calcular las coordenadas x de los límites izquierdo y derecho del triángulo a la altura correspondiente
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # Construir la forma de la franja trapezoidal/triangular
    points = [
        (x_left_top, y_top),
        (x_right_top, y_top),
        (x_right_bottom, y_bottom),
        (x_left_bottom, y_bottom)
    ]

    # Agregar un ligero cambio de transparencia para que la parte inferior sea más obvia
    alpha = 0.95 - i * 0.03 if i < num_layers - 1 else 0.95
    tri = Polygon(points, closed=True, facecolor=colors[i], edgecolor='white', linewidth=1.5, alpha=alpha, zorder=i+2)
    ax.add_patch(tri)

    # Escribir texto en el centro de cada capa
    y_text = (y_top + y_bottom) / 2
    ax.text(0.5, y_text, f"{labels[i]}",
            color='black', ha='right', va='center', fontsize=13, fontweight='medium',
            transform=ax.transAxes, zorder=10)

    # Agregar etiquetas de porcentaje
    ax.text(0.52, y_text, f"{values[i]}%",
            color='white', ha='left', va='center', fontsize=13, fontweight='bold',
            transform=ax.transAxes, zorder=10)

# Agregar nuevo texto relacionado con el título, ajustar el título y el subtítulo según los requisitos de la versión de los chicos
plt.text(0.5, 1.02, "Versión de Chicos", ha='center', fontsize=22, weight='bold', color=base_color, transform=ax.transAxes)
plt.text(0.5, 0.98, "Lógica de Desprecio: Intuitividad - Tasa de Uso Masculino", ha='center', fontsize=14, color='#666666', transform=ax.transAxes)

# Ajustar el diseño
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.05)
plt.show()