import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
# 饼图数据
pie_labels = ["1副", "其他"]
pie_sizes = [53.2, 46.8]
pie_colors = ["#dcdcdc", "#a5d6a7"]  # 灰色、浅绿色

# 嵌套柱状图数据（“其他”分类拆分）
bar_labels = ["2副", "3副及以上"]
bar_sizes = [42.7, 4.1]  # 注意：42.7+4.1=46.8，与饼图“其他”占比匹配
bar_colors = ["#a5d6a7", "#81c784"]  # 浅绿色、深绿色

# -------------------- 创建画布 --------------------
fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(8, 5), gridspec_kw={"width_ratios": [1, 2]})

# -------------------- 绘制饼图 --------------------
wedges, texts, autotexts = ax_pie.pie(
    pie_sizes,
    labels=pie_labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度（让“1副”部分在左侧）
    colors=pie_colors,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# 调整饼图文本位置（避免重叠）
for text, auto in zip(texts, autotexts):
    text.set_fontsize(10)
    auto.set_fontsize(10)

# -------------------- 绘制嵌套柱状图 --------------------
x = np.arange(len(bar_labels))
bar_width = 0.6

ax_bar.bar(
    x, 
    bar_sizes, 
    width=bar_width, 
    color=bar_colors,
    edgecolor="white",
    linewidth=1
)

# 添加数据标注
for i, val in enumerate(bar_sizes):
    ax_bar.text(
        i, val + 1, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- 美化图表 --------------------
# 饼图优化
ax_pie.set_aspect("equal")  # 保证饼图为正圆
ax_pie.spines["top"].set_visible(False)
ax_pie.spines["right"].set_visible(False)

# 柱状图优化
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(bar_labels, fontsize=10, color="#424242")
ax_bar.set_ylim(0, 50)  # y轴范围匹配数据
ax_bar.spines["top"].set_visible(False)
ax_bar.spines["right"].set_visible(False)

# 添加标题
fig.suptitle(
    "近视人群拥有的框架眼镜数量分布",
    fontsize=14,
    fontweight="bold",
    y=1.05  # 标题位置
)

# 调整布局
plt.tight_layout()

plt.show()