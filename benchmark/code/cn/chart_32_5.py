import matplotlib.pyplot as plt
import numpy as np

# 定义关键词和对应面积（按指定顺序递减，整体放大）
keywords = ["教师资格证", "在线教育", "教师编制", "教师假期", "教师待遇"]
sizes = [152000, 111600, 9200, 6800, 4400]  # 面积整体放大为原来的2倍
colors = ['#FFC2D1', '#BDE0FE', '#BDB2FF', '#A2D2FF', '#C8B6FF']  # 气泡颜色

# 创建画布
plt.figure(figsize=(12, 10))  # 增大画布尺寸

# 生成均匀分布的位置（环形排列）
theta = np.linspace(0, 2*np.pi, len(keywords), endpoint=False)
radius = 1.5  # 增大圆的半径，避免气泡重叠
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# 绘制气泡图
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, edgecolors='w', linewidths=2)

# 添加标签
for i, txt in enumerate(keywords):
    plt.annotate(txt, (x[i], y[i]), ha='center', va='center', 
                 fontsize=14, fontweight='bold', color='#333333')  # 增大字体

# 设置图表属性
plt.axis('equal')  # 保证气泡是圆形
plt.axis('off')    # 隐藏坐标轴
plt.title("教师行业关键词关注度气泡图", fontsize=18, pad=20)  # 增大标题字体

# 显示图表
plt.tight_layout()
plt.show()