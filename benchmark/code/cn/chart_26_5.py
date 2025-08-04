import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


# 数据准备
industries = [
    '健康护理', '房产/建筑', '批发/零售', '汽车', 
    '政府/非盈利机构', '酒店/旅游', '金融业', 
    '广告/营销', 'IT/互联网'
]
coverage = [2.9, 3.5, 5.1, 6.1, 7.5, 8.2, 9.2, 19.9, 21.9]

# 创建渐变色映射
cmap = LinearSegmentedColormap.from_list("custom_green", ["#E8F5E9", "#2E7D32"])

# 创建绘图对象
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#F5F5F5')  # 设置图表背景色
ax.set_facecolor('#FAFAFA')  # 设置坐标轴背景色

# 绘制横向条形图（使用渐变色）
y_pos = np.arange(len(industries))
bars = ax.barh(y_pos, coverage, color='#4CAF50', edgecolor='#2E7D32', linewidth=0.8)

# 应用渐变色
for i, bar in enumerate(bars):
    bar.set_color(cmap(i/len(bars)))

# 添加数据标签（优化位置和样式）
for i, v in enumerate(coverage):
    ax.text(v + 0.3, i, f'{v}%', va='center', fontsize=11, 
            fontweight='medium', color='#333333')

# 设置标题和坐标轴标签（优化字体和位置）
ax.set_title('哪些行业的人更关心“情人节礼物”？', 
             fontsize=18, pad=20, fontweight='bold', color='#333333')
ax.set_xlabel('行业覆盖率 (%)', fontsize=13, labelpad=15, color='#555555')
ax.set_ylabel('行业类别', fontsize=13, labelpad=15, color='#555555')

# 设置y轴刻度标签
ax.set_yticks(y_pos)
ax.set_yticklabels(industries, fontsize=11, color='#444444')

# 优化坐标轴刻度和网格线
ax.set_xlim(0, max(coverage) + 3)
ax.grid(axis='x', linestyle='--', alpha=0.6, color='#CCCCCC')

# 隐藏顶部、右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')

# 调整布局
plt.tight_layout(pad=2)

# 显示图表
plt.show()