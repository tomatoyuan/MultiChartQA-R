import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
# 市场规模（亿美元），2023 - 2025 为预测值（E）
market_size = np.array([2011, 1787, 2071, 2293, 2470, 2566, 2667])
# 为预测年份（2023 - 2025）标记特殊颜色
colors = ['green'] * 4 + ['orange'] * 3

plt.figure(figsize=(10, 6))  # 设置图表大小
bars = plt.bar(years, market_size, color=colors)

# 在每个柱子上方添加数值标注
for bar, value in zip(bars, market_size):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 15,
             f'{value}', ha='center', va='bottom', fontsize=10)

# 添加标题和坐标轴标签
plt.title('2019 - 2025年全球茶叶市场规模及预测', fontsize=14)
plt.xlabel('年份', fontsize=12)
plt.ylabel('市场规模（亿美元）', fontsize=12)

# 设置x轴刻度为年份
plt.xticks(years)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图表
plt.tight_layout()  # 调整布局
plt.show()