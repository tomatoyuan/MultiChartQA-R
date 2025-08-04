import matplotlib.pyplot as plt
import numpy as np

# 日期数据
dates = ['8-21', '8-23', '8-25', '8-27', '8-29', '8-31', '9-02', '9-04', '9-06']
# 搜索热度数据，可根据实际图表准确数值调整，这里为示意
search_heat = [32000, 26000, 19000, 14000, 17500, 31000, 11500, 9000, 19500]

x = np.arange(len(dates))  # x轴坐标

fig, ax = plt.subplots()
# 绘制柱状图
rects = ax.bar(x, search_heat, color=['r', 'r', 'gold', 'b', 'orange', 'r', 'lightgreen', 'b', 'r'])

# 设置x轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(dates)
# 设置y轴范围
ax.set_ylim(0, 35000)
# 设置标题和坐标轴标签
ax.set_title('电信诈骗搜索热度')
ax.set_ylabel('搜索热度')

# 在柱子上标注数值（可选，如需更贴近原图可不标注）
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()