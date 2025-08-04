import matplotlib.pyplot as plt
import numpy as np

# 年份及日期
years = ["2019年4-9月", "2020年4-9月", "2021年4-9月", "2022年4-9月", "2023年4-9月"]
# 各品类占比（%），按 [珠宝镶嵌/铂金/K金首饰, 黄金首饰及产品, 钟表] 顺序
category_proportions = np.array([
    [29.1, 64.5, 6.4],
    [30.1, 60.9, 9.0],
    [22.6, 70.7, 6.7],
    [19.1, 75.6, 5.3],
    [14.7, 80.1, 5.2]
])

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制堆积柱状图
bottom = np.zeros(len(years))
for i in range(category_proportions.shape[1]):
    ax.bar(x, category_proportions[:, i], bottom=bottom, width=0.6, label=['珠宝镶嵌/铂金/K金首饰', '黄金首饰及产品', '钟表'][i])
    # 添加数值标注
    for j in range(len(years)):
        ax.text(j, bottom[j] + category_proportions[j, i] / 2, f'{category_proportions[j, i]}%', ha='center', va='center')
    bottom += category_proportions[:, i]

ax.set_ylabel('占比（%）')
ax.set_xlabel('日期')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2019-2023年半年度报告期周大福产品品类营业额占比')

plt.tight_layout()
plt.show()