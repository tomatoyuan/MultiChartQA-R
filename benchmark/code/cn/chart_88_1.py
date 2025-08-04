import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2000, 2005, 2010, 2014, 2020]
# 成人肥胖率（%），数据与图表一致
obesity_rates = [7.0, 8.0, 9.9, 10.5, 14.6]
# 成人超重率（%），数据与图表一致
overweight_rates = [22.8, 29.1, 32.1, 32.7, 35.0]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制折线图（成人超重率，绿色）
overweight_line, = ax.plot(years, overweight_rates, marker='o', color="#A4C639", label="成人超重率（%）", linewidth=2)
# 绘制折线图（成人肥胖率，蓝色）
obesity_line, = ax.plot(years, obesity_rates, marker='o', color="#87CEEB", label="成人肥胖率（%）", linewidth=2)

# 添加数据标注（成人超重率）
for x, y in zip(years, overweight_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加数据标注（成人肥胖率）
for x, y in zip(years, obesity_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# 设置x轴刻度和标签
ax.set_xticks(years)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("率（%）")
# 设置标题
ax.set_title("2000-2020年中国成人肥胖率和超重率", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()