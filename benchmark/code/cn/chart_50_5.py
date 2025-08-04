import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2023", "2024", "2025e", "2026e", "2027e", "2028e"]
# 全球出货量（万台）
global_shipments = [34, 234, 585, 1070, 1730, 2600]
# 中国出货量（万台）
china_shipments = [10, 36, 108, 324, 648, 972]

x = np.arange(len(years))  # x 轴刻度位置
width = 0.35  # 每个分组中柱状图的宽度

fig, ax = plt.subplots()

# 绘制全球出货量柱状图
rects1 = ax.bar(x - width/2, global_shipments, width, label='全球出货量 (万台)', color='greenyellow')
# 绘制中国出货量柱状图
rects2 = ax.bar(x + width/2, china_shipments, width, label='中国出货量 (万台)', color='dodgerblue')

# 添加标题和坐标轴标签
ax.set_title('2023-2028年 AI眼镜出货规模和预测')
ax.set_xticks(x)
ax.set_xticklabels(years)

# 为每个柱状图添加数值标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# 添加图例
ax.legend()

plt.show()