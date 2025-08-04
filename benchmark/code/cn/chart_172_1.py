import matplotlib.pyplot as plt

# 数据定义
labels = ['偏好低糖', '偏好无糖', '不关注', '偏好多糖']
sizes = [56, 23, 12, 9]
colors = ['#00a2e8', '#b3ecf7', '#00d2c8', '#4caf50']  # 模拟原图色彩搭配

# 拼接标签显示百分比
labels_with_pct = [f'{label}, {size}%' for label, size in zip(labels, sizes)]

# 创建饼图
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts = ax.pie(sizes, labels=labels_with_pct, colors=colors, startangle=100,
                       labeldistance=0.5, textprops={'fontsize': 11, 'color': 'white'})

# 添加标题
plt.title('2022年中国消费者对碳酸饮料含糖看法', fontsize=14, fontweight='bold', pad=20)

# 强制使图为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()