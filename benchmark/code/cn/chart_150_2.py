import matplotlib.pyplot as plt
import numpy as np

# 数据整理（按品类分组，每个品类包含各线城市的占比）
categories = [
    "餐饮套餐", "休闲娱乐", "酒店住宿", "旅游门票", 
    "出行旅游", "生活服务", "美容美护", "培训咨询"
]
# 各品类下，一线城市、新一线城市、二三线城市、四五线城市的占比（%）
data = {
    "餐饮套餐": [61.8, 59.9, 72.4, 69.2],
    "休闲娱乐": [56.6, 57.3, 58.6, 43.6],
    "酒店住宿": [42.6, 41.4, 30.9, 35.9],
    "旅游门票": [39.7, 49.7, 47.4, 20.5],
    "出行旅游": [39.0, 40.8, 42.1, 48.7],
    "生活服务": [36.8, 42.0, 48.7, 48.7],
    "美容美护": [31.6, 35.7, 33.6, 23.1],
    "培训咨询": [22.9, 21.3, 23.0, 15.4]
}
# 各线城市对应的颜色（与图例一致）
colors = ['coral', 'sandybrown', 'lightpink', 'gold']
# 各线城市标签
city_labels = ["一线城市", "新一线城市", "二三线城市", "四五线城市"]

x = np.arange(len(categories))  # x轴坐标（每个品类对应一个位置）
bar_width = 0.2  # 每个城市类型柱子的宽度

fig, ax = plt.subplots(figsize=(16, 8))

# 循环绘制每个城市类型的柱子
for i in range(4):
    ax.bar(
        x + i * bar_width,  # 控制柱子的x位置，实现分组
        [data[cat][i] for cat in categories],  # 取每个品类下第i个城市类型的占比
        width=bar_width,
        color=colors[i],
        label=city_labels[i]
    )

ax.set_title('2023年中国各线城市到店类服务用户消费品类调查', fontsize=14)
ax.set_ylabel('消费占比（%）')
ax.set_xlabel('消费品类')
ax.set_xticks(x + bar_width * 1.5)  # 调整x轴刻度位置，让标签在分组中间
ax.set_xticklabels(categories)
ax.legend(title='城市类型', loc='upper right')

# 添加数值标注
for i in range(len(categories)):
    for j in range(4):
        value = data[categories[i]][j]
        ax.text(
            x[i] + j * bar_width, 
            value + 1, 
            f'{value}%', 
            ha='center', 
            va='bottom', 
            color='black', 
            fontsize=9
        )

plt.tight_layout()
plt.show()