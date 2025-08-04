import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 性别分布数据
gender_labels = ["男性", "女性"]
gender_sizes = [32.2, 67.8]
gender_colors = ["#6495ED", "#FFA07A"]

# 年龄分布数据
age_categories = ["15-25岁", "26-29岁", "31-40岁", "41-50岁", "51-55岁", "56-60岁", "其他"]
age_proportions = [13.8, 34.1, 31.5, 13.1, 5.4, 1.7, 0.4]
age_colors = ["#FFD700", "#FF7F50", "#FF7F50", "#FFD700", "#FFD700", "#FFD700", "#D3D3D3"]

# 婚姻状况数据
marital_labels = ["未婚", "已婚未育", "已婚已育"]
marital_sizes = [18.1, 14.4, 67.5]
marital_colors = ["#FFD700", "#32CD32", "#FF7F50"]

# 创建画布，3 个子图
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# 左侧：性别分布（用自定义图标 + 文本，近似模拟）
# 绘制男性图标（简化为蓝色人形）
male_x, male_y = 0.2, 0.5
male_width, male_height = 0.2, 0.4
ax1.add_patch(plt.Rectangle((male_x, male_y - male_height / 2), male_width, male_height, color=gender_colors[0]))
ax1.add_patch(plt.Circle((male_x + male_width / 2, male_y + 0.1), 0.05, color=gender_colors[0]))
ax1.text(male_x + male_width / 2, male_y - 0.3, f'{gender_labels[0]}, {gender_sizes[0]}%', ha='center', va='top')

# 绘制女性图标（简化为橙色人形）
female_x, female_y = 0.6, 0.5
female_width, female_height = 0.2, 0.4
ax1.add_patch(plt.Rectangle((female_x, female_y - female_height / 2), female_width, female_height, color=gender_colors[1]))
ax1.add_patch(plt.Circle((female_x + female_width / 2, female_y + 0.1), 0.05, color=gender_colors[1]))
ax1.text(female_x + female_width / 2, female_y - 0.3, f'{gender_labels[1]}, {gender_sizes[1]}%', ha='center', va='top')

ax1.axis('off')
ax1.set_title('2024年中国消费者性别分布')

# 中间：年龄分布柱状图
ax2.bar(age_categories, age_proportions, color=age_colors)
ax2.set_ylabel('占比（%）')
ax2.set_title('2024年中国消费者年龄分布')
# 添加数值标注
for i, prop in enumerate(age_proportions):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')

# 右侧：婚姻状况饼图
wedges, autotexts = ax3.pie(marital_sizes, colors=marital_colors, startangle=90)
ax3.legend(wedges, marital_labels, loc='lower left')
# 调整标注位置，显示百分比
for autotext in autotexts:
    autotext.set_color('white')
ax3.set_title('2024年中国消费者婚姻状况')

plt.tight_layout()
plt.show()