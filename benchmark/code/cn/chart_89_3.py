import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# 消费地点
locations = ["中高档餐厅", "大众餐厅", "家里/宿舍", "酒吧/小酒馆", "其他"]
# 18-29岁占比（%），数据与图表一致
age18_29 = [41.7, 21.1, 18.6, 10.8, 7.8]
# 30岁及以上占比（%），数据与图表一致
age30_up = [30.6, 34.7, 19.8, 11.2, 3.7]
# 中间标注的参考占比（用于对齐）
ref_rates = [35.4, 28.8, 19.3, 11.0, 5.5]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制18-29岁的水平条形图（绿色）
y = np.arange(len(locations))
bar_width = 0.35
bars1 = ax.barh(y + bar_width/2, age18_29, height=bar_width, color="#A4C639", label="18-29岁占比（%）")
# 绘制30岁及以上的水平条形图（蓝色）
bars2 = ax.barh(y - bar_width/2, age30_up, height=bar_width, color="#87CEEB", label="30岁及以上占比（%）")

# 添加数据标注（18-29岁）
for i, bar in enumerate(bars1):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(-5, 0),  # 左侧标注
                textcoords="offset points",
                ha='right', va='center',
                color='white' if i == 0 else 'black')  # 第一个标注意为白色（模拟红圈强调）

# 添加数据标注（30岁及以上）
for i, bar in enumerate(bars2):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 右侧标注
                textcoords="offset points",
                ha='left', va='center',
                color='white' if i == 1 else 'black')  # 第二个标注意为白色（模拟红圈强调）

# 设置y轴刻度和标签（调整位置，让分类在中间）
ax.set_yticks(y)
ax.set_yticklabels(locations)
ax.set_yticklabels(locations, ha='center', va='center')

# 设置标题
ax.set_title("白酒消费地点", fontsize=16, fontweight="bold")

# 添加图例
ax.legend(loc='upper right')

# 美化：隐藏顶部、右侧、底部边框
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

# 调整x轴范围，留出标注空间
ax.set_xlim(0, max(max(age18_29), max(age30_up)) + 10)

plt.tight_layout()
plt.show()