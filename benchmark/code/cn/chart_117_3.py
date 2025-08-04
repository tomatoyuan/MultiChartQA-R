import matplotlib.pyplot as plt
import numpy as np

# 购买途径
channels = [
    "专业家居市场/家居城", "品牌专卖店", "网上购买", "朋友/家人推荐或转让", 
    "设计师或他人包办", "家居博览会", "二手市场/闲置交易平台", "商场", "工厂提货"
]
# 对应占比（%）
proportions = [37.70, 36.98, 35.19, 34.29, 33.57, 32.14, 28.19, 28.19, 24.24]

x = np.arange(len(channels))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者购买硬装家居产品的途径')

plt.tight_layout()
plt.show()