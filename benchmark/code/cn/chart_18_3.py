import matplotlib.pyplot as plt
import numpy as np

# 城市名称
cities = ["成都", "武汉", "苏州", "南京", "天津", "广州", "杭州", "上海", "北京", "深圳"]
# 结婚成本（单位：万元）
costs = [55, 65, 94, 102, 108, 128, 178, 200, 202, 208]

x = np.arange(len(cities))  # 用于设置柱状图 x 轴的位置

# 创建画布和轴对象
fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图，设置颜色为白色，边框为粉色
bars = ax.bar(x, costs, color='white', edgecolor='pink')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(cities)
# 设置 y 轴标签
ax.set_ylabel("结婚成本（万元）")
# 设置标题
ax.set_title("全国各城市结婚成本 top10")
# 设置单位显示在标题旁
ax.text(0.95, 1.02, "单位：万元", transform=ax.transAxes, ha='right', va='bottom')

# 在每个柱子上标注数值
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}',
            ha='center', va='bottom')

# 设置背景颜色为粉色
ax.set_facecolor('pink')
# 去除顶部和右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.show()