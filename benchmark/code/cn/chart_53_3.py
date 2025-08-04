import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
# 月份（简化为2021.7-2022.6）
months = [f"2021.{i}" for i in range(7, 13)] + [f"2022.{i}" for i in range(1, 7)]

# 模拟数据（可替换为真实值）
protein_index = [100, 110, 120, 150, 200, 180, 160, 170, 190, 220, 240, 260]  # 蛋白粉整体
whey_index = [90, 95, 100, 130, 160, 140, 130, 140, 160, 180, 200, 220]    # 乳清蛋白

# 标注数据（对应显著变化点）
annotations = {
    "2021.11": "+70.3%",
    "2022.1": "+63.2%",
    "2022.5": "+17.4%",
    "2022.6": "+17.7%"
}

# 颜色配置（贴近原图黄绿+蓝配色）
protein_color = "#a5d6a7"  # 蛋白粉整体
whey_color = "#81d4fa"     # 乳清蛋白

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- 绘制双折线图 --------------------
# 蛋白粉整体
ax.plot(
    months, 
    protein_index, 
    marker="o", 
    color=protein_color, 
    label="蛋白粉（整体）成交额（指数）",
    linewidth=2
)

# 乳清蛋白
ax.plot(
    months, 
    whey_index, 
    marker="o", 
    color=whey_color, 
    label="乳清蛋白成交额指数",
    linewidth=2
)

# -------------------- 添加标注和箭头 --------------------
for month, text in annotations.items():
    idx = months.index(month)
    # 蛋白粉整体的标注（绿色箭头）
    if "2021.11" in month or "2022.5" in month:
        ax.annotate(
            text,
            xy=(idx, protein_index[idx]),
            xytext=(idx + 0.5, protein_index[idx] + 30),
            arrowprops=dict(
                facecolor=protein_color,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=protein_color
        )
    # 乳清蛋白的标注（蓝色箭头）
    else:
        ax.annotate(
            text,
            xy=(idx, whey_index[idx]),
            xytext=(idx + 0.5, whey_index[idx] + 25),
            arrowprops=dict(
                facecolor=whey_color,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=whey_color
        )

# -------------------- 美化图表 --------------------
# 设置y轴范围
ax.set_ylim(0, 300)

# 设置x轴刻度（倾斜避免重叠）
plt.xticks(rotation=45, ha="right", fontsize=9)

# 设置图例
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title(
    "蛋白粉（整体）、乳清蛋白月成交额趋势变化",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()