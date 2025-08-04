import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['含水量/透氧量', '材质成分', '配戴参数', '原产地', '配戴抛期', '颜色工艺', '品牌信誉', '价格水平', '相关服务', '包装储存']
values = [52, 52, 46, 45, 43, 43, 42, 41, 40, 35]

# 定义y轴位置
y_pos = np.arange(len(labels))

# 优化的渐变色方案（从深蓝到浅蓝）
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(labels)))

# 创建图形（增加尺寸）
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向条形图（增加边距和透明度）
bars = ax.barh(y_pos, values, color=colors, alpha=0.85, edgecolor='gray', linewidth=0.5)

# 设置y轴标签（增加标签间距）
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10)

# 设置x轴标签和标题
ax.set_xlabel('关注度百分比', fontsize=12)
ax.set_title('消费者关注隐形眼镜的专业维度', fontsize=14, pad=15)

# 优化数值标签（增加字体大小和颜色）
for i, v in enumerate(values):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=10, color='black')

# 添加网格线（更轻的网格）
ax.grid(axis='x', linestyle='--', alpha=0.3)

# 设置x轴范围（增加边距）
ax.set_xlim(0, max(values) * 1.1)

# 美化边框（隐藏顶部和右侧边框）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()