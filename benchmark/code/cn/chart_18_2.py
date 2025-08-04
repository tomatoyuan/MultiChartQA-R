import matplotlib.pyplot as plt
import numpy as np

# 数据定义
labels = ["酒席", "车队", "司仪", "婚庆用品", "其他", "蜜月", "首饰", "婚纱照"]
sizes = [6, 0.8, 0.2, 1.5, 5, 4, 3, 1]
total_cost = sum(sizes)  # 总费用

# 优化的颜色方案（使用更协调的渐变色）
colors = plt.cm.YlOrRd(np.linspace(0.2, 0.9, len(labels)))

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制环形图（donut chart）
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=None,  # 不在图上直接显示标签
    colors=colors,
    autopct='',  # 先不显示数值
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),  # 增加环形宽度和白色边框
)

# 自定义标签：同时显示名称和金额，并智能调整位置和颜色
for i, (wedge, label, size) in enumerate(zip(wedges, labels, sizes)):
    # 计算文本位置
    theta = (wedge.theta2 + wedge.theta1) / 2
    x = 0.65 * np.cos(np.radians(theta))  # 0.65控制径向位置
    y = 0.65 * np.sin(np.radians(theta))
    
    # 根据扇形大小调整文本样式
    text_size = 10 if size / total_cost > 0.05 else 8  # 小扇形用更小字体
    
    # 文本内容
    text = f"{label}\n{size}万元"
    
    # 调整文本颜色（深色扇形用白色文本，浅色扇形用黑色文本）
    color = 'white' if i in [0, 4, 5, 6] else 'black'
    
    # 添加文本
    ax.text(x, y, text, ha='center', va='center', fontsize=text_size, 
            fontweight='bold', color=color, bbox=dict(
                boxstyle="round,pad=0.2", 
                fc=colors[i], 
                ec='none', 
                alpha=0.7
            ))

# 设置标题
ax.set_title("上海刘小姐婚礼费用分布", fontsize=18, fontweight='bold', pad=20)
subtitle = f"总费用: {total_cost}万元"
plt.figtext(0.5, 0.92, subtitle, ha='center', fontsize=12, color='gray')

# 添加中心文本
centre_circle = plt.Circle((0, 0), 0.2, fc='white')
ax.add_patch(centre_circle)
ax.text(0, 0, "婚礼费用", ha='center', va='center', fontsize=14, fontweight='bold')

# 调整布局
plt.tight_layout()

# 添加数据来源
plt.figtext(0.5, 0.01, "数据来源: 假设示例", ha='center', fontsize=8, color='gray')

plt.show()