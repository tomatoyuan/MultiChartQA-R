import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# 中国融资规模（亿元），数据大体一致即可
china = [0, 0, 0, 0, 0, 0, 0, 10, 30, 0]  # 示例数据，可根据实际调整
# 海外融资规模（亿元），数据大体一致即可
overseas = [1, 10, 7, 21, 11, 31, 55, 71, 277, 75]  # 示例数据，可根据实际调整

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制分组柱状图（中国和海外叠加）
x = np.arange(len(years))
bar_width = 0.6
# 先绘制海外（蓝色）
overseas_bars = ax.bar(x, overseas, width=bar_width, color="#64B5F6", label="海外融资规模（亿元）")
# 再绘制中国（绿色，在海外上方叠加）
china_bars = ax.bar(x, china, width=bar_width, color="#C68439", label="中国融资规模（亿元）")

# 添加数据标注（海外）
for bar in overseas_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加数据标注（中国）
for bar in china_bars:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 标注位置调整
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='white')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("融资规模（亿元）")
# 设置标题
ax.set_title("2013-2022年上半年全球企业数字化学习行业融资规模", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()