import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据
etiquetas = ['Empeorará notablemente', 'Empeorará un poco', 'Se mantendrá igual', 'Mejorará un poco', 'Mejorará notablemente']
valores = [2, 9, 24, 54, 11]

# 颜色配置（与原图渐变感相似的蓝色系列）
colores = ['#c6dbef', '#9ecae1', '#6baed6', '#3182bd', '#08519c']

# 创建水平条形图
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.barh(etiquetas, valores, color=colores)

# 添加数据标签
for barra in barras:
    ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height()/2,
            f'{barra.get_width()}%', va='center', fontsize=10, color='gray')

# 高亮“改善一点”和“显著改善”区域
rectangulo_destacado = patches.Rectangle(
    (0, 3 - 0.5), max(valores) + 10, 2, linewidth=0, edgecolor=None,
    facecolor='#e5f5e0', alpha=0.4, zorder=0
)
ax.add_patch(rectangulo_destacado)

# 标题和说明
plt.title("Los consumidores chinos son optimistas sobre la mejora de su\n situación financiera a finales de 2024", fontsize=13, weight='bold')
plt.suptitle("El 65% de los consumidores chinos son optimistas sobre la mejora de su situación financiera a finales de 2024\n¿Cómo crees que estará la situación financiera de tu familia a finales de 2024 en comparación con ahora?",
             x=0.5, y=1.05, fontsize=10, color='navy', ha='center')
plt.figtext(0.99, 0.01, "Fuente: NIQ Consumer Outlook 2024, APAC",
            horizontalalignment='right', fontsize=9, color='gray')

plt.tight_layout()
plt.show()