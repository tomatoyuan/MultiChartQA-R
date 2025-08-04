import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['低饱和度口红', '细闪眼影', '粉红色眼影', '斩男香水', '秋冬面膜', '家用美容仪']
trade_growth = [39.5, 22.7, 323.2, 4.4, 382.8, 151.7]
payment_growth = [32.7, 22.2, 20.0, 168.1, 163.0, 32.1]

x = np.arange(len(categories))
width = 0.35

# 绘图
fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, trade_growth, width, label='交易指数增长率', color='orange')
bars2 = ax.bar(x + width/2, payment_growth, width, label='支付转化增长率', color='orangered')

# 文字设置
ax.set_ylabel('增长率（%）')
ax.set_title('淘内相关品类搜索&交易数据')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=30)
ax.legend()

# 添加数据标签
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()