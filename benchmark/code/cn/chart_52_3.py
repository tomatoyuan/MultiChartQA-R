import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
# 饼图数据
pie_labels = ["对毕业后的发展有明确规划", "没有明确规划"]
pie_sizes = [94.6, 5.4]
pie_colors = ["#81c784", "#b0bec5"]  # 贴近原图的绿色系

# 条形图数据（明确规划的细分）
bar_categories = ["继续深造", "就业", "考公考编", "出国留学"]
bar_values = [41.0, 34.8, 15.5, 3.3]
bar_colors = ["#a5d6a7", "#81c784", "#c8e6c9", "#e8f5e9"]  # 同色系渐变

# -------------------- 创建画布和子图 --------------------
fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(12, 5), 
                                     gridspec_kw={'width_ratios': [1, 2]})

# -------------------- 绘制饼图 --------------------
wedges, text_labels, auto_texts = ax_pie.pie(
    pie_sizes, 
    labels=None,  # 暂时不显示标签，通过图例展示
    autopct='%1.1f%%',
    startangle=90,
    colors=pie_colors,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
)

# 设置百分比文本颜色
for text in auto_texts:
    text.set_color('white')
    text.set_fontweight('bold')

# 添加图例显示完整标签
ax_pie.legend(
    wedges, 
    pie_labels, 
    loc='center left', 
    bbox_to_anchor=(-0.1, 0.5),
    fontsize=10
)

# 调整饼图位置
ax_pie.set_position([0.05, 0.1, 0.3, 0.8])

# -------------------- 绘制条形图 --------------------
bar_width = 0.6
x = np.arange(len(bar_categories))

# 绘制基础条形图
bars = ax_bar.barh(
    x, 
    bar_values, 
    color=bar_colors, 
    height=0.6,
    edgecolor='white',
    linewidth=1
)

# 添加数值标注
for bar in bars:
    width = bar.get_width()
    ax_bar.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f'{width}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# 美化条形图
ax_bar.set_yticks(x)
ax_bar.set_yticklabels(bar_categories, fontsize=12, color='#424242')
ax_bar.set_xlim(0, 50)  # 贴近原图比例
ax_bar.set_xticks([])   # 隐藏x轴刻度
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)
ax_bar.spines['bottom'].set_visible(False)
ax_bar.spines['left'].set_visible(False)
ax_bar.tick_params(axis='y', left=False)

# 调整条形图位置
ax_bar.set_position([0.4, 0.1, 0.5, 0.8])

# -------------------- 全局美化 --------------------
# 添加主标题
fig.suptitle(
    "大学生对毕业后发展方向的规划", 
    fontsize=16, 
    fontweight='bold', 
    y=0.95,
    x=0.3
)

# 添加连接箭头
import matplotlib.patches as patches
arrow = patches.FancyArrow(
    0.35, 0.5, 0.05, 0, 
    width=0.02, 
    head_width=0.05, 
    head_length=0.03, 
    color='#81c784',
    transform=fig.transFigure,
    figure=fig
)
fig.patches.append(arrow)

# 调整布局
plt.subplots_adjust(wspace=0.2)

plt.show()