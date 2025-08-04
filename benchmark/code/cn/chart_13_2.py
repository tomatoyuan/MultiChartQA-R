import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 整理数据
age_groups = ["18岁及以下", "18 - 24岁", "25岁-34岁", "35 - 49岁", "50岁及以上"]
sample_coverage = [23.1, 22.16, 39.41, 12.12, 2.8]  # 样本覆盖率数据
total_coverage = [12.4, 28.44, 36.63, 20.16, 3.2]  # 全体覆盖率数据

x = np.arange(len(age_groups))  # x轴刻度位置
width = 0.35  # 柱状图宽度

# 创建画布和子图，优化画布大小适配
fig, ax = plt.subplots(figsize=(10, 7))
# 设置整体背景色，贴近原图蓝色
fig.set_facecolor('#00a8e8')
ax.set_facecolor('#00a8e8')

# 绘制样本覆盖率柱状图，调整颜色更柔和
rects1 = ax.bar(
    x - width/2, 
    sample_coverage, 
    width, 
    label='样本覆盖率', 
    color='#003f5c',
    edgecolor='white',  # 增加白色描边区分柱形
    linewidth=1
)
# 绘制全体覆盖率柱状图，调整颜色更柔和
rects2 = ax.bar(
    x + width/2, 
    total_coverage, 
    width, 
    label='全体覆盖率', 
    color='#457fca',
    edgecolor='white',  # 增加白色描边区分柱形
    linewidth=1
)

# 定制标题样式
ax.set_title(
    '观海模式：上班族最受伤', 
    fontsize=20, 
    fontweight='bold', 
    color='#002f4a',  # 深色标题更醒目
    pad=20  # 增加标题与图表间距
)
ax.set_ylabel(
    '暴雨舆情情况人口属性分布', 
    fontsize=14, 
    color='#333333',
    labelpad=15  # 增加y轴标签与图表间距
)

# 定制x轴刻度标签样式
ax.set_xticks(x)
ax.set_xticklabels(
    age_groups, 
    fontsize=12, 
    color='#333333',
    rotation=0  # 保持水平显示
)

# 优化y轴刻度，显示百分比更清晰
ax.set_ylim(0, 50)  # 合理设置y轴范围
ax.yaxis.set_major_formatter('{x}%')  # 直接显示百分比样式（需 matplotlib 3.3+）
ax.tick_params(axis='y', labelsize=12, colors='#333333')

# 优化数据标签样式
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f'{height}%',
            xy=(rect.get_x() + rect.get_width()/2, height),
            xytext=(0, 5),  # 调整标签位置，避免遮挡
            textcoords='offset points',
            ha='center', 
            va='bottom',
            fontsize=11,
            color='white',  # 白色标签更醒目
            fontweight='bold'
        )

autolabel(rects1)
autolabel(rects2)

# 定制图例样式，放在图表上方
legend_elements = [
    Patch(facecolor='#003f5c', edgecolor='white', label='样本覆盖率'),
    Patch(facecolor='#457fca', edgecolor='white', label='全体覆盖率')
]
ax.legend(
    handles=legend_elements,
    loc='upper center',  # 图例位置
    bbox_to_anchor=(0.5, 1.15),  # 微调图例位置到图表上方
    ncol=2,  # 图例分两列显示
    fontsize=12,
    frameon=False  # 去掉图例边框
)

# 添加网格线，增强可读性
ax.grid(
    axis='y', 
    color='white', 
    linestyle='--', 
    alpha=0.8,
    linewidth=1
)

# 优化整体布局
plt.tight_layout()
# 显示图表
plt.show()