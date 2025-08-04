import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = [
    "蛋白粉（整体）",
    "蛋白粉（益生菌）",
    "钙铁锌/钙镁/钙",
    "维生素/矿物质",
    "酵素蛋白",
    "胶原蛋白",
    "深海鱼油/深海鱼油Omega3",
    "牡蛎/贝类提取物",
    "左旋肉碱",
    "玛卡提取物",
    "葡萄籽提取物",
    "DHA/EPA/DPA",
    "纳豆提取物",
    "叶酸",
    "蔓越莓"
]

# 模拟数据（可替换为真实值）
values = [7.4, 5.2, 4.8, 4.5, 4.2, 3.9, 
          3.7, 3.5, 3.2, 3.0, 2.8, 2.6, 
          2.4, 2.2, 2.0]

# 特殊标注（对应“蛋白粉（整体）”）
special_note = (
    "“蛋白粉”是保健食品/膳食营养补充食品一级类目下，\n"
    "膳食营养补充子类中，最头部的市场之一"
)

# 颜色配置（贴近原图绿色系）
bar_color = "#81c784"
highlight_color = "#a5d6a7"  # 高亮颜色（蛋白粉整体）

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 7))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(categories))

# 高亮第一个条形（蛋白粉整体）
bars = ax.barh(
    y, 
    values, 
    color=[highlight_color] + [bar_color]*(len(categories)-1),
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# 添加数值标注
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.2,  # 右侧偏移
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# 文字注释（右侧说明）
ax.text(
    max(values) + 1.5,  # 右侧偏移
    y[0] - 0.5,  # 向上偏移
    special_note,
    fontsize=9,
    color="#424242",
    linespacing=1.2,
    ha="left",
    bbox=dict(
        facecolor="white", 
        edgecolor=bar_color, 
        boxstyle="round,pad=0.5"
    )
)

# -------------------- 美化图表 --------------------
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=10, color="#424242")
ax.set_xticks([])  # 隐藏x轴刻度

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # 隐藏y轴刻度线

# 添加标题
ax.set_title(
    "保健食品/膳食营养补充食品（一级类目）中细分市场占比",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.subplots_adjust(left=0.3, right=0.7, top=0.85, bottom=0.1)

plt.show()