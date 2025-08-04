import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 数据
# 翻译为西班牙语：Etiquetas para las secciones del gráfico circular
labels = ['Aumento de menos de 1 hora', 'Aumento de 1 - 2 horas', 'Aumento de más de 2 horas']
# 翻译为西班牙语：Tamaños (porcentajes) de cada sección del gráfico circular
sizes = [55, 28, 17]
# 翻译为西班牙语：Colores para cada sección del gráfico circular
colors = ['#D1C4E9', '#7E57C2', '#4527A0']

# 创建图形
# 翻译为西班牙语：Crear una figura y un eje para el gráfico
fig, ax = plt.subplots(figsize=(7, 6))

# 绘制饼图，使用 autopct 自动显示比例并居中显示
# 翻译为西班牙语：Dibujar un gráfico circular, mostrar automáticamente los porcentajes y centrarlos
wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.5, edgecolor='white'),
    autopct='%1.0f%%',
    pctdistance=0.75
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(13)
    autotext.set_fontweight('bold')

# 左侧文字
# 翻译为西班牙语：Texto en el lado izquierdo del gráfico
ax.text(-1.5, 0.1, '45%', fontsize=24, fontweight='bold', color='#512DA8')
ax.text(-1.5, -0.1, 'Aumento de más de 1 hora', fontsize=11, color='#333333')

# 图例
# 翻译为西班牙语：Leyenda del gráfico
ax.legend(wedges, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False, fontsize=10)

# 数据来源
# 翻译为西班牙语：Fuente de los datos
plt.figtext(
    0.5, -0.1,
    "Fuente de datos: Encuesta de CBNData en julio de 2024\nQ23. ¿Cuánto ha aumentado su tiempo de trabajo diario promedio en comparación con hace 3 - 5 años?",
    wrap=True, ha='center', fontsize=9, color='gray'
)

plt.tight_layout()
plt.show()