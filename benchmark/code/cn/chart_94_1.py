import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e"]
# 市场规模（万亿元）
market_size = [3, 3, 4, 4, 4, 5, 4, 5, 5, 6]
# 同比增长率（%）
growth_rate = [11.7, 10.8, 10.7, 7.7, 9.4, -15.4, 18.9, 14.2, 12.4]
# 阶段划分
stages = ["平稳增长期"] * 5 + ["低谷期"] + ["恢复期"] + ["新活力期"] * 2
stage_x = [0, 4, 5, 6, 7, 9]  # 用于绘制阶段背景的x坐标边界，需与年份数量匹配，这里简单示例，可细化
stage_y = [-0.5] * len(stage_x)
stage_height = [1] * len(stage_x)
stage_colors = ["#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD"]  # 模拟阶段颜色

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图（市场规模）
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#A4C639", label="中国餐饮市场规模（万亿元）")

# 绘制折线图（同比增长率）
ax2 = ax.twinx()
ax2.plot(x[:-1], growth_rate, marker='o', color="#87CEEB", label="同比增长率（%）", linewidth=2)  # 增长率数据比年份少一个，注意切片

# 添加市场规模标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加增长率标注
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%',
                 xy=(x[i], rate),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# 绘制阶段背景（简易模拟，如需精准位置需细化坐标）
for i in range(len(stages)):
    ax.axvspan(i, i + 1, facecolor=stage_colors[i], alpha=0.3)

# 手动添加阶段文本（因自动布局复杂，这里简易放置，可根据实际调整）
stage_texts = ["平稳增长期", "低谷期", "恢复期", "新活力期"]
ax.text(2, -0.5, stage_texts[0], ha='center', va='top', fontweight='bold')
ax.text(5.5, -0.5, stage_texts[1], ha='center', va='top', fontweight='bold')
ax.text(6.5, -0.5, stage_texts[2], ha='center', va='top', fontweight='bold')
ax.text(8, -0.5, stage_texts[3], ha='center', va='top', fontweight='bold')

# 设置x轴刻度
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴（市场规模）范围
ax.set_ylim(0, 7)
# 设置标题
ax.set_title("2014-2023年中国餐饮市场规模", fontsize=14, fontweight="bold")

# 合并图例
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()