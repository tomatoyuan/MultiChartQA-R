import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator  # Importar MultipleLocator
from matplotlib.patches import Patch  # Importar Patch para crear elementos personalizados de la leyenda
from matplotlib.lines import Line2D   # Importar Line2D para crear elementos personalizados de la leyenda

# Datos
categorias = ['Casado', 'Soltero']
porcentaje_genero = [80, 20]
valores_tgi = [60, 90]

x = np.arange(len(categorias))

# Crear un gráfico
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)  # Aumentar la altura del gráfico para dejar espacio para la leyenda debajo

# Dibujar un gráfico de barras del porcentaje de género
grafico_barras = ax1.bar(categorias, porcentaje_genero, color='#4A7AFE', width=0.5, label='Estado Civil')
ax1.set_ylabel('Estado Civil (%)', fontsize=12, color='#4A7AFE')
ax1.set_ylim([0, 100])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el intervalo de graduación del eje y izquierdo en 50
ax1.yaxis.set_major_locator(MultipleLocator(50))

# Crear un segundo eje y para dibujar el gráfico de línea TGI
ax2 = ax1.twinx()
grafico_linea = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylabel('TGI', fontsize=12, color='#FF9900')
ax2.set_ylim(0, 150)

# Establecer el intervalo de graduación del eje y derecho en 50
ax2.yaxis.set_major_locator(MultipleLocator(50))

ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Agregar un título
plt.title('Estado Civil de Personas Inscritas en la Industria de Servicios Legales', fontsize=14, fontweight='bold')

# Agregar etiquetas de datos al gráfico de barras
for i, rect in enumerate(grafico_barras):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., altura + 1.5,
             f'{porcentaje_genero[i]}%',
             ha='center', va='bottom', fontsize=12, color='#4A7AFE', fontweight='bold')

# Agregar etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(categorias, valores_tgi)):
    # Ajustar la posición de la etiqueta para que esté por encima o por debajo del punto de datos para evitar solapamiento
    y_offset = 7 if i == 0 else -10  # El punto de casado se desplaza hacia arriba, y el punto de soltero se desplaza hacia abajo
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, y_offset),
                textcoords='offset points',
                ha='center', va='bottom' if y_offset > 0 else 'top',
                fontsize=12,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combinar las leyendas y ajustar la posición debajo del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Estado Civil'),  # Leyenda del gráfico de barras
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)  # Leyenda del gráfico de línea
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimizar el diseño para dejar espacio para la leyenda
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Ajustar el límite del gráfico, dejando un 10% de espacio en la parte inferior

# Mostrar el gráfico
plt.show()