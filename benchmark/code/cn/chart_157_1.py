import matplotlib.pyplot as plt
import numpy as np

# 各层标签及颜色（从下往上堆叠）
categories = ['不愿意多付溢价', '愿意多付5%以内', '愿意多付5%-10%', '愿意多付10%-20%', '愿意多付超过20%']
colors = ['#FF5C40', '#FF7B5C', '#FF9C80', '#FFBFA6', '#FFE3DC']

# 数据按堆叠顺序排列
green_total = [34, 34, 22, 9, 1]
food_drink = [30, 36, 22, 10, 2]

# 转置数据用于堆叠绘图
data = np.array([green_total, food_drink])
data_cum = data.cumsum(axis=1)

x = np.arange(data.shape[0])
width = 0.5

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制堆叠柱状图（从底部向上绘制）
for i in range(len(categories)):
    bottoms = data_cum[:, i - 1] if i > 0 else np.zeros_like(x)
    values = data[:, i]
    bars = ax.bar(x, values, width, bottom=bottoms, label=categories[i], color=colors[i])

    # 添加文本标签
    for j in range(len(x)):
        if values[j] > 3:  # 避免过小值重叠
            ax.text(x[j], bottoms[j] + values[j]/2, f'{values[j]}%', ha='center', va='center', fontsize=10, color='white')

# 设置标题和坐标
ax.set_xticks(x)
ax.set_xticklabels(['绿色消费意愿总览', '食品饮料'], fontsize=12)
ax.set_ylabel('占比（%）', fontsize=12)
ax.set_ylim(0, 105)
ax.set_title('中国消费者有一定的绿色溢价意愿', fontsize=16, weight='bold')

# 图例（顺序与图中堆叠一致）
ax.legend(loc='best', title='愿意支付溢价占比', fontsize=10, title_fontsize=11)

plt.tight_layout()
plt.show()