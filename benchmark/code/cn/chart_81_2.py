import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2018", "2019", "2020"]
# 通用仓库面积（亿平方米），数据大体一致即可
general_warehouse = [10.60, 10.80, 11.45]
# 高标准仓库面积（亿平方米），数据大体一致即可
high_standard_warehouse = [3.00, 3.15, 3.45]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制分组柱状图
x = np.arange(len(years))
bar_width = 0.35
# 通用仓库（绿色）
general_bars = ax.bar(x - bar_width/2, general_warehouse, width=bar_width, color="#C63982", label="通用仓库（亿平方米）")
# 高标准仓库（蓝色）
high_standard_bars = ax.bar(x + bar_width/2, high_standard_warehouse, width=bar_width, color="#64B5F6", label="高标准仓库（亿平方米）")

# 添加通用仓库数据标注
for bar in general_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加高标准仓库数据标注
for bar in high_standard_bars:
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
ax.set_ylabel("面积（亿平方米）")
# 设置标题
ax.set_title("2018-2020年中国通用仓库及高标准仓库面积", fontsize=14, fontweight="bold")

# 添加图例
ax.legend(loc='lower center')

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()