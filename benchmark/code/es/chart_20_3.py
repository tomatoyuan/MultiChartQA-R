import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# ======================== 1. Datos y configuración básica ========================
labels = ["Melamina", "Decoración interior", "Cosméticos", "Consumo de alcohol", "Henna", "Contaminación atmosférica"]
sizes = [33, 10, 8, 8, 8, 7]

# Coordenadas de distribución en anillo hexagonal (conversión de coordenadas polares a cartesianas)
theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
radius = 1.2  # Controla el radio del anillo hexagonal
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Paleta de colores degradados personalizada (de rosa claro a rosa oscuro)
cmap = LinearSegmentedColormap.from_list(
    'pink_cmap', 
    ['#FFE6F0', '#FFABCD', '#E66493', '#CC3377', '#B30059', '#8B003C'],
    N=len(labels)
)

# ======================== 2. Inicializar el lienzo y los ejes ========================
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#F8F8FF')  # Fondo azul claro
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Ocultar los ejes

# ======================== 3. Dibujar hexágonos tridimensionales (con sombra + degradado) ========================
for i in range(len(labels)):
    # Hexágono principal (relleno degradado)
    hex_main = RegularPolygon(
        (x[i], y[i]), numVertices=6, radius=0.5, 
        facecolor=cmap(i), edgecolor='white', linewidth=2
    )
    ax.add_patch(hex_main)
    
    # Hexágono de sombra (simular efecto tridimensional)
    hex_shadow = RegularPolygon(
        (x[i] + 0.05, y[i] - 0.05), numVertices=6, radius=0.5, 
        facecolor='gray', alpha=0.2, edgecolor='none'
    )
    ax.add_patch(hex_shadow)
    
    # Dibujar el número de proporción (centrado, en negrita)
    ax.text(
        x[i], y[i], f"{sizes[i]}%", 
        ha='center', va='center', 
        fontsize=14, fontweight='bold', 
        color='white'
    )
    
    # Dibujar el texto de la etiqueta (diseño circular, ajustar el ángulo)
    text_angle = np.rad2deg(theta[i]) - 90  # Ajustar el ángulo del texto al hexágono
    ax.text(
        x[i] * 1.8, y[i] * 1.8, labels[i], 
        ha='center', va='center', 
        fontsize=12, color='#333333', 
        rotation=text_angle
    )

# ======================== 4. Agregar título y decoración ========================
# Título central
ax.text(
    0, 0, "Proporción de causas de cáncer", 
    ha='center', va='center', 
    fontsize=10, fontweight='bold', 
    color='#CC3377'
)

# Descripción en la parte inferior
ax.text(
    0, -2.4, "Fuente de datos: Estadísticas simuladas | Unidad: %", 
    ha='center', va='center', 
    fontsize=10, color='#666666', 
)

# Fondo degradado (difusión desde el centro hacia afuera)
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient_img = np.tile(gradient, (256, 1))
ax.imshow(
    gradient_img, extent=(-2.5, 2.5, -2.5, 2.5), 
    cmap=cm.get_cmap('Blues_r'), alpha=0.3
)

plt.tight_layout()
plt.show()