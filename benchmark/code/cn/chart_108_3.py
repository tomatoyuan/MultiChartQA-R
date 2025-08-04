import matplotlib.pyplot as plt
import numpy as np

# 评价维度
dimensions = ["形式新颖", "实时更新", "内容丰富", "互动性强", "专业权威", 
              "独家报道", "数据支持", "国际化视野", "深度分析"]
# 各维度下不同评分（1-5分）的占比，按 5分、4分、3分、2分、1分 顺序
data = np.array([
    [29.82, 46.05, 14.04, 7.02, 3.07],
    [43.53, 32.89, 18.64, 3.51, 1.43],
    [36.62, 36.51, 16.89, 7.13, 2.85],
    [28.07, 35.20, 27.30, 7.46, 1.97],
    [35.64, 33.44, 21.60, 6.03, 3.29],
    [29.39, 38.93, 18.53, 11.61, 1.54],
    [38.05, 34.43, 18.53, 5.70, 3.29],
    [35.96, 37.39, 17.98, 6.92, 1.75],
    [35.96, 34.76, 20.18, 6.47, 2.63]
])

# 评分对应的颜色，与图表中的颜色对应
colors = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
scores = ["5分", "4分", "3分", "2分", "1分"]

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(dimensions))

for i in range(data.shape[1]):
    ax.bar(dimensions, data[:, i], bottom=bottom, color=colors[i], label=scores[i])
    # 添加数值标注
    for j in range(len(dimensions)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国财经新闻用户对财经媒体新闻的重要性评分')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()