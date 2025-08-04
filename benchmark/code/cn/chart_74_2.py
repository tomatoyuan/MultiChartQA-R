import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# 数字经济增速（%），数据大体一致即可
digital_economy_growth = [18.9, 20.3, 20.9, 15.6, 9.7, 16.2]
# GDP增速（%），数据大体一致即可
gdp_growth = [6.8, 6.9, 6.7, 6.0, 2.2, 8.1]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制数字经济增速折线图
digital_line, = ax.plot(years, digital_economy_growth, marker='o', color="#A4C639", label="数字经济增速（%）", linewidth=2)
# 绘制GDP增速折线图
gdp_line, = ax.plot(years, gdp_growth, marker='o', color="#64B5F6", label="GDP增速（%）", linewidth=2)

# 添加数字经济增速数据标注
for x, y in zip(years, digital_economy_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加GDP增速数据标注
for x, y in zip(years, gdp_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# 设置y轴标签
ax.set_ylabel("增速（%）")
# 设置标题
ax.set_title("2016-2021年中国数字经济增速与GDP增速", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()