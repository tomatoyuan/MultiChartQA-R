import matplotlib.pyplot as plt
import numpy as np

# 睡眠问题分类（TOP10）
problems = [
    "深睡时间太短", "入睡困难", "习惯性熬夜晚睡", 
    "睡得浅/易被惊醒", "睡眠时长不够", "白天容易犯困/没精神", 
    "睡眠作息不规律", "周末等时间赖床/起不来", "多梦/噩梦"
]
# 模拟占比数据（贴近原图）
percentages = [13.8, 11.7, 10.6, 10.0, 9.7, 9.5, 7.9, 7.1, 6.3]
# 自由配色（可调整，示例用蓝色系）
bar_color = "#CB87EB"  # 可替换为其他颜色如 "#FF8C00"

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向柱状图
y = np.arange(len(problems))
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
ax.set_yticklabels(problems)
# 设置x轴刻度（0-15%）
ax.set_xlim(0, 15)
# 设置标题
ax.set_title("用户反馈睡眠问题（TOP10）", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()