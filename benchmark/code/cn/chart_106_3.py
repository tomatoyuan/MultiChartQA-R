import matplotlib.pyplot as plt
import numpy as np

# 品牌名称
brands = ["农夫山泉矿泉水", "娃哈哈矿泉水", "怡宝矿泉水", "百岁山矿泉水", "康师傅矿泉水", 
          "景田矿泉水", "可口可乐气泡矿泉水", "昆仑山矿泉水", "冰露矿泉水", "恒大冰泉矿泉水", 
          "法国依云矿泉水", "圣培露", "波兰泉"]
# 对应占比（%）
proportions = [48.53, 45.04, 36.73, 35.66, 29.49, 
               22.79, 22.25, 20.38, 20.11, 18.23, 
               14.75, 11.80, 10.72]

x = np.arange(len(brands))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(brands, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者最常购买的包装饮用水品牌')

plt.tight_layout()
plt.show()