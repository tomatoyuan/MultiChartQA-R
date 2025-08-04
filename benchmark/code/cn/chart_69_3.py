import matplotlib.pyplot as plt
import numpy as np

# 住宿偏好类别
categories = ["卫生安全", "特色体验", "亲子项目", "宠物友好", "拍照打卡", "一价全包", "其它"]
# 对应数据（占比），数据大体一致即可
data = [91.2, 49.8, 36.6, 28.7, 27.0, 12.0, 10.5]
# 颜色设置，贴近原图绿色系
color = "#C6395C"

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, data, width=bar_width, color=color, edgecolor="white")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title("微度假人群的住宿偏好", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.show()