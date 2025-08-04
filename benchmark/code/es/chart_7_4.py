import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, PercentFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Datos
categorias = ['Universitarios y superiores', 'Carreras técnicas universitarias', 'Bachillerato y inferiores']
nivel_educativo = [20, 30, 60]  # Datos de nivel educativo
valores_tgi = [140, 125, 100]  # Datos de TGI

x = np.arange(len(categorias))

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(6, 5), dpi=100)

# Dibujar el gráfico de barras del nivel educativo
grafico_barras = ax1.bar(categorias, nivel_educativo, color='#4A7AFE', width=0.5, label='Nivel educativo')
ax1.set_ylim([0, 80])
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el intervalo de marcas y el formato para el eje y izquierdo
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
ax1.yaxis.set_major_locator(MultipleLocator(20))

# Crear un segundo eje y para dibujar el gráfico de línea TGI
ax2 = ax1.twinx()
grafico_linea = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', label='TGI', linewidth=2)
ax2.set_ylim(0, 150)

# Establecer el intervalo de marcas para el eje y derecho
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Añadir el título
plt.title('Nivel educativo de las personas que se dedican a la industria de servicios legales', fontsize=14, fontweight='bold')

# Añadir etiquetas de datos al gráfico de barras
for rect in grafico_barras:
    altura = rect.get_height()
    # Añadir etiquetas de porcentaje en el centro superior del gráfico de barras
    ax1.text(rect.get_x() + rect.get_width()/2, altura + 1.5,
             f'{altura}%',
             ha='center', va='bottom', fontsize=11, color='#4A7AFE', fontweight='bold')

# Añadir etiquetas de datos al gráfico de línea
for i, (cat, tgi) in enumerate(zip(categorias, valores_tgi)):
    # Ajustar el desplazamiento de la etiqueta según la posición del punto de datos para evitar superposiciones
    desplazamiento_y = 5 if tgi < 130 else 8  # Aumentar el desplazamiento adecuadamente para valores más altos
    ax2.annotate(f'{tgi}',
                 xy=(i, tgi),  # Usar el índice para la posición para evitar problemas con coordenadas en chino
                 xytext=(0, desplazamiento_y),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 fontsize=11, color='#FF9900', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#FF9900', alpha=0.8))

# Combinar las leyendas y ajustar la posición en la parte inferior del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Distribución del nivel educativo'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.1),
           ncol=2, fontsize=10)

# Optimizar el diseño para dejar espacio para la leyenda
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Mostrar el gráfico
plt.show()