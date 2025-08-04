import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["居民人均体育消费支出", "成年人人均体育消费支出", "老年人人均体育消费支出"]
# 2014年数据（元），数据大体一致即可
data_2014 = [926.0, 968.4, 504.0]
# 2020年数据（元），数据大体一致即可
data_2020 = [1330.4, 1758.2, 1092.2]

# 柱状图宽度
bar_width = 0.35
# 颜色设置，贴近原图绿色和蓝色
colors = ["#A4C639", "#64B5F6"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制2014年数据柱状图
x = np.arange(len(categories))
bar_2014 = ax.bar(x - bar_width/2, data_2014, width=bar_width, color=colors[0], label="2014年 (元)")
# 绘制2020年数据柱状图
bar_2020 = ax.bar(x + bar_width/2, data_2020, width=bar_width, color=colors[1], label="2020年 (元)")

# 添加2014年数据标注
for bar in bar_2014:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加2020年数据标注
for bar in bar_2020:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签
ax.set_ylabel("消费支出 (元)")
# 设置标题
ax.set_title("2014年&2020年中国人均体育消费支出", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()