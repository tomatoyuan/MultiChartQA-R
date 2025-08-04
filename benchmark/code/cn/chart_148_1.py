import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# --------------------- 数据准备 ---------------------
# 性别分布
gender_labels = ["女性", "男性"]
gender_sizes = [60, 40]
gender_colors = ["pink", "lightblue"]

# 年龄分布
age_labels = ["21岁及以下", "22-30岁", "31-40岁", "41-50岁", "51-59岁", "60岁及以上"]
age_sizes = [4.0, 35.5, 46.6, 10.9, 2.4, 0.6]
age_colors = ["coral", "gold", "green", "brown", "gray", "olive"]

# 月收入分布
income_labels = ["5000元及以下", "5001-10000元", "10001-15000元", "15001-20000元", 
                 "20001-25000元", "25001-30000元", "30000元以上"]
income_sizes = [20.0, 37.2, 26.5, 10.2, 2.9, 1.3, 1.9]
income_colors = ["sienna", "orange", "darkorange", "coral", "lightcoral", "pink", "palevioletred"]

# --------------------- 创建画布 ---------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

# --------------------- 绘制性别分布（方块形式） ---------------------
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 20)
ax1.axis('off')  # 隐藏坐标轴

# 绘制女性方块
female_blocks = int(gender_sizes[0] / 2)  # 每个方块代表2%
for i in range(female_blocks):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=gender_colors[0]))

# 绘制男性方块
male_blocks = int(gender_sizes[1] / 2)
for i in range(male_blocks):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=gender_colors[1], alpha=0.8))

# 添加性别标签和占比
ax1.text(10, 2, f"{gender_labels[0]}: {gender_sizes[0]}%", fontsize=12, ha='center')
ax1.text(10 + gender_sizes[0], 2, f"{gender_labels[1]}: {gender_sizes[1]}%", fontsize=12, ha='center')

ax1.set_title('性别分布', fontsize=14)

# --------------------- 绘制年龄分布饼图 ---------------------
wedges, texts, autotexts = ax2.pie(age_sizes, colors=age_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('年龄分布', fontsize=14)
ax2.legend(wedges, age_labels, title="年龄区间", loc="center left", bbox_to_anchor=(1, 0.5))

# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制月收入分布饼图 ---------------------
wedges, texts, autotexts = ax3.pie(income_sizes, colors=income_colors, autopct='%1.1f%%', startangle=90)
ax3.set_title('月收入分布', fontsize=14)
ax3.legend(wedges, income_labels, title="收入区间", loc="center left", bbox_to_anchor=(1, 0.5))

# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('中国无糖饮料消费者画像：性别/年龄/收入', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()