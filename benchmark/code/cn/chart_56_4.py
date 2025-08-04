import matplotlib.pyplot as plt
import numpy as np

# 数据
factors = ["商品质量", "商品价格", "品牌", "平台形象", "主播信用"]
percentages = [76.9, 64.1, 59.3, 42.5, 39.3]
colors = ["#a5d6a7"]  # 统一的绿色，可根据需要微调

# 创建画布
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制柱状图
bars = ax.barh(factors, percentages, color=colors*len(factors))

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=9, fontweight='bold')

# 美化设置
ax.set_title("直播电商用户消费决策构成因素", fontsize=12, fontweight='bold')
ax.set_xlabel("用户消费决策因素（%）", fontsize=10)
ax.set_xticks(np.arange(0, max(percentages)+10, 10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(["用户消费决策因素（%）"], loc='lower right')

plt.tight_layout()
plt.show()