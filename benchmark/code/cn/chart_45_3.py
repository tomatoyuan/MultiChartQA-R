import matplotlib.pyplot as plt
import numpy as np

# 决策因素名称
labels = ['功能相关参数', '外观设计/时尚度', '用户评价/口碑', '价格/促销活动', 
          '品牌知名度', '售后服务', '明星/KOL代言', '联名款/限量款']
# 各因素对应的比例数据
values = [89, 61, 45, 35, 27, 19, 5, 3]

# 设置柱状图的横坐标位置
x = np.arange(len(labels))  
# 绘制柱状图，设置柱子宽度等
fig, ax = plt.subplots()
rects = ax.bar(x, values, width=0.5, color=['pink', 'pink', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'])

# 设置坐标轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')  # 旋转标签，避免重叠
ax.set_ylabel('比例（%）')
ax.set_title('消费者购买功能性服饰时的决策因素')

# 在柱子上标注数值
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}%'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 数值距离柱子顶部的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()  # 自动调整布局，避免标签等显示不全
plt.show()