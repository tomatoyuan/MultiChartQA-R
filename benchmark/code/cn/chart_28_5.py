import matplotlib.pyplot as plt
import numpy as np

# 数据定义
genders = ["女生", "男生"]
gender_percents = [45, 55]
gender_colors = ['#FF7E79', '#7EB0D5']

# 创建画布
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# 绘制美化的水平分段条形图
bar_height = 0.4
ax.barh(0, gender_percents[0], color=gender_colors[0], 
         height=bar_height, edgecolor='white', linewidth=1.5, label=genders[0])
ax.barh(0, gender_percents[1], left=gender_percents[0], color=gender_colors[1], 
         height=bar_height, edgecolor='white', linewidth=1.5, label=genders[1])

# 添加数据标签
ax.text(gender_percents[0]/2, 0, f"{gender_percents[0]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')
ax.text(gender_percents[0] + gender_percents[1]/2, 0, f"{gender_percents[1]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# 设置条形图样式
ax.set_xlim(0, 100)
ax.set_yticks([])  # 移除y轴
ax.set_xlabel("占比 (%)", fontsize=12, labelpad=10)
ax.set_title("25-34岁男女对双11的关注占比", fontsize=14, pad=20, fontweight='bold')

# 自定义x轴刻度
ax.set_xticks([0, 25, 50, 75, 100])
ax.tick_params(axis='x', which='major', labelsize=10)

# 添加图例
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), 
           ncol=2, frameon=False, fontsize=12)

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.3)

# 添加边框
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# 在分界处添加斜线 - 男女区分线
divider_y = np.linspace(-bar_height/2, bar_height/2, 100)
divider_x = np.ones_like(divider_y) * gender_percents[0]
ax.plot(divider_x, divider_y, color='white', linewidth=1.5, linestyle='--')

# 调整布局
plt.tight_layout(pad=3)

# 保存图表（可选）
# plt.savefig('gender_distribution.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()