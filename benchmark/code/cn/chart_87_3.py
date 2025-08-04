import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# -------------------- 数据准备 --------------------
reasons = [
    "医生建议", "想先采取别的方式看看", 
    "自己觉得没必要配镜", "孩子不愿意配镜", "其他"
]
percentages = [41.2, 36.5, 14.4, 7.9, 0.1]

# 极坐标角度划分（每个分类一个角度）
angles = np.linspace(0, 2 * np.pi, len(reasons), endpoint=False)
# 将数据转为 numpy 数组
data = np.array(percentages)

# 设置颜色渐变
cmap = cm.get_cmap("autumn_r")  # 橙红色渐变
colors = [cmap(i / len(data)) for i in range(len(data))]

# -------------------- 创建极坐标图 --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# 设置起始角度 & 排列方向
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 绘制极坐标柱状图
bars = ax.bar(angles, data, width=0.5, color=colors, edgecolor="white", linewidth=1)

# 添加数据标注
for i, (bar, percentage) in enumerate(zip(bars, data)):
    angle = angles[i]
    ax.text(
        angle, bar.get_height(),
        f"{percentage}%",
        ha='center', va='bottom',
        fontsize=10, fontweight="bold",
        color="#424242"
    )

# 添加标签（类别）
ax.set_xticks(angles)
ax.set_xticklabels(reasons, fontsize=10, color="#333333")

# 去除极轴线与刻度
ax.set_yticklabels([])
ax.spines["polar"].set_visible(False)
ax.grid(False)

# 添加标题
ax.set_title("未立即配镜/暂未配镜的原因", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()