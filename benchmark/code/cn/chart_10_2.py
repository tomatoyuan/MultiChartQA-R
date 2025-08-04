import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['职业培训计算机端检索占比', '职业培训移动端检索占比']
sizes = [19.30, 80.70]
# 更现代的配色方案
colors = ['#3498db', '#e74c3c']  
# 突出显示移动端部分
explode = (0, 0.05)  

# 创建图形和轴，设置图形大小
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制环形图，添加阴影效果和百分比文本格式优化
wedges, texts, autotexts = ax.pie(sizes, 
                                explode=explode,
                                labels=labels,
                                autopct=lambda p: f'{p:.2f}%\n({p*sum(sizes)/100:.1f})',
                                startangle=90,
                                colors=colors,
                                wedgeprops={'width': 0.4, 'edgecolor': 'w', 'linewidth': 2},
                                shadow=True,
                                textprops={'fontsize': 12})

# 设置标题和图例
ax.set_title('职业培训检索终端占比分析', fontsize=16, pad=20)
ax.legend(wedges, labels, title="终端类型", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 优化百分比文本样式 - 将颜色修改为深色
plt.setp(autotexts, size=12, weight="bold", color='black')  # 修改颜色为黑色
plt.setp(texts, size=12)

# 设置图形背景和布局
plt.tight_layout()
plt.axis('equal')  # 保证饼图是圆形
plt.subplots_adjust(right=0.8)  # 为图例留出空间

# 保存图形（可选）
# plt.savefig('职业培训检索终端占比.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()