import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- 数据定义 --------------------
categories = [
    "免疫力问题",
    "生长发育问题",
    "强健骨骼/促进骨骼发育",
    "视力问题",
    "促进肠胃消化",
    "专注力"
]
percentages = [76.0, 63.8, 63.3, 61.2, 48.0, 39.8]

# -------------------- 角度与颜色映射 --------------------
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
colors = cm.get_cmap("viridis")(mcolors.Normalize()(percentages))  # 可替换为 'coolwarm', 'viridis', etc.

# -------------------- 创建画布（极坐标） --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
bars = ax.bar(
    angles,
    percentages,
    width=2*np.pi/N * 0.8,  # 控制宽度
    color=colors,
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加标注 --------------------
for angle, height in zip(angles, percentages):
    ax.text(
        angle,
        height - 7,  # 圆弧外偏移
        f"{height:.1f}%",
        ha='center', va='center',
        fontsize=10,
        color="black",
        fontweight="bold"
    )

# -------------------- 设置类目标签（绕圆放置） --------------------
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=11, color="#333333")

# 隐藏极坐标默认半径线与刻度
ax.set_yticklabels([])
ax.set_yticks([])
ax.spines["polar"].set_visible(False)

# 添加标题
plt.title("4-6岁儿童阶段的健康关注（%）", fontsize=14, fontweight="bold", pad=30)

plt.tight_layout()
plt.show()