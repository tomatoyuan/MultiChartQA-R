import matplotlib.pyplot as plt
import numpy as np

# 季度
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = np.array([7.0, 5.0, 4.2, 10.9])

# 气泡大小 (面积) 基于销售额放大一些，更直观
sizes = sales * 1000  

# 气泡颜色，渐变色
colors = ['#a8d5a2', '#82c97b', '#5eb852', '#3f9137']

fig, ax = plt.subplots(figsize=(7, 5))

# x 轴数值，用于散点位置
x = np.arange(len(quarters))

# 绘制气泡图
scatter = ax.scatter(x, sales, s=sizes, c=colors, alpha=0.7, edgecolors='white', linewidth=1.5)

# 添加数据标签
for i, val in enumerate(sales):
    ax.text(x[i], val + 0.3, f'{val}亿', ha='center', fontsize=10, fontweight='bold', color='#2e2e2e')

# 设置x轴
ax.set_xticks(x)
ax.set_xticklabels(quarters, fontsize=11, color="#424242")

# 隐藏y轴刻度
ax.set_yticks([])

# 添加总销售额说明文本
total_sales = sales.sum()
ax.text(0.5, 0.9, f"过去4季度 总销售额为{total_sales:.1f}亿",
        transform=ax.transAxes, fontsize=12, color='#388e3c', ha='center', va='bottom', fontweight='bold')

# 标题
ax.set_title("2021Q2-2022Q1啤酒电商销售额气泡图", fontsize=14, fontweight='bold')

# 美化：隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()