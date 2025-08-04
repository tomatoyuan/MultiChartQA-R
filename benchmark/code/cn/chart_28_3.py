import matplotlib.pyplot as plt
import numpy as np

# 数据定义
age_groups = ["19-24岁", "25-34岁", "18岁以下", "35-49岁", "50岁以上"]
age_percentages = [52, 41, 5, 2, 0]
age_colors = ['#4A7ABC', '#5EB95E', '#F37B1D', '#905CA9', '#E5E5E5']

# 创建画布
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# 绘制美化的饼图
wedges, texts = ax.pie(
    age_percentages,
    labels=None,
    autopct=None,
    startangle=90,
    colors=age_colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    pctdistance=0.8,
)

# 为饼图添加阴影效果
for w in wedges:
    w.set_alpha(0.9)
    w.set_zorder(1)

# 设置标题
ax.set_title("不同年龄层对双11的关注占比", fontsize=16, pad=25, 
              fontweight='bold', color='#333333')
ax.axis('equal')  # 保证饼图是圆的

# 优化标签位置计算，使用斜线+水平线样式
label_positions = []

for i, (wedge, group, percent) in enumerate(zip(wedges, age_groups, age_percentages)):
    if percent == 0:  # 跳过0%的部分
        continue
        
    # 获取楔形的角度
    ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    rad = np.deg2rad(ang)
    y = np.sin(rad)
    x = np.cos(rad)
    
    # 智能调整标签距离
    angle = wedge.theta2 - wedge.theta1
    base_radius = 1.25
    radius = base_radius + max(0, 0.3 - angle/180)
    
    # 计算斜线终点和水平线终点
    line1_length = 0.25
    line2_length = 0.4
    
    line1_end_x = x * (1 + line1_length)
    line1_end_y = y * (1 + line1_length)
    
    if x > 0:  # 右侧标签
        line2_end_x = line1_end_x + line2_length
        line2_end_y = line1_end_y
    else:  # 左侧标签
        line2_end_x = line1_end_x - line2_length
        line2_end_y = line1_end_y
    
    # 检查是否与已有标签重叠
    overlap = False
    label_pos = (line2_end_x, line2_end_y)
    
    for pos in label_positions:
        dist = np.sqrt((label_pos[0] - pos[0])**2 + (label_pos[1] - pos[1])**2)
        if dist < 0.3:
            overlap = True
            if x > 0:  # 右侧标签上移
                line1_end_y += 0.1
                line2_end_y += 0.1
            else:  # 左侧标签下移
                line1_end_y -= 0.1
                line2_end_y -= 0.1
            break
    
    label_positions.append(label_pos)
    
    # 绘制两段式连接线
    ax.plot([x, line1_end_x], [y, line1_end_y], color='#999999', linestyle='-', linewidth=1)
    ax.plot([line1_end_x, line2_end_x], [line1_end_y, line2_end_y], color='#999999', linestyle='-', linewidth=1)
    
    # 添加标签文本
    if x > 0:
        ax.text(line2_end_x + 0.05, line2_end_y, f"{group}: {percent}%", 
                ha='left', va='center', fontsize=11, backgroundcolor='white')
    else:
        ax.text(line2_end_x - 0.05, line2_end_y, f"{group}: {percent}%", 
                ha='right', va='center', fontsize=11, backgroundcolor='white')

# 调整布局
plt.tight_layout(pad=3)

# 保存图表（可选）
# plt.savefig('age_distribution.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()