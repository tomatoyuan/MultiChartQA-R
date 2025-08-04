import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import font_manager as fm


# Datos
categorias = ['Antienvejecimiento (Traducción \n'
              'literal, quizás "Antienvejecimiento \n'
              'y reafirmación" sea mejor)',
              'Sosegado y anti-alérgico',
              'Nutrición y reparación',
              'Blanqueamiento y desmapeado', 'Hidratación']
q1_2023 = [648, 190, 297, 365, 191]
q1_2024 = [884, 215, 314, 395, 233]
crecimiento = [q1_2024[i] - q1_2023[i] for i in range(len(q1_2023))]

x = np.arange(len(categorias))
ancho = 0.35

# Configuración de colores
color_2023 = '#fcd7cc'
color_2024 = '#f29676'

fig, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, q1_2023, ancho, label='Número de marcas Q1 23', color=color_2023)
barras2 = ax.bar(x + ancho/2, q1_2024, ancho, label='Número de marcas Q1 24', color=color_2024)

# Etiquetas de valores
for i in range(len(x)):
    ax.text(x[i] - ancho/2, q1_2023[i] + 10, str(q1_2023[i]), ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + ancho/2, q1_2024[i] + 10, str(q1_2024[i]), ha='center', va='bottom', fontsize=10)
    ax.annotate(f'+{crecimiento[i]}',
                xy=(x[i] + ancho/2, q1_2024[i] + 40),
                xytext=(x[i] + ancho/2, q1_2024[i] + 60),
                ha='center',
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='black', lw=1))

# Área de borde de grupo
ax.add_patch(patches.Rectangle((-0.5, 0), 1.0, 1000, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(-0.5, 1050, 'Aumento de la competencia', color='orangered', fontsize=12)

ax.add_patch(patches.Rectangle((1.5, 0), 1.0, 500, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(1.5, 550, 'Competencia estable', color='peru', fontsize=12)

# Resto de configuraciones
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=30)
ax.set_ylabel('Número de marcas')
ax.set_ylim(0, 1200)

ax.set_title('[Subcategoría de cremas faciales] Patrón de competencia de marcas de \n'
             'cremas faciales por eficacia en Q1 24 (Comercio electrónico principal)')
ax.legend()

plt.tight_layout()
plt.show()