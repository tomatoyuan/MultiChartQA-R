import matplotlib.pyplot as plt

# 数据
labels = ["听父母的", "自己决定", "听专家或其它"]
sizes = [36, 58, 6]
colors = ["#99CCFF", "#FFCC99", "#CC99FF"]  # 保持原有配色

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 绘制饼图，添加阴影和爆炸效果突出"自己决定"部分
explode = (0, 0.05, 0)  # 仅"自己决定"部分突出
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    autopct='%1.1f%%',  # 仅显示百分比
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},  # 添加白色边框
    textprops={'fontsize': 12, 'weight': 'bold'}  # 加粗百分比文本
)

# 设置标题
ax.set_title("关于填报志愿，你更倾向于", fontsize=18, pad=20, fontweight='bold')

# 保证饼图为圆形
ax.axis("equal")  

# 优化图例样式
legend = ax.legend(
    wedges, 
    labels, 
    title="填报志愿倾向", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5),
    frameon=True,
    framealpha=0.9,
    edgecolor='lightgray',
    fontsize=12,
    title_fontsize=14,
    labelspacing=1.2,
    handlelength=1.5,
    handleheight=1.5
)

# 为图例添加背景色和圆角
frame = legend.get_frame()
frame.set_facecolor('#f8f9fa')
frame.set_boxstyle("round,pad=0.5,rounding_size=4")

# 添加数据标签样式
for text in autotexts:
    text.set_backgroundcolor('white')
    text.set_alpha(0.8)
    text.set_bbox(dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# 调整布局
plt.tight_layout(pad=2)

# 显示图形
plt.show()