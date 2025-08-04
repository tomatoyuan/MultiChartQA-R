import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# 国产品牌婴幼儿奶粉零售价格（元/斤），数据大体一致即可
domestic_prices = [166.3, 171.9, 179.8, 189.5, 204.3, 211.6]
# 国际品牌婴幼儿奶粉零售价格（元/斤），数据大体一致即可
international_prices = [214.3, 220.7, 228.0, 235.5, 250.5, 257.8]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制国产品牌价格折线图
domestic_line, = ax.plot(years, domestic_prices, marker='o', color="#A4C639", label="国产品牌婴幼儿奶粉（元/斤）", linewidth=2)
# 绘制国际品牌价格折线图
international_line, = ax.plot(years, international_prices, marker='o', color="#64B5F6", label="国际品牌婴幼儿奶粉（元/斤）", linewidth=2)

# 添加国产品牌数据标注
for x, y in zip(years, domestic_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加国际品牌数据标注
for x, y in zip(years, international_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# 设置y轴标签
ax.set_ylabel("零售价格（元/斤）")
# 设置标题
ax.set_title("2016-2021年中国婴幼儿奶粉零售价格变化趋势", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()