import matplotlib.pyplot as plt
import numpy as np

# 数据
grupos = ['Total personas', 'Hombres', 'Mujeres', '18 - 34 años', '35 - 64 años', 'Ciudades de primer nivel', 'Ciudades de bajo nivel']
valores = [31.4, 29.8, 33.2, 26.7, 32.6, 28.6, 33.0]
colores = ['#bbbbbb'] + ['#ff2d55'] * 6  # El primer elemento en gris, el resto en rojo

y = np.arange(len(grupos))

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Gráfico de barras horizontales
barras = ax.barh(y, valores, color=colores, height=0.6)

# Agregar etiquetas de valores a la derecha
for i, (barra, val) in enumerate(zip(barras, valores)):
    ax.text(val + 0.5, barra.get_y() + barra.get_height() / 2, f'{val:.1f}%', va='center', fontsize=10)

# Línea de referencia discontinua (alineada con el valor máximo)
ax.axvline(x=31.4, linestyle='--', color='gray', linewidth=2)

# Configurar etiquetas y título
ax.set_yticks(y)
ax.set_yticklabels(grupos, fontsize=11)
ax.set_xlim(0, 40)
ax.invert_yaxis()  # Colocar "Total personas" en la parte superior
ax.set_xlabel('Penetración semanal (%)', fontsize=12)
ax.set_title('Penetración semanal de micro - novelas en escena\nentre diferentes segmentos de la población', fontsize=14, fontweight='bold', pad=20)

# Quitar los bordes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Líneas de cuadrícula
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()