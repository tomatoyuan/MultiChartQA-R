import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter  # Importar PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Datos
categorias = ['Alto Consumo', 'Consumo Medio', 'Bajo Consumo']
nivel_de_consumo = [37, 40, 20]
valores_tgi = [110, 90, 100]

x = np.arange(len(categorias))

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)

# Dibujar el gráfico de barras del nivel de consumo
grafico_barras = ax1.bar(categorias, nivel_de_consumo, color='#4A7AFE', width=0.5)
ax1.set_ylim([0, 60])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el eje y izquierdo en formato porcentaje y eliminar la etiqueta del eje y
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(20))

# Crear un segundo eje y para dibujar el gráfico de línea del TGI
ax2 = ax1.twinx()
grafico_linea = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', linewidth=2)
ax2.set_ylim(0, 150)
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Establecer el intervalo de graduación del eje y derecho y eliminar la etiqueta del eje y
ax2.yaxis.set_major_locator(MultipleLocator(50))

# Agregar un título
plt.title('Nivel de Consumo de Personas Involucradas en la Industria de Servicios Legales', fontsize=14, fontweight='bold')

# Agregar etiquetas de datos al gráfico de barras
for i, rect in enumerate(grafico_barras):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., altura + 1,
             f'{nivel_de_consumo[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE', fontweight='bold')

# Agregar etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(categorias, valores_tgi)):
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, 7),  # Desplazamiento vertical
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10,
                color='#FF9900',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combinar las leyendas y ajustar la posición debajo del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Nivel de Consumo'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-', 
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, fontsize=10)

# Optimizar el diseño
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Mostrar el gráfico
plt.show()