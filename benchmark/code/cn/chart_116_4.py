import matplotlib.pyplot as plt
import numpy as np

# 电商平台名称
platforms = ["拼多多", "天猫/淘宝", "京东", "苏宁易购", "聚划算", "京喜", "苏宁拼购", 
             "盒马鲜生", "每日优鲜", "抖音", "快手"]
# 各评分（5分、4分、3分、2分、1分 ）占比，按平台顺序，每个平台对应一个子列表
data = np.array([
    [24.72, 42.16, 22.62, 7.11, 3.39],
    [38.13, 29.56, 23.26, 7.27, 1.78],
    [32.96, 36.03, 16.31, 12.12, 2.58],
    [25.85, 33.12, 23.75, 13.73, 3.55],
    [25.69, 37.96, 23.10, 9.05, 4.20],
    [28.76, 34.57, 22.77, 10.02, 3.88],
    [25.85, 39.10, 21.00, 11.47, 2.58],
    [29.24, 38.77, 21.65, 7.59, 2.73],
    [28.59, 37.96, 21.82, 9.05, 2.58],
    [27.63, 39.74, 22.78, 6.46, 3.39],
    [29.56, 36.19, 21.81, 9.37, 3.07]
])
# 评分对应颜色
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
scores = ["5分", "4分", "3分", "2分", "1分"]

fig, ax = plt.subplots(figsize=(14, 8))
bottom = np.zeros(len(platforms))

for i in range(data.shape[1]):
    ax.bar(platforms, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # 添加数值标注，在每个堆积块中间位置
    for j in range(len(platforms)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', 
                ha='center', va='center', fontsize=7)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者对各电商平台购买农货产品时总体体验满意情况')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()