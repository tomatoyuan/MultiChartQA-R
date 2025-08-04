import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2015, 2024)
# 市场渗透率（%），数据大体一致即可
penetration = [51.6, 55.6, 59.6, 63.9, 72.2, 77.1, 82.0, 85.2, 88.6]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
line, = ax.plot(years, penetration, marker='o', color="#C63982", label="渗透率（%）", linewidth=2)

# 添加数据标注
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C63982")

# 设置x轴刻度和标签
ax.set_xticks(years)
ax.set_xticklabels([f"{year}" for year in years])
# 设置y轴标签
ax.set_ylabel("渗透率（%）")
# 设置标题
ax.set_title("2015-2023年中国婴儿纸尿裤市场渗透率及预测", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()