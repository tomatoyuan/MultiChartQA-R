import matplotlib.pyplot as plt
import numpy as np

# 年份与份额数据
years = ['MAT2022', 'MAT2023', 'MAT2024']
top5 = np.array([27, 34, 37])
top6_10 = np.array([15, 13, 11])
top11_20 = np.array([13, 12, 11])
others = 100 - (top5 + top6_10 + top11_20)

# 堆叠柱状图位置
x = np.arange(len(years))
bar_width = 0.6

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(top=0.88)

# 画堆叠柱状图
p1 = ax.bar(x, top5, bar_width, label='TOP5', color='#FF7F7F')
p2 = ax.bar(x, top6_10, bar_width, bottom=top5, label='TOP6-10', color='#FFBFA2')
p3 = ax.bar(x, top11_20, bar_width, bottom=top5+top6_10, label='TOP11-20', color='#FFD6A5')
p4 = ax.bar(x, others, bar_width, bottom=top5+top6_10+top11_20, label='其他', color='#D3D3D3')

# 添加所有部分的数值标签
for i in range(len(years)):
    # TOP5
    ax.text(x[i], top5[i] / 2, f"{top5[i]}%", ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # TOP6-10
    ax.text(x[i], top5[i] + top6_10[i] / 2, f"{top6_10[i]}%", ha='center', va='center',
            fontsize=10, color='black')

    # TOP11-20
    ax.text(x[i], top5[i] + top6_10[i] + top11_20[i] / 2, f"{top11_20[i]}%", ha='center', va='center',
            fontsize=10, color='black')

    # 其他
    ax.text(x[i], 100 - others[i] / 2, f"{others[i]}%", ha='center', va='center',
            fontsize=10, color='black')

# 设置坐标轴和标题
ax.set_title('MAT2022-MAT2024线上淘系\n“光腿神器”品牌份额占比变化', fontsize=15, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('品牌份额占比（%）', fontsize=12)
ax.set_ylim(0, 100)

# 添加数据来源注释
source_text = ("数据来源：魔镜市场情报数据，MAT2024：2023.07-2024.06\n"
               "数据说明：取数逻辑为天猫/淘宝/抖音平台下，“连裤袜/打底袜”类目下商品标题包含“光腿神器/光腿裸感神器”等关键词的消费数据；\n"
               "大数据：全洞察")
plt.figtext(0.5, -0.05, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

# 图例与样式
ax.legend(loc='upper right', frameon=False)
ax.set_facecolor('#f9f9f9')
plt.tight_layout()
plt.show()