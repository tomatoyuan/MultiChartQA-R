import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 营业成本（亿元）
operating_cost = [17343.1, 17790.9, 17198.7, 16446.5, 18463.0, 20525.4, 21906.8]
# 营业收入（亿元）
operating_revenue = [14610.8, 15107.0, 14788.1, 14240.7, 16142.4, 17716.5, 21442.0]
# 营收增长率（%）
revenue_growth = [15.8, 3.4, -2.1, -3.7, 13.4, 9.8, 23.7]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# 绘制营业成本（黄色虚线框模拟，先画成本的背景框）
for i in range(len(years)):
    # 绘制黄色虚线矩形框
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, operating_cost[i], fill=False, edgecolor='gold', linestyle='--', linewidth=2)
    ax.add_patch(rect)
    # 标注营业成本数值
    ax.text(x[i], operating_cost[i] + 500, f'{operating_cost[i]}', ha='center', va='bottom')

# 绘制营业收入柱状图
bars = ax.bar(x, operating_revenue, color='blue', label='营业收入（亿元）', width=0.4)
# 标注营业收入数值
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 500, f'{rev}', ha='center', va='bottom')

# 绘制营收增长率环形标注（近似模拟，用文本在上方显示）
for i, growth in enumerate(revenue_growth):
    # 环形标注位置在柱子上方，用圆形背景突出（简化处理）
    circle = plt.Circle((x[i], operating_revenue[i] + 2000), 0.3, color='lightcoral', alpha=0.3)
    ax.add_artist(circle)
    ax.text(x[i], operating_revenue[i] + 1500, f'{growth}%', ha='center', va='center', fontsize=12, color='red')

ax.set_ylabel('金额（亿元）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2017-2023年中国A股新能源汽车整车制造上市公司营收及成本')

plt.ylim(0, max(operating_cost) + 3000)  # 调整 y 轴范围容纳标注
plt.tight_layout()
plt.show()