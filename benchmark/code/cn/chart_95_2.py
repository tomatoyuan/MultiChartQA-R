import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2007, 2009, 2011, 2013, 2015, 2017, 2019]
# 不同学历平均起薪（元/月，模拟数据，尽量贴近趋势）
specialty = [1410, 1510, 1856, 2285, 2734, 3185, 3548]
bachelor = [1788, 2276, 2743, 3278, 3961, 4825, 5417]
master = [3469, 3637, 4003, 5461, 6334, 8556, 8778]
doctor = [3252, 3757, 5118, 8800, 6746, 10774, 13849]

# 颜色配置（尽量贴近原图）
colors = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4"]
labels = ["专科生（元/月）", "本科生（元/月）", "硕士研究生（元/月）", "博士研究生（元/月）"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图并标注数据
for i, (data, color, label) in enumerate(zip([specialty, bachelor, master, doctor], colors, labels)):
    ax.plot(years, data, marker='o', color=color, label=label, linewidth=2)
    # 添加数据标注
    for x, y in zip(years, data):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(5, 5),  # 标注位置偏移
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color=color)

# 设置x轴刻度
ax.set_xticks(years)
# 设置标题
ax.set_title("2007-2019年不同学历层次大学毕业生平均起薪", fontsize=14, fontweight="bold")

# 添加图例
ax.legend(loc='upper left')

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()