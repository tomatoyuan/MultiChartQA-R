import matplotlib.pyplot as plt
import numpy as np

# --------------------- 左侧饼图数据 ---------------------
pie_labels = ["到店堂食为主", "线上外卖为主", "线下购买后带回家吃", "线上线下比例接近"]
pie_sizes = [32.5, 23.3, 23.5, 20.7]
pie_colors = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513"]

# --------------------- 右侧分组柱状图数据 ---------------------
bar_categories = ["30%以下（不含30%）", "30-40%（不含40%）", "40-50%（不含50%）", "50-80%（不含80%）", "80-100%"]
bar_values = [
    [32.2, 67.8],  # 第一组：橙色部分、浅色部分
    [43.8, 56.2], 
    [19.3, 80.7], 
    [3.4, 96.6], 
    [1.3, 98.7]
]
bar_colors = ["#FF7F50", "#FAF0E6"]  # 橙色、浅米色

# 创建画布，一行两列布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- 绘制左侧饼图 ---------------------
wedges, texts, autotexts = ax1.pie(pie_sizes, colors=pie_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023年中国居民夜间餐饮消费占比类型分布')
# 调整图例
ax1.legend(wedges, pie_labels, title="消费类型", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制右侧分组柱状图 ---------------------
x = np.arange(len(bar_categories))
bottom = np.zeros(len(bar_categories))
for i in range(2):
    ax2.bar(x, [val[i] for val in bar_values], bottom=bottom, color=bar_colors[i], label=pie_labels[i] if i==0 else '')
    bottom += [val[i] for val in bar_values]

ax2.set_title('2023年中国居民夜间餐饮消费占全天比例分布')
ax2.set_ylabel('占比（%）')
ax2.set_xticks(x)
ax2.set_xticklabels(bar_categories, rotation=45, ha='right')
ax2.legend(title="消费类型", loc="upper left")

# 添加分组柱状图数值标注
for i, (val1, val2) in enumerate(bar_values):
    ax2.text(i, val1/2, f'{val1}%', ha='center', va='center', color='white')
    ax2.text(i, val1 + val2/2, f'{val2}%', ha='center', va='center', color='black')

# 模拟黄色虚线框（前两组）
ax2.plot([x[0]-0.3, x[0]+0.3, x[0]+0.3, x[0]-0.3, x[0]-0.3], 
         [0, 0, 100, 100, 0], 
         linestyle='--', color='gold', linewidth=2)
ax2.plot([x[1]-0.3, x[1]+0.3, x[1]+0.3, x[1]-0.3, x[1]-0.3], 
         [0, 0, 100, 100, 0], 
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('2023年中国居民夜间餐饮消费占全天餐饮消费比例情况', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()