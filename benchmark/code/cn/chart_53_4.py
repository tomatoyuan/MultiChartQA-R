import matplotlib.pyplot as plt
import numpy as np

# 数据定义（与原图结构对应，可微调数值）
age_groups = ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "≥60"]
percentages = [23.3, 17.3, 17.3, 13.3, 10.2, 7.6, 5.3, 2.8, 2.8]  # 占比数据
tgis = [159, 119, 93, 90, 89, 76, 69, 63, 75]  # TGI 数据

# 颜色配置（贴近原图绿色系）
bar_color = "#81c784"

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制横向条形图
y = np.arange(len(age_groups))
bars = ax.barh(y, percentages, color=bar_color, height=0.6, edgecolor="white", linewidth=1)

# 添加占比数值标注
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移 1 个单位
        bar.get_y() + bar.get_height() / 2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# 添加 TGI 标注（在条形左侧，模拟原图布局）
for i, (age, tgi) in enumerate(zip(age_groups, tgis)):
    ax.text(
        -3,  # 左侧偏移，可根据实际调整
        y[i] + bar.get_height() / 2,
        f"TGI: {tgi}",
        va="center",
        ha="right",
        fontsize=9,
        color="#424242"
    )

# 美化图表
ax.set_yticks(y)
ax.set_yticklabels(age_groups, fontsize=12, color="#424242")
ax.set_xticks([])  # 隐藏 x 轴刻度

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # 隐藏 y 轴刻度线

# 添加标题
ax.set_title(
    "蛋白奶粉体：年龄段",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局（让内容居中，给左侧 TGI 标注留空间）
plt.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.1)

plt.show()