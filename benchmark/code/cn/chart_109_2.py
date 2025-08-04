import matplotlib.pyplot as plt
import numpy as np

# 平台名称
platforms = ["抖音网店", "淘宝", "拼多多", "快手网店", "京东", "小红书", "社区团购", 
             "每日优鲜", "天猫", "唯品会", "苏宁易购", "微信视频号"]
# 对应占比（%）
proportions = [29.79, 25.00, 24.73, 24.20, 24.20, 23.14, 23.14, 23.14, 23.14, 20.74, 20.74, 19.95]

x = np.arange(len(platforms))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(platforms, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国农村电商经营者销售商品常用平台')

plt.tight_layout()
plt.show()