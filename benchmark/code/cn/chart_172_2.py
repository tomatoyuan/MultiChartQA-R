import matplotlib.pyplot as plt

# 数据定义
labels = ['血糖控制', '血压调节', '降低胆固醇', '心脏健康', '其他']
sizes = [25, 25, 25, 17, 8]
colors = ['#00d2c8', '#66cdaa', '#00a2e8', '#3399ff', '#ccecf9']  # 按图示配色

# 构建标签内容（带百分比）
labels_with_pct = [f'{label}, {size}%' for label, size in zip(labels, sizes)]

# 绘图
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts = ax.pie(sizes, labels=labels_with_pct, colors=colors,
                       startangle=90, labeldistance=0.5,
                       textprops={'fontsize': 11, 'color': 'white'})

# 标题
plt.title('2024年慢病相关原料创新方向', fontsize=14, fontweight='bold', pad=20)

# 保持图为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()