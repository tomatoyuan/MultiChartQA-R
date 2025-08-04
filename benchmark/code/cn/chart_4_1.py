import matplotlib.pyplot as plt
import numpy as np

# 生成完整的5月日期（1-31日）
dates = [f"5/{i}" for i in range(1, 32)]
x = np.arange(len(dates))  # 用于横坐标定位

# 整形美容关注度数据（左侧纵轴，单位：百万）
plastic_surgery = [
    6.5, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 9.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0
]

# 鼻部整形占比数据（右侧纵轴，单位：%）
nose_plastic = [
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0
]

# 眼部整形占比数据（右侧纵轴，单位：%）
eye_plastic = [
    5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0
]

# 皮肤美容占比数据（右侧纵轴，单位：%）
skin_care = [
    15.0, 15.0, 15.0, 15.0, 15.0, 14.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 13.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 16.0
]

# 创建画布和双轴
fig, ax1 = plt.subplots(figsize=(14, 7))  # 增大画布尺寸
ax2 = ax1.twinx()

# 绘制整形美容柱状图（左轴）
bar_width = 0.6
bars = ax1.bar(
    x,
    plastic_surgery,
    color="#1f77b4",  # 专业蓝色
    width=bar_width,
    label="整形美容"
)
ax1.set_ylabel("关注度（百万）", color="#1f77b4", fontsize=12, fontweight="bold")
ax1.set_ylim(0, 10)
ax1.set_yticks(np.arange(0, 11, 1))
ax1.tick_params(axis="y", labelcolor="#1f77b4", labelsize=10)

# 在柱状图顶部添加数值标签
for bar in bars:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2., height + 0.1,
        f'{height:.1f}',
        ha='center', va='bottom', fontsize=9
    )

# 绘制鼻部整形折线（右轴）
ax2.plot(
    x,
    nose_plastic,
    color="#2ca02c",  # 专业绿色
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="鼻部整形"
)

# 绘制眼部整形折线（右轴）
ax2.plot(
    x,
    eye_plastic,
    color="#ff7f0e",  # 专业橙色
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="眼部整形"
)

# 绘制皮肤美容折线（右轴）
ax2.plot(
    x,
    skin_care,
    color="#d62728",  # 专业红色
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="皮肤美容"
)
ax2.set_ylabel("占比（%）", color="black", fontsize=12, fontweight="bold")
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 20, 2))
ax2.tick_params(axis="y", labelcolor="black", labelsize=10)

# 设置横轴刻度（每3天显示一个刻度，避免过于拥挤）
ax1.set_xticks(x[::3])  # 每隔3天显示一个刻度
ax1.set_xticklabels(dates[::3], fontsize=10, rotation=45, ha="right")  # 旋转45度并右对齐

# 添加网格（仅左轴y方向）
ax1.grid(axis="y", linestyle="--", color="gray", alpha=0.4)

# 合并图例（放置在底部）
lines_ax1, labels_ax1 = ax1.get_legend_handles_labels()
lines_ax2, labels_ax2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines_ax1 + lines_ax2,
    labels_ax1 + labels_ax2,
    loc="lower center",
    ncol=4,
    bbox_to_anchor=(0.5, -0.2),
    frameon=False,
    fontsize=11
)

# 设置标题
ax1.set_title("5月医疗美容行业搜索关注度趋势", fontsize=16, fontweight="bold", y=1.05)

# 添加背景色区分不同区域
for i in range(0, len(dates), 6):
    if i % 12 == 0:
        ax1.axvspan(i-0.5, i+5.5, alpha=0.05, color='gray')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()