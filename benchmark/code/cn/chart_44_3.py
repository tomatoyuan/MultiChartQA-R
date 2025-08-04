import matplotlib.pyplot as plt
import numpy as np

# 零食类别
categories = ['甜饮料', '耐啃零食', '油炸膨化食品', '酸奶', '烘焙食品', '坚果', '辣味零食', '高糖食品', '果干蜜饯']
# 对应选择比例
percentages = [55, 43, 43, 42, 42, 39, 38, 36, 33]

x = np.arange(len(categories))  # x轴坐标

fig, ax = plt.subplots()
# 绘制柱状图
rects = ax.bar(x, percentages, color='green')

# 添加标题和坐标轴标签
ax.set_title('朋克加班人上班嘴馋时的零食选择分布')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('选择比例（%）')

# 在柱子上标注数值
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()