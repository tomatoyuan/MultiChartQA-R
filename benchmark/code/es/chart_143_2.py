import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
canales = [
    ("Venta minorista fuera de línea", 50.2, "#FF6347"),
    ("Recomendación de conocidos", 36.4, "#FFD700"),
    ("Publicidad tradicional", 40.6, "#FFDAB9"),
    ("Plataformas de compartición de contenido", 24.0, "#F4A460"),
    ("Plataformas de vídeos cortos", 42.3, "#FFB6C1"),
    ("Plataformas de comercio electrónico", 49.6, "#FFA07A"),
]

# Coordenadas del diseño hexagonal (ajustadas manualmente para aproximarse al diseño original)
coords_hexagonales = [
    (0, 1),   # Venta minorista fuera de línea
    (1, 0),   # Recomendación de conocidos
    (1, -1),  # Publicidad tradicional
    (0, -2),  # Plataformas de compartición de contenido
    (-1, -1), # Plataformas de vídeos cortos
    (-1, 0),  # Plataformas de comercio electrónico
]

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # Ocultar los ejes

# Dibujar hexágonos y agregar texto
for (canal, porc, color), (x, y) in zip(canales, coords_hexagonales):
    # Dibujar un hexágono (simulado con un círculo)
    hexagono = plt.Circle((x, y), 0.4, color=color, alpha=0.8)
    ax.add_artist(hexagono)
    # Agregar el nombre del canal y el porcentaje
    ax.text(x, y + 0.1, canal, ha='center', va='bottom', fontsize=10)
    ax.text(x, y - 0.1, f'{porc}%', ha='center', va='top', fontsize=9, color='white')

# Título
ax.text(0, 1.8, 'Encuesta 2023 sobre los canales de información de cosméticos de los consumidores chinos', ha='center', fontsize=12, fontweight='bold')
ax.text(0, 1.5, 'Encuesta 2023 sobre los canales de información de cosméticos de los consumidores en China', 
        ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()