import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Datos (estimados visualmente del gráfico, reemplazar con datos precisos si están disponibles)
categorias = ['Menos de 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Más de 65']
porcentaje_edad = [2, 10, 45, 25, 15, 5, 3]  # Proporción de edad
valores_tgi = [60, 90, 120, 100, 90, 110, 180]  # Datos de TGI

x = np.arange(len(categorias))

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(12, 6), dpi=100)

# Dibujar el gráfico de barras de la proporción de edad
grafico_barras = ax1.bar(categorias, porcentaje_edad, color='#4A7AFE', width=0.5, label='Edad')
ax1.set_ylim([0, 55])  # Aumentar el límite superior para dejar espacio para las anotaciones
ax1.tick_params(axis='y', labelcolor='#4A7AFE', labelsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=12)

# Establecer el intervalo de las marcas en el eje y izquierdo
ax1.yaxis.set_major_locator(MultipleLocator(10))

# Añadir anotaciones de datos al gráfico de barras
for i, rect in enumerate(grafico_barras):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., altura + 1,
             f'{porcentaje_edad[i]}%',
             ha='center', va='bottom', fontsize=10, color='#4A7AFE')

# Crear un segundo eje y para dibujar el gráfico de línea de TGI
ax2 = ax1.twinx()
grafico_linea, = ax2.plot(categorias, valores_tgi, color='#FF9900', marker='o', 
                      label='TGI', linewidth=2, markersize=8)
ax2.set_ylim(0, 220)  # Aumentar el límite superior para dejar espacio para las anotaciones

# Establecer el intervalo de las marcas en el eje y derecho
ax2.yaxis.set_major_locator(MultipleLocator(50))
ax2.tick_params(axis='y', labelcolor='#FF9900', labelsize=10)

# Añadir anotaciones de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(x, valores_tgi)):
    ax2.annotate(f'{y_val}',
                xy=(x_val, y_val),
                xytext=(0, 10) if i != 6 else (0, -15),  # Colocar la anotación debajo para el último punto
                textcoords="offset points",
                ha='center',
                va='bottom' if i != 6 else 'top',
                fontsize=10,
                color='#FF9900',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#FF9900", alpha=0.8))

# Añadir el título
plt.title('Edad de la población en litigios de divorcio', fontsize=16, fontweight='bold')

# Combinar las leyendas y ajustar la posición debajo del gráfico
elementos_leyenda = [
    Patch(facecolor='#4A7AFE', edgecolor='w', label='Proporción de Edad'),
    Line2D([0], [0], color='#FF9900', marker='o', linestyle='-',
           label='Índice TGI', linewidth=2, markersize=6)
]

ax1.legend(handles=elementos_leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.12),
           ncol=2, fontsize=12, frameon=False)

# Añadir líneas de cuadrícula para mejorar la legibilidad
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Optimizar el diseño para dejar espacio para la leyenda
plt.tight_layout(rect=[0, 0.1, 1, 0.95])

# Mostrar el gráfico
plt.show()