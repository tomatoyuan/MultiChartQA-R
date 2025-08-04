import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据
labels = ['显著变糟', '变糟一些', '维持现状', '改善一点', '显著改善']
values = [2, 9, 24, 54, 11]

# 颜色配置（与原图渐变感相似的蓝色系列）
colors = ['#c6dbef', '#9ecae1', '#6baed6', '#3182bd', '#08519c']

# 创建水平条形图
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(labels, values, color=colors)

# 添加数据标签
for bar in bars:
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width()}%', va='center', fontsize=10, color='gray')

# 高亮“改善一点”和“显著改善”区域
highlight_rect = patches.Rectangle(
    (0, 3 - 0.5), max(values) + 10, 2, linewidth=0, edgecolor=None,
    facecolor='#e5f5e0', alpha=0.4, zorder=0
)
ax.add_patch(highlight_rect)

# 标题和说明
plt.title("中国消费者对2024年底财务状况的改善持乐观态度", fontsize=13, weight='bold')
plt.suptitle("65%的中国消费者对2024年底财务状况的改善持乐观态度\n您认为到2024年底，您的家庭财务状况与现在相比会如何？",
             x=0.5, y=1.05, fontsize=10, color='navy', ha='center')
plt.figtext(0.99, 0.01, "Source: NIQ Consumer Outlook 2024, APAC",
            horizontalalignment='right', fontsize=9, color='gray')

plt.tight_layout()
plt.show()