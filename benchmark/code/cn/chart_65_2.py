import matplotlib.pyplot as plt
import numpy as np

# 平台名称
platforms = ["Tiktok", "Youtube", "Instagram", "Facebook", "Twitter", "其他"]
# 对应数据
data = [30.0, 22.0, 22.0, 14.0, 4.0, 13.0]

x = np.arange(len(platforms))  # 用于设置x轴位置
bar_width = 0.5  # 柱状图宽度

fig, ax = plt.subplots()
# 绘制柱状图，设置颜色、宽度等，颜色尽量贴近蓝色
bars = ax.bar(x, data, width=bar_width, color="#64B5F6", edgecolor="white")  

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标签距离柱状图的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(platforms)
# 设置y轴标签（原图表未显示y轴标签，可根据需求决定是否添加）
# ax.set_ylabel("占比（%）")
# 设置图表标题
ax.set_title("海外创作者偏好发布内容的平台")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.show()