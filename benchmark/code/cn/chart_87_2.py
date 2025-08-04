import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["最低标准", "6-9岁", "10-13岁", "14-17岁"]
# 数据（min），与图表对应
data = [120, 64.3, 55.5, 44.9]
# 各类别中达到平均的部分（示意值，匹配图表视觉效果）
avg_parts = [120, 30, 25, 20]  
# 颜色设置
colors = ["#A4C639", "#D3D3D3", "#D3D3D3", "#D3D3D3"]  
avg_line_y = 54.9  # 平均时长

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
for i in range(len(categories)):
    # 绘制底部（灰色或绿色）
    rect = ax.bar(x[i], data[i], width=bar_width, color=colors[i])
    # 绘制顶部覆盖的“平均部分”（仅最低标准不需要覆盖，因为它本身就是绿色且超过平均）
    if categories[i] != "最低标准":
        ax.bar(x[i], data[i] - avg_parts[i], bottom=avg_parts[i], width=bar_width, color=colors[0])
    # 添加数据标注
    ax.text(x[i], data[i] + 2, f'{data[i]}min', ha='center', va='bottom', color='black')

# 绘制平均时长的黄色虚线
ax.axhline(y=avg_line_y, color='yellow', linestyle='--', linewidth=2)
ax.text(3.2, avg_line_y + 2, f'平均 {avg_line_y}min', ha='left', va='bottom', color='gold', fontweight='bold')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title('2018年中国儿童青少年的户外运动情况', fontsize=14, fontweight='bold')

# 美化：隐藏顶部、右侧和底部边框
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()