import matplotlib.pyplot as plt
import numpy as np

# 左侧购买原因数据
left_reasons = ["携带方便性", "操作便捷性", "握持舒适度", "颜值小而美", "减少屏幕使用时间", "价格较低"]
left_proportions = [73.5, 54.4, 45.2, 38.4, 24.1, 11.0]

# 右侧影响因素数据
right_factors = [
    "认为该品牌影响力大", "曾经购买过该品牌的其它手机", "性价比高", 
    "较好的售后服务", "系统更符合自己的使用习惯", "小屏技术领先同类品牌", 
    "处理器厂家"
]
right_proportions = [47.2, 46.6, 42.6, 40.2, 33.3, 19.7, 10.0]

fig = plt.figure(figsize=(16, 6))
# 左侧子图
ax1 = fig.add_subplot(121)
y1 = np.arange(len(left_reasons))
bars1 = ax1.barh(y1, left_proportions, color='orange')
for i, proportion in enumerate(left_proportions):
    ax1.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)
ax1.set_yticks(y1)
ax1.set_yticklabels(left_reasons)
ax1.set_xlabel('占比（%）')
ax1.set_title('中国消费者购买小屏手机的原因')

# 右侧子图
ax2 = fig.add_subplot(122)
y2 = np.arange(len(right_factors))
bars2 = ax2.barh(y2, right_proportions, color='orange')
for i, proportion in enumerate(right_proportions):
    ax2.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)
ax2.set_yticks(y2)
ax2.set_yticklabels(right_factors)
ax2.set_xlabel('占比（%）')
ax2.set_title('中国消费者选择小屏手机品牌的影响因素')

plt.tight_layout()
plt.show()