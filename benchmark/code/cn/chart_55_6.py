import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
consume_groups = [
    "1000元及以下",
    "1001元-2000元",
    "2001元-3000元",
    "3001元-5000元",
    "5001元-8000元",
    "8001元-10000元",
    "10000元以上"
]
percentages = [8.1, 15.8, 25.9, 27.1, 14.7, 4.0, 4.5]  # 占比（%）

# 颜色配置（贴近原图绿色）
bar_color = "#a5d6a7"

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(consume_groups))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加百分比标注 --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(consume_groups, fontsize=12, color="#424242")

# 隐藏x轴
ax.set_xticks([])

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # 隐藏y轴刻度线

# 添加图例（模拟原图的图例样式）
ax.legend(
    ["用户月消费占比（%）"],
    loc="upper right", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "2025年中国电竞用户个人月消费水平",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()