import matplotlib.pyplot as plt
import numpy as np

# 数据定义（与原图结构对应，可微调数值）
categories = ["早晨", "白天", "夜间（包括凌晨）", "非固定的碎片化时间"]
values = [3.0, 24.8, 53.2, 19.0]  # 模拟数据，可替换为真实值
special_label = {
    "夜间（包括凌晨）": "研究生TGI=121\n华中地区TGI=130"
}

# 颜色配置（贴近原图绿色系）
bar_color = "#81c784"
border_color = "#dcedc1"  # 虚线框颜色

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制横向条形图
y = np.arange(len(categories))
bars = ax.barh(y, values, color=bar_color, height=0.6, edgecolor="white", linewidth=1)

# 添加数值标注
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# 绘制特殊维度的虚线框（夜间）
target_idx = categories.index("夜间（包括凌晨）")
target_bar = bars[target_idx]
x0, y0 = target_bar.get_xy()
w, h = target_bar.get_width(), target_bar.get_height()
# 绘制虚线矩形框
rect = plt.Rectangle(
    (x0 - 0.2, y0 - 0.1),  # 向外扩展一点边距
    w + 0.4, h + 0.2,
    fill=False,
    linestyle="--",
    color=border_color,
    linewidth=2
)
ax.add_patch(rect)

# 添加特殊维度的文字标注（研究生TGI等）
if "夜间（包括凌晨）" in special_label:
    ax.text(
        x0 + w + 7,  # 右侧偏移
        y0 + h/2,
        special_label["夜间（包括凌晨）"],
        va="center",
        fontsize=9,
        color="#424242",
        linespacing=1.2
    )

# 美化图表
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color="#424242")
ax.set_xticks([])  # 隐藏x轴刻度
# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis="y", left=False)  # 隐藏y轴刻度线

# 添加标题
ax.set_title(
    "大学生最常进行论文写作的时间",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局（让内容居中）
plt.subplots_adjust(left=0.2, right=0.7, top=0.85, bottom=0.1)

plt.show()