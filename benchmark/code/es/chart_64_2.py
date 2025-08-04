import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
etiquetas = [
    'Subida del 1%-20%', 'Subida del 21%-40%', 'Subida del 41%-60%', 'Subida del 61%-80%',
    'Subida del 81%-100%', 'Subida de más del 100%', 'Básicamente sin cambios', 'Bajada del 1%-20%',
    'Cuatro intervalos de bajada del 21%-100%', 'Diseño e inversión por la sede central del grupo'
]
porcentajes = [20.3, 36.6, 10.6, 6.5, 6.5, 2.4, 8.1, 4.1, 0, 4.9]

# Configuración de colores (similar a la imagen original, usar gris para categorías de bajada y verde para otras)
colores = ['#a5d65d'] * 7 + ['#d3d3d3'] + ['#a5d65d'] * 2

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(etiquetas))
barras = ax.barh(y, porcentajes, color=colores, height=0.6)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height()/2,
            f'{ancho}%', va='center', fontsize=9, color='#333')

# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(etiquetas, fontsize=10)

# Ocultar las marcas del eje x
ax.set_xticks([])

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Agregar un título
ax.set_title('Aumento/Disminución de los costos de diseño de dominio privado de comerciantes chinos en 2022 en comparación con el diseño inicial',
             fontsize=14, fontweight='bold', pad=20)

# Ajustar el diseño
plt.tight_layout()
plt.show()