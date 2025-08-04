import matplotlib.pyplot as plt
import numpy as np

# 代际分类
generations = ["00后", "90后", "80后", "70后", "60后+"]
# 模拟睡眠得分数据（贴近原图）
scores = [81.7, 82.7, 83.0, 83.3, 83.5]
# 自由配色（可调整，示例用绿色系）
bar_color = "#A4C639"  

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制柱状图
x = np.arange(len(generations))  
bar_width = 0.5  
bars = ax.bar(x, scores, width=bar_width, color=bar_color)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(generations)
# 设置y轴刻度（80-85，适配数据）
ax.set_ylim(80, 85)
# 设置标题
ax.set_title("各代际人群睡眠得分", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()