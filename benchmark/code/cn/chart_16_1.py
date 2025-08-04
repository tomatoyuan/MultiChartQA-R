import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2011, 2012, 2013, 2014, 2015]
# 清华录取省状元数
qinghua = [35, 43, 50, 42, 43]
# 北大录取省状元数
beida = [23, 27, 24, 48, 38]

# 设置条形宽度
bar_width = 0.35
# 生成 x 轴位置，用于放置两组条形
x = np.arange(len(years))  

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制清华的条形
rects1 = ax.bar(x - bar_width/2, qinghua, bar_width, label='清华', color='#6699CC')
# 绘制北大的条形
rects2 = ax.bar(x + bar_width/2, beida, bar_width, label='北大', color='#CC6666')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置 y 轴标签
ax.set_ylabel('录取省状元数')
# 设置标题
ax.set_title('2011-2015年清华、北大录取省状元数对比')
# 添加图例
ax.legend()

# 在条形上标注数值
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

# 调整布局，避免标签重叠
fig.tight_layout()
# 显示图表
plt.show()