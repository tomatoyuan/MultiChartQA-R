import matplotlib.pyplot as plt
import numpy as np
import matplotlib


# 数据
labels = ['增加1小时以内', '增加1-2小时', '增加2小时以上']
sizes = [55, 28, 17]
colors = ['#D1C4E9', '#7E57C2', '#4527A0']

# 创建图形
fig, ax = plt.subplots(figsize=(7, 6))

# 绘制饼图，使用 autopct 自动显示比例并居中显示
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
ax.text(-1.5, 0.1, '45%', fontsize=24, fontweight='bold', color='#512DA8')
ax.text(-1.5, -0.1, '增加超过1小时', fontsize=11, color='#333333')

# 图例
ax.legend(wedges, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False, fontsize=10)

# 数据来源
plt.figtext(
    0.5, -0.1,
    "数据来源：2024年7月CBNData问卷调研\nQ23. 相较3-5年之前，您的平均每天工作时长增加了多少？",
    wrap=True, ha='center', fontsize=9, color='gray'
)

plt.tight_layout()
plt.show()