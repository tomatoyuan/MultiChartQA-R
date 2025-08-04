import matplotlib.pyplot as plt
import numpy as np

# 各项因素
factors = ["外观", "售后服务", "质量", "品牌与信誉度", "稀有度", "价格"]
# 各评分（1-5分）的占比，按 5分、4分、3分、2分、1分 顺序
data = np.array([
    [30.79, 21.06, 17.59, 16.67, 13.89],
    [28.94, 24.31, 21.05, 15.28, 10.42],
    [27.08, 26.85, 18.06, 15.51, 12.50],
    [25.93, 28.70, 18.29, 14.81, 12.27],
    [23.61, 30.56, 18.52, 14.58, 12.73],
    [17.59, 29.40, 21.30, 16.20, 15.51]
])

# 评分对应的颜色，与图表中的颜色对应
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
scores = ["5分", "4分", "3分", "2分", "1分"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(factors))

for i in range(data.shape[1]):
    ax.bar(factors, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # 添加数值标注
    for j in range(len(factors)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国手办消费者对手办各项因素的评分情况')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()