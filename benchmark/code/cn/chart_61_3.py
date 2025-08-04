import matplotlib.pyplot as plt
import numpy as np

# 数据定义
months = ["1月", "2月", "3月"]
years = ["2023年", "2024年", "2025年"]
data = [
    [67.3, 64.1, 62.9],
    [67.2, 64.9, 63.3],
    [69.7, 66.9, 63.4]
]
growth_rates = ["同比-1.9%", "同比-2.5%", "同比-5.1%"]
colors = ["#a5d65d", "#81c784", "#4bb7e6"]  # 匹配图表颜色

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制分组柱状图
x = np.arange(len(months))
bar_width = 0.25
for i in range(3):
    ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i], label=years[i], edgecolor='white')
    # 添加数据标注
    for j, val in enumerate(data[i]):
        ax.text(x[j] + i * bar_width, val -3, f'{val}', ha='center', va='bottom', fontsize=9)

# 添加同比注释
for i in range(3):
    ax.text(x[i] + 1 * bar_width, max(data[i]) + 2, growth_rates[i], ha='center', va='bottom', fontsize=10, color='blue')

# 美化设置
ax.set_title("mUserTracker-2023-2025Q1\n单机单日使用次数", fontsize=12, fontweight='bold')
ax.set_xticks(x + bar_width)
ax.set_xticklabels(months)
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()