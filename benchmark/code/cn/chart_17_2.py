import matplotlib.pyplot as plt
import numpy as np


# 数据定义
provinces = ["广东", "江苏", "山东", "北京", "河南"]
fraud_attention = [11, 9, 6.5, 5.2, 4]
gdp_2015 = [9.5, 7.5, 4, 1.2, 2.2]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(provinces))
width = 0.35

# 设置渐变色
colors1 = plt.cm.Oranges(np.linspace(0.6, 0.9, len(provinces)))
colors2 = plt.cm.Greens(np.linspace(0.6, 0.9, len(provinces)))

# 绘制带渐变色的柱状图
rects1 = ax.bar(x - width/2, fraud_attention, width, 
                label='各省份电信诈骗关注度', color=colors1, 
                edgecolor='black', linewidth=0.5)

rects2 = ax.bar(x + width/2, gdp_2015, width, 
                label='2015各省份GDP总量', color=colors2, 
                edgecolor='black', linewidth=0.5)

# 添加数值标签（优化位置和样式）
def add_labels(rects, ax, is_top=False):
    for rect in rects:
        height = rect.get_height()
        y_pos = height + 0.3 if not is_top else height - 0.3
        va = 'bottom' if not is_top else 'top'
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, y_pos),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va=va,
                    fontsize=10, fontweight='bold')

add_labels(rects1, ax)
add_labels(rects2, ax, is_top=True)

# 设置图表标题和坐标轴标签
ax.set_title("各省份电信诈骗关注度与2015各省份GDP总量对比", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("数值 (单位：亿元/关注度指数)", fontsize=12, labelpad=10)

# 设置x轴和y轴样式
ax.set_xticks(x)
ax.set_xticklabels(provinces, fontsize=12, fontweight='bold')
ax.set_ylim(0, 13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 美化图例
legend = ax.legend(fontsize=10, frameon=True, loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('gray')
frame.set_alpha(0.8)

# 添加底部文字说明（优化排版）
plt.figtext(0.5, 0.01, 
            "防骗关注前五：广东 山东 江苏 北京 河南\n"
            "2015各省GDP排行前五：广东 江苏 山东 浙江 河南", 
            ha="center", fontsize=10, color='dimgray')

# 添加背景色区分区域
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# 调整布局
plt.tight_layout(pad=3)
plt.show()