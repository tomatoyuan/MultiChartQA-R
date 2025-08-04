import matplotlib.pyplot as plt
import numpy as np

# 使用场景
scenarios = [
    "上下班通勤", "接送孩子", "短途自驾游", 
    "亲友聚会", "商场/超市购物", "长途自驾游", "长途探亲"
]
# 模拟占比数据（尽量贴近原图）
percentages = [67.8, 61.2, 59.6, 45.6, 44.7, 44.0, 32.7]
# 颜色配置（贴近原图的绿色）
color = "#A4C639"

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制横向柱状图
y = np.arange(len(scenarios))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=color)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # 标注位置：右侧偏移 5
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(scenarios)
# 设置x轴刻度（0-70%）
ax.set_xlim(0, 70)
# 设置标题
ax.set_title("MPV车辆使用场景", fontsize=14, fontweight="bold")

# 隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()