import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = [
    "提高免疫力、增强抵抗力",
    "改善睡眠",
    "补充能量，让自己有精力",
    "改善胃肠道健康",
    "均衡营养的摄取",
    "提升眼睛/视力健康",
    "提高代谢水平",
    "改善记忆力",
    "调节内分泌",
    "提升骨骼和关节健康"
]

# 模拟数据（前3项为绿色，其余为灰色）
percentages = [75.7, 57.9, 47.7, 46.9, 44.9, 43.8, 35.6, 35.0, 34.4, 33.3]

# 颜色配置（前3项绿色，其余灰色）
colors = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categories)-3)

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
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
        f"{width}",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=11, color="#424242")

# 隐藏x轴
ax.set_xticks([])

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # 隐藏y轴刻度线

# 添加标题
ax.set_title(
    "居民服用膳食营养补充剂的目的（%）",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()