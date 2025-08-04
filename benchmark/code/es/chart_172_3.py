import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['2021', '2022', '2026E']
valores = [64416, 69700.8, 93311.9]
x = np.arange(len(años))

# Creación del gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Gráfico de barras
barras = ax.bar(x, valores, color='#00d2c8', width=0.5, label='Tamaño del mercado \n(miles de millones de yuanes)')

# Agregar etiquetas de valores
for i, v in enumerate(valores):
    ax.text(x[i], v + 2000, f'{v}', ha='center', va='bottom', fontsize=10)

# Agregar anotación de CAGR
ax.annotate('CAGR = 7.6%',
            xy=(0, valores[0] + 8000), xytext=(0.8, valores[2] + 8000),
            textcoords='data',
            fontsize=13, color='#00d2c8', fontweight='bold')

# Configuración de los ejes
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11)
ax.set_ylim(0, 105000)
ax.set_ylabel('Unidad: miles de millones de yuanes', fontsize=12)
ax.set_title('Mercado global de alimentos para mejorar la inmunidad', fontsize=14, fontweight='bold', pad=20)

# Leyenda
ax.legend(loc='upper left', fontsize=10)

# Líneas de cuadrícula
ax.yaxis.grid(True, linestyle='--', alpha=0.3)

# Embellir el borde
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()