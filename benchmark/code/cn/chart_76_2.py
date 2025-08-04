import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# 单位新增活跃用户对应当期营销费用（元/人），数据大体一致即可
marketing_cost = [67.6, 100.1, 154.6, 251.6, 435.7, 298.1, 474.8, 572.3]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, marketing_cost, width=bar_width, color="#A4C639", label="当前营销费用/当前新增活跃用户数均值（元/人）")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 模拟绿色外边框
for spine in ax.spines.values():
    spine.set_color('#A4C639')
    spine.set_linewidth(2)

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("当前营销费用/当前新增活跃用户数均值（元/人）")
# 设置标题
ax.set_title("2014-2021年头部互联网上市公司单位新增活跃用户对应当期营销费用", fontsize=12, fontweight="bold")

# 添加图例
ax.legend(loc='upper left')

plt.tight_layout()  # 自动调整布局
plt.show()