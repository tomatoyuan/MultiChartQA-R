import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022.7"]
# 总融资数量（笔）
total_financing = [10, 11, 12, 12, 14, 6, 9]
# 亿元以上融资数量（笔）
billion_financing = [2, 3, 2, 3, 3, 3, 2]

# 柱状图宽度
bar_width = 0.35
# 颜色设置，贴近原图绿色和蓝色
colors = ["#49C639", "#F664D9"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制总融资数量柱状图
x = np.arange(len(years))
total_bars = ax.bar(x - bar_width/2, total_financing, width=bar_width, color=colors[0], label="总融资数量（笔）")
# 绘制亿元以上融资数量柱状图
billion_bars = ax.bar(x + bar_width/2, billion_financing, width=bar_width, color=colors[1], label="亿元以上融资数量（笔）")

# 添加总融资数量数据标注
for bar in total_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加亿元以上融资数量数据标注
for bar in billion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("融资数量（笔）")
# 设置标题
ax.set_title("2016-2022年7月中国低代码融资事件数量", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()