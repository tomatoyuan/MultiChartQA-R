import matplotlib.pyplot as plt
import numpy as np

# --------------------- 左侧“购买频率”饼图数据 ---------------------
frequency_labels = [
    "基本上每天都喝", "一周3-4次", "一周1-2次", 
    "一月1-2次", "不固定", "极少"
]
frequency_sizes = [11.9, 29.5, 38.3, 7.9, 10.7, 1.7]  # 占比（%）
frequency_colors = ["coral", "gold", "green", "brown", "olive", "darkgreen"]

# --------------------- 右侧“喜欢的促销活动”横向柱状图数据 ---------------------
promotion_labels = [
    "开盖有奖", "第二瓶半价", "打折", "附赠小礼品"
]
promotion_proportions = [59.2, 55.8, 50.5, 44.8]  # 占比（%）
promotion_colors = ["coral"] * len(promotion_labels)  # 统一橙色

# --------------------- 创建画布（一行两列） ---------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- 绘制左侧“购买频率”饼图 ---------------------
wedges, texts, autotexts = ax1.pie(
    frequency_sizes, 
    colors=frequency_colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.8  # 调整标注位置，避免重叠
)
ax1.set_title('2023年中国消费者购买无糖饮料频率', fontsize=14)
# 调整图例位置（图外右侧）
ax1.legend(
    wedges, 
    frequency_labels, 
    title="购买频率", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)
# 优化标注文字颜色（深色切片用白色字，浅色用黑色字）
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制右侧“喜欢的促销活动”横向柱状图 ---------------------
x_promotion = np.arange(len(promotion_labels))
ax2.barh(x_promotion, promotion_proportions, color=promotion_colors)
ax2.set_title('2023年中国消费者喜欢的无糖饮料促销活动种类', fontsize=14)
ax2.set_xlabel('占比（%）')
ax2.set_ylabel('促销活动种类')
ax2.set_yticks(x_promotion)
ax2.set_yticklabels(promotion_labels)
ax2.set_xlim(0, 70)  # 调整x轴范围适配最大占比（59.2%）

# 添加右侧数值标注
for i, prop in enumerate(promotion_proportions):
    ax2.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# --------------------- 添加样本来源说明 ---------------------
fig.text(0.5, -0.05, '样本来源：草莓派数据调查与计算系统 (Strawberry Pie)', 
         fontsize=10, ha='center')

plt.tight_layout()
plt.show()