import matplotlib.pyplot as plt

# -------------------- 数据定义 --------------------
labels = ["男性", "女性"]
sizes = [63.4, 36.6]  # 占比（%）
colors = ["#a5d6a7", "#4dd0e1"]  # 颜色配置（贴近原图）

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- 绘制环形饼图 --------------------
# 核心：通过 wedgeprops 设置环形宽度
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度（让“男性”部分在右侧）
    colors=colors,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "width": 0.3,    # 环形宽度（核心参数）
        "edgecolor": "white",
        "linewidth": 2
    }
)

# -------------------- 添加中心文本 --------------------
# 在环形中心添加“63.4% 的电竞用户为男性”
ax.text(
    0, 0, 
    "63.4% 的电竞用户为男性",
    ha="center", 
    va="center",
    fontsize=14,
    color="#424242",
    fontweight="bold"
)

# -------------------- 美化图表 --------------------
# 设置标题
ax.set_title(
    "2025年中国电竞用户性别情况",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 优化布局
plt.tight_layout()

plt.show()