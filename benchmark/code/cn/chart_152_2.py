# 图表3：重新绘制横向柱状图，优化颜色方案与标签可视化

import matplotlib.pyplot as plt

factors = [
    "穿着舒适，不紧绷不勒",
    "塑形臀部，提升轮廓",
    "优质面料，柔软亲肤",
    "弹性高，包容性高",
    "微压塑形，显瘦修身"
]
percentages = [38, 33, 32, 30, 28]

colors = ['#ec407a', '#f06292', '#f48fb1', '#f8bbd0', '#fce4ec']  # 渐变粉

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(factors, percentages, color=colors, edgecolor='gray')

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', fontsize=10)

# 标题与美化
ax.set_title("鲨鱼裤购买影响因素 Top5", fontsize=14)
ax.invert_yaxis()  # 最高的在上方
ax.set_xlim(0, 45)
ax.set_xlabel("占比（%）")
plt.tight_layout()
plt.show()