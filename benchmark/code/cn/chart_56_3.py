import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
labels = ["非常满意", "比较满意", "一般", "不太满意", "完全不满意"]
sizes = [7.8, 37.4, 46.9, 4.6, 3.4]  # 占比（%）
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # 颜色配置（贴近原图）

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制饼图 --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=140,     # 起始角度（调整扇形位置）
    colors=colors,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# -------------------- 添加注释（仅 45.2% 消费者满意） --------------------
# 计算满意占比（非常满意 + 比较满意）
satisfied_percent = sizes[0] + sizes[1]
ax.annotate(
    f"仅 {satisfied_percent:.1f}% 消费者对商品感到满意",
    xy=(1.1, 0.8),  # 注释位置（右侧上方）
    xytext=(1.3, 0.9), 
    arrowprops=dict(
        facecolor="pink", 
        edgecolor="pink", 
        arrowstyle="->", 
        linewidth=1
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="pink", ec="pink", alpha=0.5)
)

# -------------------- 美化图表 --------------------
# 设置标题
ax.set_title(
    "直播电商消费者对商品的满意程度",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整图例位置（避免与饼图重叠）
ax.legend(
    loc="lower left", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# 优化布局
plt.tight_layout()

plt.show()