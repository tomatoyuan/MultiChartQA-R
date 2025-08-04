import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2015, 2022)
# 线上健身渗透率（%），数据大体一致即可
penetration = [0.0, 0.8, 17.5, 21.7, 33.2, 42.7, 45.5]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制折线图
line, = ax.plot(years, penetration, marker='o', color="#A4C639", label="我国线上健身渗透率（%）", linewidth=2)

# 添加数据标注
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 设置x轴刻度和标签
ax.set_xticks(years)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("渗透率（%）")
# 设置标题
ax.set_title("2015-2021年中国线上健身渗透率", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()