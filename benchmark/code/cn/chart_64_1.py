import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
# 满意度分类
labels = [
    "非常满意", "9分", "8分", "7分", "6分", 
    "5分", "4分", "3分", "2分", "非常不满意"
]
# 百分比数据
percentages = [22.0, 23.6, 14.6, 17.1, 16.3, 4.9, 1.6, 0, 0, 0]
# 平均满意度
average_score = 7.97

# 颜色配置（贴近原图绿色系）
bar_color = "#a5d6a7"

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(labels))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6
)

# -------------------- 添加数据标注 --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1, 
        bar.get_y() + bar.get_height() / 2,
        f"{width}%",
        va="center", 
        fontsize=9, 
        color="#424242",
        fontweight="bold"
    )

# -------------------- 添加平均满意度标注（蓝色水滴） --------------------
# 绘制垂直线
ax.axvline(
    average_score, 
    color="lightblue", 
    linestyle="--", 
    linewidth=2,
    label=f"平均满意度 {average_score}分"
)

# 绘制水滴形状（简化为注释文本+箭头）
ax.annotate(
    f"{average_score}分",
    xy=(average_score, len(labels)/2), 
    xytext=(average_score + 3, len(labels)/2), 
    arrowprops=dict(
        arrowstyle="->",
        color="blue", 
        linewidth=1
    ),
    fontsize=12,
    color="blue",
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="lightblue",
        edgecolor="blue",
        alpha=0.8
    )
)

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

# 隐藏x轴刻度
ax.set_xticks([])

# 隐藏顶部、右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title(
    "2022年中国商户私域布局带来效果满意度",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()