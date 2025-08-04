import matplotlib.pyplot as plt
import numpy as np

# 食用场景分类
scenarios = [
    "聚餐/用餐后", "看剧/综艺/电影", 
    "下午茶点", "工作/学习时", 
    "运动/健身后", "外出游玩", "自制美食场景"
]
# 模拟占比数据（贴近原图）
percentages = [64.0, 59.6, 55.4, 51.8, 47.5, 44.0, 42.2]
# 自由配色（可调整，示例用橙色系）
bar_color = "#F6FF7A"  # 可替换为其他颜色如 "#87CEEB"
# 蓝色虚线框覆盖的前四项索引
dashed_box_indices = [0, 1, 2, 3]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向柱状图
y = np.arange(len(scenarios))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

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
ax.set_yticklabels(scenarios)
# 设置x轴刻度（0-70%）
ax.set_xlim(0, 70)
# 设置标题
ax.set_title("水果食用场景", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()