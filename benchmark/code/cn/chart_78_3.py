import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2001, 2022)
# 香港职位空缺数量（万个），数据大体一致即可
vacancies = [1.7, 1.6, 2.1, 2.9, 3.7, 3.9, 4.8, 3.2, 3.5, 4.8, 5.5, 6.5, 7.2, 7.4, 7.1, 6.7, 7.4, 7.8, 5.4, 3.5, 6.1]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
line, = ax.plot(years, vacancies, marker='o', color="#39C6BA", label="香港职位空缺数量（万个）", linewidth=2)

# 添加数据标注
for x, y in zip(years, vacancies):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#39C6BA")

# 设置x轴刻度和标签
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
# 设置y轴标签
ax.set_ylabel("香港职位空缺数量（万个）")
# 设置标题
ax.set_title("2001-2021年香港职位空缺数量", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()