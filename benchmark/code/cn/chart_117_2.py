import matplotlib.pyplot as plt
import numpy as np

# 关注因素
factors = [
    "舒适性", "材质质感", "环保性", "耐用性", "易清洁性", "安全性", 
    "风格设计", "色彩搭配", "装饰性", "实用", "品牌", "售后服务", "折扣"
]
# 对应占比（%）
proportions = [37.69, 36.92, 35.38, 33.85, 33.46, 32.88, 
               32.50, 31.35, 30.38, 30.19, 28.08, 27.12, 25.00]

x = np.arange(len(factors))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者购买软装家居产品的关注因素')

plt.tight_layout()
plt.show()