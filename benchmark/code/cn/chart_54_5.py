import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据整理 --------------------
# 从图中提取的 TGI 数据（按行对应三组）
data = {
    "7-11岁小学阶段": [109, 102, 105, 111, 95, 107, 104, 102, 93, 79, 89, 78, 95, 69, 24],
    "12-14岁初中阶段": [103, 98, 109, 84, 128, 107, 92, 102, 112, 123, 164, 121, 152, 111, 109],
    "15-17岁高中阶段": [96, 87, 98, 92, 95, 88, 94, 98, 95, 105, 107, 106, 124, 99, 135, 212]
}

# 确保三组数据长度一致（补全缺失值，实际应根据原始数据调整）
max_len = max(len(v) for v in data.values())
for key in data:
    if len(data[key]) < max_len:
        data[key] += [np.nan]*(max_len - len(data[key]))

# 分组标签（x轴位置）
x = np.arange(max_len)

# 颜色配置（贴近原图的浅绿色）
colors = ["#a5d6a7", "#c8e6c9", "#e8f5e9"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- 绘制分组柱状图 --------------------
bar_width = 0.25  # 每组柱子宽度

for i, (group, values) in enumerate(data.items()):
    ax.bar(
        x + i*bar_width, 
        values, 
        width=bar_width, 
        color=colors[i], 
        label=group,
        edgecolor="white",
        linewidth=1
    )

# -------------------- 添加数据标注 --------------------
for i, (group, values) in enumerate(data.items()):
    for j, val in enumerate(values):
        if not np.isnan(val):
            ax.text(
                x[j] + i*bar_width, 
                val + 2,  # 向上偏移
                f"{val}",
                ha="center",
                fontsize=8,
                color="#424242",
                fontweight="bold"
            )

# -------------------- 美化图表 --------------------
# 设置x轴刻度（隐藏，因为是分类对比）
ax.set_xticks([])

# 设置y轴范围
ax.set_ylim(0, 220)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加图例
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 添加标题
ax.set_title(
    "不同年龄段青少年 TGI 数据对比",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()