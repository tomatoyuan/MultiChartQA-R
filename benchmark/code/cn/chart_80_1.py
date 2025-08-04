import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e"]
# 市场规模（亿元），数据大体一致即可
market_size = [352, 481, 549, 555, 499, 486, 530, 555, 628]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#C63982", label="市场规模（亿元）")

# 添加数据标注
for bar in bars:
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
ax.set_ylabel("市场规模（亿元）")
# 设置标题
ax.set_title("2015-2023年中国婴儿纸尿裤市场规模及预测", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()