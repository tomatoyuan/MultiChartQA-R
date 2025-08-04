import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import cm

# -------------------- 数据定义 --------------------
platforms = ["抖音", "哔哩哔哩", "微信", "快手", "微博", "海外渠道", "小红书", "知乎", "其他"]
data = [53.4, 48.6, 48.0, 24.9, 24.0, 19.5, 15.3, 11.3, 19.8]
x = np.arange(len(platforms))

# -------------------- 颜色设置（渐变蓝紫） --------------------
cmap = cm.get_cmap("cool")  # 蓝紫渐变
colors = [cmap(i / len(data)) for i in range(len(data))]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(9, 6))

# -------------------- 绘制圆角条形图 --------------------
bar_height = 0.5
for i, (platform, value) in enumerate(zip(platforms, data)):
    rect = patches.FancyBboxPatch(
        (0, i - bar_height / 2),  # 起始点 (x, y)
        value, bar_height,        # 宽度，高度
        boxstyle="round,pad=0.1",
        linewidth=0,
        facecolor=colors[i],
        edgecolor="none",
        alpha=0.9
    )
    ax.add_patch(rect)

    # 添加数据标签
    ax.text(value + 1, i, f"{value}%", va="center", ha="left",
            fontsize=10, fontweight="bold", color="#424242")

# -------------------- 美化图表 --------------------
ax.set_xlim(0, max(data) + 10)
ax.set_ylim(-0.5, len(platforms) - 0.5)
ax.set_yticks(x)
ax.set_yticklabels(platforms, fontsize=11, color="#333333")

ax.set_xticks([])
ax.set_xlabel("")  # 不显示x轴
ax.set_title("中国创作者偏好发布内容的平台", fontsize=14, fontweight="bold", pad=20)

# 隐藏边框
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# 去除刻度
ax.tick_params(axis="both", which="both", length=0)

plt.tight_layout()
plt.show()