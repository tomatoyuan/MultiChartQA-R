import matplotlib.pyplot as plt
import numpy as np

# 关注方面
aspects = ["价格", "界面设计与操作使用", "电池", "外观设计", "手机匹配速度", "使用准确性", 
           "防水功能", "售后服务", "品牌", "防摔功能"]
# 对应占比（%）
proportions = [47.77, 44.33, 40.38, 36.56, 33.63, 32.48, 
               22.93, 22.17, 21.91, 14.01]

x = np.arange(len(aspects))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(aspects, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者购买智能手表时关注方面')

plt.tight_layout()
plt.show()