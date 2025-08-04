import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2007", "2009", "2011", "2013", "2015", "2017", "2019"]
# 各类去向的占比（模拟数据，尽量贴近原图趋势 ）
employment = [54, 46, 56, 55, 59, 58, 51]    # 就业
further_study = [20, 25, 19, 19, 27, 29, 33] # 升学或拟升学
waiting = [26, 30, 25, 26, 15, 13, 16]       # 待就业及其他

# 颜色配置（尽量贴近原图）
colors = ["#A4C639", "#8EBF8F", "#87CEEB"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制堆叠柱状图
bottom = np.zeros(len(years))
for i, (label, data, color) in enumerate(zip(["就业", "升学或拟升学", "待就业及其他"], 
                                            [employment, further_study, waiting], 
                                            colors)):
    ax.bar(years, data, bottom=bottom, color=color, label=label)
    bottom += data

    # 添加数据标注
    for x, y in zip(years, data):
        ax.annotate(f'{y}%',
                    xy=(x, bottom[i] - y/2),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# 设置y轴刻度（0-100%）
ax.set_ylim(0, 100)
# 设置标题
ax.set_title("2007-2019年中国大学生毕业去向", fontsize=14, fontweight="bold")

# 添加图例
ax.legend(loc='lower right')

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()