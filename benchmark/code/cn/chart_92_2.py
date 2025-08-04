import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2016, 2017, 2018, 2019, 2020, 2021]
# 新能源汽车产量（万辆，模拟数据 ）
production = [52, 79, 127, 124, 137, 355]
# 增速（%，模拟数据 ）
growth_rates = [53.6, 59.9, -2.2, 10.0, 159.5]  # 注意：2016 年无增速（对比前一年），这里按图中数据逻辑，从 2017 开始有增速点

# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 700)

# 绘制柱状图（产量 ）
ax1.bar(years, production, color="#A4C639", label="产量（万辆）")
ax1.set_ylabel("产量（万辆）", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# 创建次坐标轴绘制折线图（增速 ）
ax2 = ax1.twinx()

ax2.set_ylim(-100, 200)

# 折线图的 x 轴取 2017-2021（对应增速数据点 ），与原图一致
ax2.plot(years[1:], growth_rates, marker='o', color="#87CEEB", label="增速（%）", linewidth=2)
ax2.set_ylabel("增速（%）", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# 添加柱状图数据标注
for x, y in zip(years, production):
    ax1.annotate(f'{y}',
                xy=(x, y),
                xytext=(0, 3),  # 标注位置微调
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加折线图数据标注（注意：只标注 2017-2021 ）
for x, y in zip(years[1:], growth_rates):
    ax2.annotate(f'{y}%',
                xy=(x, y),
                xytext=(-2, 15),  # 标注位置微调
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# 设置 x 轴刻度
ax1.set_xticks(years)
# 设置标题
ax1.set_title("2016-2021年中国新能源汽车产量", fontsize=14, fontweight="bold")

# 合并图例（注意：折线图从 2017 开始，需调整图例显示 ）
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()