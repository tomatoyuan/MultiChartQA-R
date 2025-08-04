import matplotlib.pyplot as plt
import numpy as np

# Datos
años = [2000, 2019, 2020, 2021]
esperanza_de_vida = [66.8, 73.2, 72.5, 71.4]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Convertir años a variables categóricas (distribución uniforme)
y_pos = np.arange(len(años))

# Dibujar un gráfico de barras horizontales con relleno de color degradado
colores = plt.cm.Greens(np.linspace(0.4, 0.8, len(años)))
barras = ax.barh(y_pos, esperanza_de_vida, color=colores, alpha=0.8, edgecolor='gray', linewidth=0.5)

# Agregar etiquetas de datos
for barra, valor in zip(barras, esperanza_de_vida):
    ax.text(barra.get_width() + 0.2,
            barra.get_y() + barra.get_height() / 2,
            f'{valor}',
            va='center',
            fontweight='bold',
            fontsize=10)

# Agregar una nota auxiliar indicando el mismo nivel que 2012
ax.annotate('Mismo nivel que 2012',
            xy=(71.4, y_pos[-1]),
            xytext=(73, y_pos[-1] - 0.3),
            arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8),
            fontsize=10)

# Establecer las etiquetas de las marcas del eje y a años (distribución uniforme)
ax.set_yticks(y_pos)
ax.set_yticklabels(años, fontsize=11)

# Establecer el rango y las marcas del eje x
ax.set_xlim(65, 75)
ax.set_xticks(np.arange(65, 76, 1))

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Agregar un título y un subtítulo
fig.suptitle('Impacto de la pandemia de COVID - 19 en la esperanza de vida global',
             fontsize=16,
             fontweight='bold',
             y=0.96)

ax.set_title('Tendencia de la esperanza de vida global (2000 - 2021)',
             fontsize=13,
             loc='left',
             pad=12)

# Agregar una leyenda
ax.legend([barras[0]], ['Esperanza de vida (años)'], loc='lower right')

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajustar el diseño
plt.subplots_adjust(bottom=0.1, left=0.15)

# Mostrar el gráfico
plt.show()