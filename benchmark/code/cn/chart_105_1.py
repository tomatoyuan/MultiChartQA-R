import matplotlib.pyplot as plt
import numpy as np

# 购买原因
reasons = ["健康监测", "产品设计精美有个性", "记录运动情况", "炫耀彰显身份", "查看小孩子或老人定位", 
           "方便自己的生活（如收发信息及电话）", "单纯的自我喜欢"]
# 对应占比（%）
proportions = [45.48, 44.71, 43.44, 40.38, 25.35, 25.10, 19.11]

x = np.arange(len(reasons))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者购买智能手表原因')

plt.tight_layout()
plt.show()