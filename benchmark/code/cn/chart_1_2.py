import matplotlib.pyplot as plt
import numpy as np

# 年龄分组
age_groups = ['18岁以下', '18-24岁', '25-34岁', '35-44岁', 
              '45-54岁', '55-64岁', '65岁以上']
# 模拟数据，大体符合图示比例，可根据实际微调
data = [22, 28, 14, 10, 7, 6, 5]  

# 设置现代配色方案 - 深蓝到浅蓝渐变
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(age_groups)))
# 高亮显示18-24岁组
colors[1] = plt.cm.magma(0.6)

x = np.arange(len(age_groups))  # x轴刻度位置

# 创建图形和坐标轴，使用更宽的画布
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#ffffff')  # 白色背景
ax.set_facecolor('#f5f5f5')  # 浅灰色坐标轴背景

# 绘制柱状图，增加立体感
bars = ax.bar(x, data, width=0.7, color=colors, alpha=0.85, 
              edgecolor='#333333', linewidth=0.6)

# 在每个柱子上方添加数据标签，增加阴影效果
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.4,
            f'{height}', ha='center', va='bottom', 
            fontsize=11, fontweight='bold', color='black',
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.2'))

# 设置x轴刻度标签，水平显示
ax.set_xticks(x)
ax.set_xticklabels(age_groups, fontsize=12, fontweight='medium')

# 设置y轴范围和标签，隐藏y轴刻度线
ax.set_ylim(0, max(data) * 1.2)
ax.set_ylabel('搜索比例 (%)', fontsize=13, fontweight='medium', labelpad=10)
ax.tick_params(axis='y', which='both', length=0)

# 添加水平网格线，使用更浅的颜色
ax.grid(axis='y', linestyle='-', alpha=0.3, color='lightgray')

# 设置图表标题和副标题
ax.set_title('中风搜索人群年龄分布', fontsize=18, pad=20, fontweight='bold')
ax.text(0.5, 0.96, '18-24岁年龄段搜索量占比最高', transform=ax.transAxes, 
        ha='center', va='top', fontsize=13, color='#555555')

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 调整左侧和底部边框的颜色和粗细
ax.spines['left'].set_color('#cccccc')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_color('#cccccc')
ax.spines['bottom'].set_linewidth(1.5)


# 添加注释箭头指向最高的柱子
ax.annotate('最高占比', xy=(1, 30), xytext=(1, 32),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            ha='center', fontsize=12)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()