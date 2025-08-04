import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 数据
actividades = ['Ecuestre', 'Golf', 'Glamping', 'Deportes acuáticos', 'Deportes extremos', 'Escalada']
valores = [181, 123, 120, 111, 120, 117]
categorias = ['Aire libre de lujo'] * 4 + ['Aire libre profesional'] * 2
colores = ['#d7a970'] * 4 + ['#f2c56d'] * 2

# 绘图
fig, ax = plt.subplots(figsize=(9, 8))
barras = ax.barh(actividades, valores, color=colores)

# Agregar etiquetas de valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 2, barra.get_y() + barra.get_height() / 2, f'{int(ancho)}',
            va='center', ha='left', fontsize=10, color='white', weight='bold')

# Bloques de color de fondo de categorías (área de marcado a la derecha)
ax.axhspan(-0.5, 3.5, facecolor='#3b2d44', alpha=0.3)
ax.text(150, 1.5, 'Aire libre de lujo', va='center', ha='center', fontsize=12, color='#FFFFFF', weight='bold')

ax.axhspan(3.5, 5.5, facecolor='#3a2b1f', alpha=0.3)
ax.text(150, 4.5, 'Aire libre profesional', va='center', ha='center', fontsize=12, color='#FFFFFF', weight='bold')

# Título y descripción del gráfico
plt.title('Escenarios de aire libre de alta preferencia', fontsize=16, weight='bold')

# Embellir el gráfico
ax.invert_yaxis()
ax.set_xlim(0, 200)
ax.set_xticks([])
y_pos = np.arange(len(actividades))
ax.set_yticks(y_pos)
ax.set_yticklabels(actividades, fontsize=12)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.text(0, -1.2, 'Fuente de datos: Encuesta de CBNData en mayo\n'
                  'Explicación de los datos: TGI de preferencia = proporción de esta \n'
                  'población que elige este escenario / proporción de todos los consumidores\n'
                  ' que eligen este escenario * 100, TGI>100 significa preferencia',
         fontsize=9, ha='left', va='bottom')

plt.tight_layout()
plt.show()