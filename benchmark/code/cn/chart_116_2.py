import matplotlib.pyplot as plt
import numpy as np

# 线上购买农货产品的原因
reasons = [
    "方便，节省时间和精力", "购前可以更好了解货品", "可选择货品丰富", 
    "优惠活动多", "价格便宜", "可购买其他地区的产品", 
    "货品质量有保障", "可购买反季节产品"
]
# 对应占比（%）
proportions = [41.29, 40.65, 40.00, 38.71, 38.71, 37.42, 32.90, 29.03]

x = np.arange(len(reasons))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者偏好在线上购买农货产品的原因')

plt.tight_layout()
plt.show()