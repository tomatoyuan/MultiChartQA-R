import matplotlib.pyplot as plt
import numpy as np

# 数据
expectations = [
    "产品效果持续时间长", "复合功效的产品", "促销/优惠力度加大", 
    "包装设计更美观、有创意", "价格亲民的产品", "更多新晋国产品牌", 
    "购买渠道增多，购买方便", "改善导购/销售的服务态度", "改善售后服务"
]
percentages = [61.1, 41.2, 40.9, 39.6, 31.0, 29.5, 28.7, 17.0, 10.4]

x = np.arange(len(expectations))

fig, ax = plt.subplots(figsize=(10, 7))

# 绘制柱状图
bars = ax.barh(x, percentages, color='orange')  # 水平柱状图更适合展示此类数据
ax.set_xlabel('期待占比（%）')
ax.set_ylabel('期待内容')
ax.set_yticks(x)
ax.set_yticklabels(expectations)
ax.invert_yaxis()  # 让第一个期待显示在最上方
ax.set_title('2023年中国消费者对化妆品行业发展的期待调查')

# 添加数值标注
for bar in bars:
    length = bar.get_width()
    ax.text(length + 1, bar.get_y() + bar.get_height() / 2, 
            f'{length}%', ha='left', va='center')

plt.tight_layout()
plt.show()