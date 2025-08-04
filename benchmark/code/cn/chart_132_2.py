import matplotlib.pyplot as plt
import numpy as np

# 企业类型
categories = ["国有企业", "国家机关", "民营企业", "三资企业", "事业单位"]
# 各届占比（2021届、2022届、2023届 ）
percentages_2021 = [42.5, 11.4, 19.0, 11.2, 13.2]
percentages_2022 = [44.4, 9.4, 17.4, 11.9, 14.7]
percentages_2023 = [46.7, 12.5, 12.6, 14.6, 12.3]

x = np.arange(len(categories))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))

# 绘制 2021 届（橙色）、2022 届（黄色）、2023 届（绿色）柱状图
bar_2021 = ax.bar(x - width, percentages_2021, width, color='coral', label='2021届')
bar_2022 = ax.bar(x, percentages_2022, width, color='gold', label='2022届')
bar_2023 = ax.bar(x + width, percentages_2023, width, color='green', label='2023届')

# 添加数值标注
for bars in [bar_2021, bar_2022, bar_2023]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', ha='center', va='bottom')

ax.set_ylabel('占比（%）')
ax.set_xlabel('企业类型')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_title('2021-2023年中国应届生期望就业企业类型')

plt.tight_layout()
plt.show()