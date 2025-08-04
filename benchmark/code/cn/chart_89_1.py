import matplotlib.pyplot as plt
import numpy as np

# 数据定义
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = [64.3, 69.5, 91.2, 81.2]

# 坐标轴
x = np.arange(len(quarters))

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制渐变面积图
# 用fill_between创建底部渐变
ax.plot(x, sales, color="#4CAF50", linewidth=2.5, marker='o', label="销售额")
ax.fill_between(x, sales, color="#C8E6C9", alpha=0.8)

# 添加数据标注
for i, val in enumerate(sales):
    ax.text(x[i], val + 1.5, f"{val}", ha='center', va='bottom', fontsize=10, fontweight='bold', color="#388E3C")

# 添加总销售额说明文本
total_sales = sum(sales)
ax.text(0.5, 0.9, f"过去4季度 总销售额破{total_sales:.0f}亿",
        transform=ax.transAxes, fontsize=12, color='#0288D1', ha='center', va='bottom', fontweight='bold')

# 设置x轴
ax.set_xticks(x)
ax.set_xticklabels(quarters, fontsize=11)

# 隐藏y轴刻度线，仅设置范围
ax.set_yticks([])
ax.set_ylim(0, max(sales) + 15)

# 添加标题
ax.set_title("2021Q2-2022Q1 白酒电商销售额趋势", fontsize=14, fontweight="bold", pad=15)

# 美化：去除边框
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# 网格线（增强阅读感）
ax.grid(axis='y', linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()