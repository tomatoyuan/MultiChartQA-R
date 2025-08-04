import matplotlib.pyplot as plt
import numpy as np

# 数据
regions = ["广东", "浙江", "山东", "北京", "江苏", "上海", "湖北", "河南", "安徽", "湖南", "江西", "福建"]
# 模拟的数量值，按降序排列
values = [30, 28, 25, 24, 23, 22, 20, 12, 11, 10, 9, 8]

# 定义颜色分组（粉、橙、浅蓝），按数值大小排序
colors = ["#f9cbda"] * 3 + ["#f7c253"] * 4 + ["#c7e3ed"] * 5

# 创建画布和轴对象
fig, ax = plt.subplots(figsize=(10, 8))

# 反转y轴，使数值大的在上方
ax.invert_yaxis()

# 绘制横向柱状图
bars = ax.barh(regions, values, color=colors, edgecolor='none', alpha=0.85)

# 设置标题和标签
ax.set_title("购物后悔消费者地域分布", fontsize=16, fontweight="bold", pad=20)
ax.set_xlabel("消费者数量", fontsize=12, labelpad=10)

# 设置刻度标签大小
ax.tick_params(axis='both', which='major', labelsize=11)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 在每个柱子上添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}', ha='left', va='center', fontsize=10)

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.6)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()