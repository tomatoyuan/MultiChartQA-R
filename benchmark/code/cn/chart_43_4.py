import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["影音设备（智能音响、智能耳机）", "电子教育类（学习机等）", "电脑硬件/显示器/电脑周边", 
              "摄影摄像产品", "游戏机及配件（switch、PS等）", "从没购买过"]
percentages = [51.1, 36.4, 34.2, 23.0, 17.5, 13.1]

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制条形图
bars = ax.bar(categories, percentages, color='cyan')

# 设置标题和标签
ax.set_title('近一年购买各类数码3C产品的女性人数占比')
ax.set_ylabel('占比（%）')

# 旋转x轴标签，避免重叠
plt.xticks(rotation=45, ha='right')

# 在每个条形上方添加数值标注
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{percentage}%', ha='center', va='bottom')

# 显示图形
plt.tight_layout()
plt.show()