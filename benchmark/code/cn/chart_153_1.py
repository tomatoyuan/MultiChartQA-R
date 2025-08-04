# 图表1：关键词搜索笔记数据变化（柱状图 + 折线图双轴）

import matplotlib.pyplot as plt
import numpy as np

# 数据定义
categories = ["毛孔讨论问题", "毛孔粗大话题总量", "毛孔护理"]
old_values = [43.65, 8.7, 0.16]
new_values = [79.06, 17.95, 0.39]
growth_rates = [81.12, 106.32, 143.75]

x = np.arange(len(categories))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图
bars1 = ax1.bar(x - width/2, old_values, width, label='2022/08-2023/07', color='#c5d9de')
bars2 = ax1.bar(x + width/2, new_values, width, label='2023/08-2024/07', color='#355c5c')
ax1.set_ylabel('搜索笔记数量（万条）')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=10)
ax1.legend(loc='upper left')

# 添加柱子顶部数值
for bar in bars1 + bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}',
             ha='center', va='bottom', fontsize=9)

# 折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rates, color='gray', marker='o', label='同比增长率')
for i, rate in enumerate(growth_rates):
    ax2.text(x[i], rate + 3, f'{rate:.2f}%', color='black', ha='center', fontsize=9)
ax2.set_ylabel('同比增长率（%）')
ax2.set_ylim(0, 180)

# 标题与美化
plt.title("图1.1-1 小红书关键词搜索笔记数据（数据来源：飞瓜）")
plt.tight_layout()
plt.show()