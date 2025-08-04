import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['茶产品']
mat2023 = [100]  # 假设的 MAT2023 数据，可替换为真实值
mat2024 = [118]  # 根据 +18% 假设的 MAT2024 数据，可替换为真实值 
growth_rate = 18  # 增长率

x = np.arange(len(categories))  # 柱状图 x 轴位置
width = 0.35  # 柱状图宽度

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mat2023, width, label='MAT2023', color='lightgreen')
rects2 = ax.bar(x + width/2, mat2024, width, label='MAT2024', color='green')

# 添加增长率箭头和文本
arrow_x = x[0]
arrow_y = max(mat2023 + mat2024) * 0.6  # 箭头位置，可调整
ax.annotate(f'+{growth_rate}%', xy=(arrow_x, mat2023[0]), xytext=(arrow_x, arrow_y),
            arrowprops=dict(facecolor='orange', shrink=0.05),
            ha='center', va='bottom', fontsize=14, color='orange')

# 添加数值标注函数
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# 为两个柱子添加数值标注
add_labels(rects1)
add_labels(rects2)

# 设置坐标轴标签等
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.title('MAT2023-MAT2024年线上淘宝天猫相关“茶”产品消费市场规模')
plt.show()