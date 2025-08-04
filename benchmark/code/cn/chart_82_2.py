import matplotlib.pyplot as plt
import numpy as np

# 痛点类别
pain_points = [
    "工作生活压力大，易情绪紧张/低落",
    "主观上对自身身材/体态不满意",
    "亚健康状态，患有颈椎病等慢性疾病",
    "社交媒体营销引发身材/生活方式焦虑",
    "有熬夜、抽烟等不良生活习惯/嗜好",
    "工作生活难以平衡，空闲时间较少",
    "社交圈窄，希望交更多朋友",
    "可支配收入难以满足消费需求"
]
# 对应占比（%），数据大体一致即可
percentages = [55.1, 50.7, 47.0, 43.8, 41.6, 39.9, 31.9, 29.7]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制条形图（水平条形图，调整为与原图方向一致）
y = np.arange(len(pain_points))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#A4C639")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签（调整顺序，让第一个痛点在最上方）
ax.set_yticks(y)
ax.set_yticklabels(pain_points)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2022年中国健身用户日常生活工作中的主要痛点", fontsize=14, fontweight="bold")

# 模拟不同边框样式（根据原图，部分条目有虚线边框，这里简化示意，可按需扩展）
# 比如给“亚健康状态，患有颈椎病等慢性疾病”添加虚线边框
special_index = 2
special_bar = bars[special_index]
x0, y0 = special_bar.get_xy()
width, height = special_bar.get_width(), special_bar.get_height()
# 绘制虚线矩形边框
rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()