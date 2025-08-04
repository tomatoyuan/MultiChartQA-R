import matplotlib.pyplot as plt
import numpy as np

# 数据准备
provinces = ["湖北", "浙江"]
# 各届奥运会（注意：原数据里24届出现两次，这里按列标题顺序处理 ）
games = ["23届", "24届", "24届", "26届", "27届", "28届", "29届", "30届"]  
# 湖北金牌数
hubei_golds = [1, 1, 3, 4, 6, 4, 5, 2]  
# 浙江金牌数
zhejiang_golds = [2, 1, 1, 1, 1, 4, 2, 4]  

x = np.arange(len(games))  # x轴刻度位置
width = 0.35  # 柱状图宽度

fig, ax = plt.subplots()
# 绘制湖北数据
rects1 = ax.bar(x - width/2, hubei_golds, width, label='湖北')  
# 绘制浙江数据
rects2 = ax.bar(x + width/2, zhejiang_golds, width, label='浙江')  

# 设置x轴刻度与标签
ax.set_xticks(x)
ax.set_xticklabels(games)
# y轴标题
ax.set_ylabel('金牌数')  
# 图表标题
ax.set_title('湖北、浙江各届奥运会金牌数对比')  
ax.legend()  # 显示图例

# 为每个柱子添加数值标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 标签距离柱子的垂直距离
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()  # 优化布局
plt.show()  # 显示图表