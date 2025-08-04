import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator  # Importar MultipleLocator
from matplotlib.patches import Patch  # Importar Patch para crear elementos personalizados de la leyenda
from matplotlib.lines import Line2D   # Importar Line2D para crear elementos personalizados de la leyenda

# Datos
categorias = ['Hombre', 'Mujer']
porcentaje_genero = [51, 49]  # Proporción de género
valores_tgi = [85, 115]  # Valores TGI, se pueden ajustar según la situación real

x = np.arange(len(categorias))

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)  # Aumentar la altura del gráfico para dejar espacio para la leyenda debajo

# Dibujar el gráfico de barras de la proporción de género
grafico_barras = ax1.bar(categorias, porcentaje_genero, color='#4A7AFE', width=0.5, label='Género')
ax1.set_ylabel('Proporción de género (%)', fontsize=12, color='#4A7AFE')
ax1.set_ylim([46, 52])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el intervalo de las marcas de la eje y izquierda a 2
ax1.yaxis.set_major_locator(MultipleLocator(2))

# Crear una segunda eje y para dibujar el gráfico de línea TGI
ax2 = ax1.twinx()
grafico_linea = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylabel('TGI', fontsize=12, color='#FF9900')
ax2.set_ylim(0, 150)

# Establecer el intervalo de las marcas de la eje y derecha a 50
ax2.yaxis.set_major_locator(MultipleLocator(50))

ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Agregar un título
plt.title('Proporción de género de personas involucradas en la industria de servicios legales', fontsize=14, fontweight='bold')

# Agregar etiquetas de datos al gráfico de barras
for i, rect in enumerate(grafico_barras):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., altura + 0.1,
             f'{porcentaje_genero[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# Agregar etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(categorias, valores_tgi)):
    # Ajustar la posición de la etiqueta para que esté a la derecha del punto de datos
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(10, 0),  # Desplazar 10 puntos hacia la derecha
                textcoords='offset points',
                ha='left', va='center',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

# Combinar las leyendas y ajustar la posición debajo del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Género'),  # Leyenda para el gráfico de barras
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)  # Leyenda para el gráfico de línea
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimizar el diseño para dejar espacio para la leyenda
plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Ajustar el límite del gráfico, dejando un 10% de espacio en la parte inferior

# Mostrar el gráfico
plt.show()