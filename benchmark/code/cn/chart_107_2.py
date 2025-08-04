import matplotlib.pyplot as plt
import numpy as np

# 考虑因素
factors = ["他人评价", "家庭共享计划", "价格", "客户服务质量", "隐私保护和安全性", "通话质量", 
           "可选套餐类型及数量", "网络覆盖率", "信号、网速", "增值服务（短号、视频会员、宽带等）", 
           "数据流量政策（流量不清零、流量转赠等）"]
# 对应占比（%）
proportions = [17.88, 21.73, 24.84, 26.45, 26.87, 27.41, 
               29.34, 30.73, 32.66, 32.87, 34.26]

y = np.arange(len(factors))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 7))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(factors)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国用户选择通信运营商时主要考虑因素')

plt.tight_layout()
plt.show()