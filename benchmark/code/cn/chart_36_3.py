import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["AI 助力人群点击率提升约", "AI 助力人群转化率提升约", "人群圈选效率提升约"]
values = [20, 30, 100]  # 百分比数值
colors = ["#FF99CC", "#FF99CC", "#FF99CC"]  # 接近的粉色
bar_width = 0.5  # 柱状图宽度
x = np.arange(len(labels))  # x 轴位置

# 创建图形
fig, ax = plt.subplots(figsize=(8, 4))  # 调整画布大小，接近原图表比例

# 绘制柱状图
bars = ax.bar(x, values, width=bar_width, color=colors, edgecolor="white")

# 添加标题
ax.set_title("「AI 圈人」有何用", fontsize=14, fontweight="bold", y=1.1)  # 标题位置稍上

# 添加数据标签
for bar, value in zip(bars, values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{value}%",
            ha="center", va="bottom", fontsize=12, color="pink")

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10)

# 隐藏 y 轴（原图表无 y 轴显示）
ax.yaxis.set_visible(False)

# 隐藏边框（更接近原图表简洁风格）
for spine in ax.spines.values():
    spine.set_visible(False)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()