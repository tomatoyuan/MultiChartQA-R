import matplotlib.pyplot as plt

# -------------------- 数据定义 --------------------
labels = ["过去1年买过膳食营养补充剂", "过去1年未买过膳食营养补充剂"]
sizes = [70.6, 29.4]  # 占比（%）

# 颜色配置（贴近原图配色）
colors = ["#a5d6a7", "#dcdcdc"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- 绘制饼图 --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度（让“买过”部分在右侧）
    colors=colors,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "linewidth": 2, 
        "edgecolor": "white"
    }
)

# -------------------- 美化图表 --------------------
# 设置标题
ax.set_title(
    "过去1年买过膳食营养补充剂的人群占比",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整图例位置（模拟原图的布局）
ax.legend(
    loc="upper left", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# 优化布局
plt.tight_layout()

plt.show()