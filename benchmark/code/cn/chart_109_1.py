import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# 同比增速（%）
growth_rates = [30.4, 19.1, 8.9, 11.3, 3.6, 12.9, 6.4]

x = np.arange(len(years))  # x轴坐标

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制柱状图
bars = ax.bar(x, growth_rates, color='orange')

# 添加数值标注
for i, rate in enumerate(growth_rates):
    ax.text(i, rate + 1, f'{rate}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel('同比增速（%）')
ax.set_title('2018-2024年中国农村网络销售额同比增速变化')

plt.tight_layout()
plt.show()