import matplotlib.pyplot as plt
import numpy as np

# 满意度维度
dimensions = ["品牌知名度", "代言人/广告宣传", "口感", "饮品成分与功效", "产品种类/差异性", "价格", "促销活动", 
              "购买便利", "售后服务", "外观设计", "卫生质量", "营销方式（IP联名/体验式消费等活动）"]
# 各维度下不同评分（1-5分）的占比，按 5分、4分、3分、2分、1分 顺序
data = np.array([
    [41.55, 43.16, 10.04, 5.36, 1.39],
    [32.98, 34.32, 24.13, 7.50, 1.07],
    [40.48, 37.80, 14.48, 4.58, 2.68],
    [33.51, 39.14, 17.43, 6.43, 3.49],
    [32.71, 36.19, 21.98, 7.24, 1.88],
    [26.27, 42.63, 20.64, 7.77, 2.69],
    [32.17, 36.46, 19.64, 8.85, 2.88],
    [28.95, 35.12, 20.65, 10.99, 4.29],
    [28.69, 33.24, 24.93, 9.12, 4.02],
    [32.98, 42.09, 17.43, 5.36, 2.18],
    [38.61, 36.73, 16.89, 4.03, 3.79],
    [29.49, 34.85, 25.21, 8.31, 2.16]
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
ax.set_title('2025年中国消费者对目前市场上包装饮用水满意度评分')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()