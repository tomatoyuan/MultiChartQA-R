import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
regions = [
    "美国", "巴西", "印度", "印度尼西亚",
    "英国", "日本", "西班牙", "德国",
    "意大利", "法国"
]
percentages = [22.7, 14.5, 6.7, 3.7, 3.4, 2.8, 2.4, 2.0, 2.0, 2.0]

# 闭合数据
values = percentages + [percentages[0]]
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=True)

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# -------------------- 绘制雷达图 --------------------
ax.plot(angles, values, color="#ab47bc", linewidth=2)
ax.fill(angles, values, color="#ce93d8", alpha=0.4)

# -------------------- 设置坐标标签 --------------------
ax.set_xticks(angles[:-1])
ax.set_xticklabels(regions, fontsize=10, color="#424242")

# -------------------- 设置极轴范围 --------------------
ax.set_rlabel_position(30)
ax.set_yticks([2.5, 5, 10, 15, 20, 25])
ax.set_yticklabels(["2.5%", "5%", "10%", "15%", "20%", "25%"], color="#757575", fontsize=9)
ax.set_ylim(0, 25)

# -------------------- 添加数值标注（方法3：微调位置） --------------------
for i, val in enumerate(percentages):
    angle = angles[i]
    x = angle
    y = val + 2  # 向外偏移
    ha = "left" if np.pi/2 < angle < 3*np.pi/2 else "right"
    ax.text(
        x, y, f"{val}%",
        fontsize=9,
        ha=ha,
        va="center",
        color="#424242",
        fontweight="bold",
        rotation_mode="anchor"
    )

# -------------------- 添加图例 --------------------
import matplotlib.patches as mpatches
patch = mpatches.Patch(color="#ab47bc", label="各区域占比（%）")
ax.legend(handles=[patch], loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=10)

# -------------------- 添加标题 --------------------
ax.set_title(
    "全球各区域红人营销帖子数量分布（雷达图）",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- 显示图表 --------------------
plt.tight_layout()
plt.show()