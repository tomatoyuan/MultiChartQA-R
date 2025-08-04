import matplotlib.pyplot as plt
import numpy as np

# 痛点分类
pain_points = [
    "设备传统，不够智能", "设备功能单一", "设备对人力依赖高",
    "设备使用期间噪音大", "设备占地面积大", "设备易坏，损坏率高",
    "设备使用期间油烟大", "设备寿命短，报废率高", "设备成本高，难以回本",
    "设备运行/出菜效率低", "设备操作复杂/不简便"
]
# 模拟占比数据（可调整，前三项与原图近似）
percentages = [48.9, 48.1, 48.1, 37.6, 36.8, 33.8, 28.6, 27.8, 25.6, 24.8, 16.5]
# 蓝色虚线框覆盖的前三项索引
dashed_box_indices = [0, 1, 2]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 7))

# 绘制横向柱状图
y = np.arange(len(pain_points))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color="#A4C639")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # 标注位置：右侧偏移 5
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# 绘制蓝色虚线框
min_y = min([bars[i].get_y() for i in dashed_box_indices])
max_y = max([bars[i].get_y() + bar_height for i in dashed_box_indices])
max_width = max([bars[i].get_width() for i in dashed_box_indices])

# 绘制虚线框（上、右、下、左）
ax.plot([0, max_width], [max_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([max_width, max_width], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, max_width], [min_y, min_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, 0], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(pain_points)
# 设置x轴刻度（0-50%）
ax.set_xlim(0, 55)
# 设置标题
ax.set_title("厨电设备使用痛点", fontsize=14, fontweight="bold")

# 隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()