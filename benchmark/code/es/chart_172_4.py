import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ['2022', '2028E']
valores = [449.25, 607.95]
x = np.arange(len(años))

# Creación del gráfico
fig, ax = plt.subplots(figsize=(7, 6))

# Gráfico de barras
barras = ax.bar(x, valores, color='#00d2c8', width=0.5, label='Tamaño del mercado (miles de millones de yuanes)')

# Agregar etiquetas de valores en la parte superior
for i, v in enumerate(valores):
    ax.text(x[i] - 0.1, v + 15, f'{v}', ha='center', va='bottom', fontsize=10)

# Agregar anotación de CAGR
ax.annotate('CAGR = 5.17%',
            xy=(x[0], valores[0] + 25), xytext=(x[1], valores[1] + 25),
            textcoords='data',
            arrowprops=dict(arrowstyle='-', linestyle='dotted', color='#00d2c8', linewidth=2),
            fontsize=13, color='#00d2c8', fontweight='bold')

# Configuración de los ejes
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=11)
ax.set_ylim(0, 700)
ax.set_ylabel('Unidad: miles de millones de yuanes', fontsize=12)
ax.set_title('Tamaño del mercado global de edulcorantes', fontsize=14, fontweight='bold', pad=20)

# Leyenda
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# Mejora visual
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])  # Dejar espacio para la leyenda
plt.show()