import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['产品健康属性浓', '有现成礼盒包装更省心', '对收礼人较为实用', '性价比，花小钱办大事', '贵重，送出去面子足']
values = [87, 71, 70, 58, 41]

# 创建渐变色柱状图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values)

# 应用渐变色（通过颜色透明度渐变模拟）
for i, bar in enumerate(bars):
    bar.set_facecolor((0.6, 0, 0, 0.3 + 0.7 * values[i] / 100))  # 红色通道固定，透明度随值增加

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 上移3点
                textcoords="offset points",
                ha='center', va='bottom')

# 图表美化
ax.set_ylabel('关注比例（%）')
ax.set_title('购置新年礼物时关注点分布（带渐变色）')
plt.xticks(rotation=20)
plt.tight_layout()

plt.show()