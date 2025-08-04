import matplotlib.pyplot as plt
import numpy as np

# 技术方向
tech_directions = ["人工智能", "大数据", "测试", "运维/技术支持", "后端开发", "前端开发", "移动开发"]
# 对应百分比数据
data = np.array([87.7, 44.2, 38.5, 38.0, 35.1, 22.2, 21.1])

# 气泡大小（用数据的平方模拟感知面积）
sizes = data ** 2.2  # 调整指数以优化视觉感知
colors = plt.cm.plasma(data / max(data))  # 使用 plasma 配色映射增强设计感

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 坐标轴设置
x = np.arange(len(tech_directions))

# 绘制气泡图
scatter = ax.scatter(x, [1]*len(x), s=sizes, c=colors, alpha=0.8, edgecolors='white', linewidths=1.5)

# 添加数值标注
for i in range(len(tech_directions)):
    ax.text(x[i], 1.02, f"{data[i]}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

# 设置x轴标签为技术方向
ax.set_xticks(x)
ax.set_xticklabels(tech_directions, rotation=15, ha="right", fontsize=11)
ax.set_yticks([])

# 添加标题
ax.set_title("2022年春季互联网主要技术方向招聘需求同比变化", fontsize=14, fontweight="bold", pad=20)

# 去除边框
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()