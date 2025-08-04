import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # Importar PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Datos
categorias = ['Menos de 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Más de 65']
porcentaje_edad = [2, 15, 40, 30, 20, 5, 2]  # Datos de porcentaje de edad
valores_tgi = [70, 130, 120, 90, 80, 60, 60]  # Datos de TGI

x = np.arange(len(categorias))

# Crear un gráfico
fig, ax1 = plt.subplots(figsize=(10, 5), dpi=100)

# Dibujar un gráfico de barras para el porcentaje de edad
grafico_barras = ax1.bar(categorias, porcentaje_edad, color='#4A7AFE', width=0.5, label='Edad')
ax1.set_ylim([0, 50])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el eje y izquierdo en formato de porcentaje
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(10))

# Crear un segundo eje y para dibujar el gráfico de línea TGI
ax2 = ax1.twinx()
grafico_linea = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# Establecer el intervalo de graduación para el eje y derecho
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Añadir un título
plt.title('Edad de los profesionales de la industria de servicios legales', fontsize=14, fontweight='bold')

# Añadir etiquetas de datos al gráfico de barras
for i, rect in enumerate(grafico_barras):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., altura + 1,
             f'{porcentaje_edad[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE', fontweight='bold')

# Añadir etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(categorias, valores_tgi)):
    # Ajustar la posición de la etiqueta según el valor de TGI para evitar solapamiento
    y_offset = 8 if y_val < 100 else 12
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, y_offset),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combinar las leyendas y ajustar la posición debajo del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Porcentaje de edad'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.15),
           ncol=2, fontsize=10)

# Optimizar el diseño para dejar espacio para la leyenda
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Mostrar el gráfico
plt.show()