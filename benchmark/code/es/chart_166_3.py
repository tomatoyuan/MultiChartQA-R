import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['2021', '2022', '2023']
total = [6, 42, 69]
local = [4, 25, 52]

ancho_barra = 0.4
pos_y = np.arange(len(años))

# 颜色
color_total = '#FFDDDD'
color_local = '#E0E0E0'

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 5))

barras1 = ax.barh(pos_y, total, height=ancho_barra, color=color_total, label='Número de registros de nuevos materiales (unidades)')
barras2 = ax.barh(pos_y, local, height=ancho_barra/2, color=color_local, label='Número de registros de nuevos materiales de empresas locales (unidades)')

# Agregar etiquetas de valores
for i, (b1, b2) in enumerate(zip(barras1, barras2)):
    ax.text(b1.get_width() + 1, b1.get_y() + b1.get_height()/2, f'{total[i]}', va='center', fontsize=10, color='red')
    ax.text(b2.get_width() + 1, b2.get_y() + b2.get_height()/2, f'{local[i]}', va='center', fontsize=10, color='black')

# Configurar el título y las etiquetas
ax.set_yticks(pos_y)
ax.set_yticklabels(años)
ax.invert_yaxis()
ax.set_xlim(0, max(total) + 10)
ax.set_title('Número de registros de nuevos materiales en la industria de cosméticos', fontsize=14, loc='left', pad=20)
ax.legend()

# Agregar texto explicativo en la parte superior
plt.figtext(0.01, -0.03,
            'En 2023, se completaron 69 registros de nuevos materiales, de los cuales 52 fueron de empresas locales, lo que representa \n'
            'el 75.36%. En comparación con 2022, el número de registros de nuevos materiales de empresas locales aumentó un 108%.',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()