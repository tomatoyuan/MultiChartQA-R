import matplotlib.pyplot as plt
import numpy as np

# 食用频率分类
frequencies = [
    "每天一次及以上", "两到三天一次", 
    "四到五天一次", "一周一次", 
    "两周一次", "两周以上一次"
]
# 模拟占比数据（贴近原图）
percentages = [54.9, 27.7, 11.6, 4.1, 1.1, 0.1]
# 自由配色（可调整，示例用蓝色系）
bar_color = "#87CEEB"  # 可替换为其他颜色如 "#FF8C00"

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制横向柱状图
y = np.arange(len(frequencies))
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

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(frequencies)
# 设置x轴刻度（0-60%）
ax.set_xlim(0, 60)
# 设置标题
ax.set_title("水果食用频率", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()