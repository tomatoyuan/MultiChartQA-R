import matplotlib.pyplot as plt

# -------------------- 数据定义 --------------------
labels = ["高中及以下", "本科及以上", "专科"]
sizes = [60.2, 27.1, 12.7]  # 占比（%）
tgis = [76, 218, 156]       # TGI 值

# 颜色配置（贴近原图配色）
colors = ["#a5d6a7", "#81d4fa", "#c8e6c9"]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- 绘制饼图 --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度（让“高中及以下”在右侧）
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
    "蛋白粉整体：学历情况",
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