import matplotlib.pyplot as plt
import numpy as np

# 体检服务指标
indicators = ["体检预约的方便性", "体检报告内容的专业性和完整性", "获取体检报告的时间", 
              "等候体检的时间", "体检场所的环境", "体检中心内的设备", "体检时问题响应速度和解决速度"]
# 各评分（5分、4分、3分、2分、1分）占比，按指标顺序，每个指标对应一个子列表
data = np.array([
    [33.39, 38.66, 19.60, 7.08, 1.27],
    [32.85, 38.66, 18.15, 8.53, 1.81],
    [31.58, 31.94, 21.78, 13.07, 1.63],
    [26.50, 35.93, 25.59, 9.98, 2.00],
    [32.49, 41.38, 17.06, 7.44, 1.63],
    [41.74, 38.11, 15.98, 3.60, 0.54],
    [28.31, 45.01, 14.34, 9.44, 2.90]
])
# 评分对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
scores = ["5分", "4分", "3分", "2分", "1分"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(indicators))

for i in range(data.shape[1]):
    ax.bar(indicators, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # 添加数值标注，在每个堆积块中间位置
    for j in range(len(indicators)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', 
                ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者对体检服务各项指标满意度评分')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()