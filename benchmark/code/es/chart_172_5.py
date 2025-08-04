import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# 数据
etiquetas = ['Suplemento de oligoelementos', 'Contiene fibra dietética', 'Contiene probióticos', 'Contiene DHA', 'Suplemento de vitaminas']
valores = [70, 56, 46, 41, 23]
x = np.arange(len(etiquetas))

# Crear el lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Lista de colores degradados personalizada (de oscuro a claro)
colores_degradados = [
    ('#00d2c8', '#a2f0ec'),
    ('#00c0d6', '#a3e8f5'),
    ('#00a6de', '#a4dbf7'),
    ('#0091e6', '#a5cef9'),
    ('#0077ed', '#a7c2fb')
]

# Dibujar cada barra con degradado
ancho_barra = 0.6
for i, (val, (color_superior, color_inferior)) in enumerate(zip(valores, colores_degradados)):
    # Barras con degradado personalizado (simuladas mediante superposición de rectángulos)
    for j in range(100):  # 100 segmentos para simular el degradado
        fraccion = j / 100
        altura = val * (1 / 100)
        y = altura * j
        color = LinearSegmentedColormap.from_list("grad", [color_inferior, color_superior])(fraccion)
        ax.add_patch(Rectangle((x[i] - ancho_barra / 2, y), ancho_barra, altura, color=color, linewidth=0))

    # Agregar el porcentaje en la parte superior de la barra
    ax.text(x[i], val + 1.5, f'{val}%', ha='center', fontsize=10)

# Establecer las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, fontsize=11, rotation=30)
ax.set_ylim(0, 80)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.set_title('Interés de los padres chinos en los componentes beneficiosos con efectos funcionales', fontsize=14, fontweight='bold', pad=20)

# Leyenda
ax.legend(['Porcentaje (%)'], loc='best', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# Mejorar la apariencia
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()