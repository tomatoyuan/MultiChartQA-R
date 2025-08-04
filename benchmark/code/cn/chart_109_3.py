import matplotlib.pyplot as plt
import numpy as np

# 商品类型
product_types = ["手工业商品", "衣服、鞋帽等", "工农生产用具（如：镰刀、锄头、机械设备等）", 
                 "家用电器（如：手机、电脑、冰箱、彩电等）", "日用百货（如：纸品清洁、家居收纳、美容护肤等）", 
                 "食品生鲜（如：粮油、水果、酒水饮料、零食等）"]
# 对应占比（%）
proportions = [23.94, 27.39, 38.83, 39.10, 41.76, 50.53]

y = np.arange(len(product_types))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(product_types)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国农村电商经营者销售商品类型')

plt.tight_layout()
plt.show()