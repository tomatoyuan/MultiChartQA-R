import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2023", "2024e", "2025e", "2026e", "2027e", "2028e"]
# 科技投入（亿元），大体模拟，可根据实际调整
tech_investment = [517.6, 586.7, 672.9, 771.3, 881.5, 1020.1]
# 增速（%），大体模拟，可根据实际调整
growth_rate = [13.4, 14.7, 14.6, 14.3, 15.7, 16.8]

x = np.arange(len(years))  # x轴刻度位置
bar_width = 0.5  # 柱状图宽度

fig, ax1 = plt.subplots(figsize=(14, 7))  # 进一步增大图表宽度

# 绘制科技投入柱状图
bars = ax1.bar(x, tech_investment, width=bar_width, label='科技投入 (亿元)', color='greenyellow')
ax1.set_ylabel('科技投入 (亿元)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)

# 为柱状图添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    # 最后一个标签位置特殊处理
    if i == len(bars) - 1:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(15, 10),  # 向右上方偏移
                    textcoords="offset points",
                    ha='left', va='bottom',  # 左对齐，底部对齐
                    fontsize=10)
    else:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 8),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

# 创建第二个y轴，绘制增速折线图
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_rate, marker='o', markersize=7, label='增速 (%)', 
                color='dodgerblue', linewidth=2)
ax2.set_ylabel('增速 (%)', fontsize=12)

# 为折线图添加数值标签
for i, rate in enumerate(growth_rate):
    # 最后一个标签位置特殊处理
    if i == len(growth_rate) - 1:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(15, -15),  # 向右下方偏移
                    textcoords="offset points",
                    ha='left', va='top',  # 左对齐，顶部对齐
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    else:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(-10, 10) if rate > 14.5 else (-10, -15),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# 添加标题
ax1.set_title('2023-2028年中国保险业科技投入', fontsize=14, pad=15)

# 合并图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=11)

# 美化图表
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # 添加水平网格线
plt.tight_layout()  # 自动调整布局

plt.show()