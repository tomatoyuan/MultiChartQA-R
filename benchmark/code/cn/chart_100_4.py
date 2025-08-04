import matplotlib.pyplot as plt
import numpy as np

# 影响睡眠的因素（TOP10）
factors = [
    "睡前忍不住玩手机/平板", "习惯性晚睡，缺乏改变动力", "生活压力太大，影响休息",
    "熬夜学习工作，影响休息", "白天不自由，晚上报复性熬夜", "卧室隔音差、环境嘈杂",
    "室友/伴侣影响我睡眠", "床垫、枕头等不舒服", "卧室温度、湿度不适宜",
    "身体病痛影响睡眠"
]
# 模拟占比数据（贴近原图）
percentages = [15.9, 13.6, 12.9, 9.5, 8.1, 7.2, 6.2, 5.6, 4.5, 3.5]
# 自由配色（可调整，示例用蓝色系）
bar_color = "#87CEEB"  

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向柱状图
y = np.arange(len(factors))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height / 2),
                xytext=(5, 0),  
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(factors)
# 设置x轴刻度（0-17%，适配数据）
ax.set_xlim(0, 17)
# 设置标题
ax.set_title("影响睡眠因素（TOP 10）", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()