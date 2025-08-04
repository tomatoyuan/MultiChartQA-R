import matplotlib.pyplot as plt
import numpy as np

# 睡眠质量反馈分类
labels = ["无问题，睡得非常好", "还好，偶尔有睡眠问题", "是，时不时有睡眠问题", "是，有较严重的睡眠问题", "是，有非常严重的睡眠问题"]
# 模拟占比数据（贴近原图）
percentages = [18.7, 47.0, 23.2, 8.7, 2.4]
# 自由配色（可调整，示例用绿色系）
bar_color = "#6339C6"  

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
x = np.arange(len(labels))  
bar_width = 0.5  
bars = ax.bar(x, percentages, width=bar_width, color=bar_color)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=40, ha='right', fontsize=9)  
# 设置y轴刻度（0-50%，适配数据）
ax.set_ylim(0, 50)
# 设置标题
ax.set_title("用户反馈自身睡眠质量情况", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()