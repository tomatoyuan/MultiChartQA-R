import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Preparación de datos
industrias = [
    'Salud', 'Inmuebles/Construcción', 'Mayorista/Minorista', 'Automóvil',
    'Gobierno/Organizaciones sin fines de lucro', 'Hoteles/Turismo', 'Finanzas',
    'Publicidad/Marketing', 'Tecnologías de la información/Internet'
]
cobertura = [2.9, 3.5, 5.1, 6.1, 7.5, 8.2, 9.2, 19.9, 21.9]

# Crear un mapa de colores de gradiente
cmap = LinearSegmentedColormap.from_list("verde_personalizado", ["#E8F5E9", "#2E7D32"])

# Crear un objeto de trazado
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#F5F5F5')  # Establecer el color de fondo del gráfico
ax.set_facecolor('#FAFAFA')  # Establecer el color de fondo del eje

# Dibujar un gráfico de barras horizontales (utilizando color de gradiente)
y_pos = np.arange(len(industrias))
barras = ax.barh(y_pos, cobertura, color='#4CAF50', edgecolor='#2E7D32', linewidth=0.8)

# Aplicar color de gradiente
for i, barra in enumerate(barras):
    barra.set_color(cmap(i/len(barras)))

# Agregar etiquetas de datos (optimizar posición y estilo)
for i, v in enumerate(cobertura):
    ax.text(v + 0.3, i, f'{v}%', va='center', fontsize=11,
            fontweight='medium', color='#333333')

# Establecer el título y las etiquetas de los ejes (optimizar fuente y posición)
ax.set_title('¿Qué industrias se preocupan más por los "regalos de San Valentín"?',
             fontsize=18, pad=20, fontweight='bold', color='#333333')
ax.set_xlabel('Cobertura de la industria (%)', fontsize=13, labelpad=15, color='#555555')
ax.set_ylabel('Categorías de la industria', fontsize=13, labelpad=15, color='#555555')

# Establecer las etiquetas de las marcas del eje y
ax.set_yticks(y_pos)
ax.set_yticklabels(industrias, fontsize=11, color='#444444')

# Optimizar las marcas de los ejes y las líneas de la cuadrícula
ax.set_xlim(0, max(cobertura) + 3)
ax.grid(axis='x', linestyle='--', alpha=0.6, color='#CCCCCC')

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')

# Ajustar el diseño
plt.tight_layout(pad=2)

# Mostrar el gráfico
plt.show()