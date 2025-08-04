import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# 数据
years = np.array([2018, 2019, 2020, 2021, 2025])
sales_scales = np.array([6531, 7562, 8848, 10458, 17218])

# 归一化用于颜色映射
norm = mcolors.Normalize(vmin=min(sales_scales), vmax=max(sales_scales))
cmap = cm.get_cmap('BuGn')

# 创建画布
fig, ax = plt.subplots(figsize=(10, 5))

# 计算气泡大小（面积）：面积与值成比例，避免太大
bubble_sizes = (sales_scales / max(sales_scales)) * 25000

# 绘制气泡图
sc = ax.scatter(
    years, 
    [1]*len(years),  # 垂直居中
    s=bubble_sizes,
    c=sales_scales,
    cmap=cmap,
    alpha=0.8,
    edgecolors='white',
    linewidth=1.5
)

# 添加文本标注（销售额）
for i, (x, y, val) in enumerate(zip(years, [1]*len(years), sales_scales)):
    ax.text(x, y, f"{val}", ha="center", fontsize=10, fontweight="bold", color="#333")

# 添加CAGR标注文字
ax.annotate("CAGR 17% →", xy=(2018.2, 1.15), fontsize=10, color="#388e3c", weight="bold")
ax.annotate("→ CAGR 13.3%", xy=(2021.3, 1.15), fontsize=10, color="#1976d2", weight="bold")

# 美化横轴
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=11)
ax.set_xlim(2017.5, 2025.5)

# 隐藏 y 轴
ax.set_yticks([])
ax.spines['left'].set_visible(False)

# 美化边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_alpha(0.2)

# 添加标题
ax.set_title("2018-2025年中国IC市场销售规模（亿元）", fontsize=14, fontweight='bold', pad=20)

# 去除网格线，仅强调气泡 + 文字
ax.grid(False)

plt.tight_layout()
plt.show()