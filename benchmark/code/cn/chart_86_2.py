import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2019", "2020", "2021"]
# 女性综艺数量占比（%），数据与图表一致
percentage = [9.8, 10.5, 14.7]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制折线图
line, = ax.plot(years, percentage, marker='o', color="#C6395A", label="女性综艺数量占比（%）", linewidth=2)

# 添加数据标注
for x, y in zip(years, percentage):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 15),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# 设置x轴刻度和标签
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title("SVC-2019-2021年女性综艺占比趋势", fontsize=14, fontweight="bold")

# 添加图例
ax.legend(loc='upper left')

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()