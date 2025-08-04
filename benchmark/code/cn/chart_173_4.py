import matplotlib.pyplot as plt

# 数据
labels = ['每天都看', '每周看4~6天', '每周看1~3天', '低于1周1天', '无规律']
sizes = [18, 36, 39, 6, 2]
colors = ['#ff6384', '#ff8fa3', '#ff2d55', '#ffb6c1', '#ffe5eb']  # 区分不同频次的红色系

# 构建标签内容
labels_with_pct = [f'{label}\n {size}%' for label, size in zip(labels, sizes)]

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts = ax.pie(sizes,
                       labels=labels_with_pct,
                       colors=colors,
                       startangle=90,
                       labeldistance=1.1,
                       textprops={'fontsize': 10},
                       wedgeprops=dict(width=0.6))

# 添加标题
plt.title('微短剧受众观看频次分布', fontsize=14, fontweight='bold', pad=20)

# 确保图为圆形
ax.axis('equal')

# 添加数据来源说明
fig.text(0.01, 0.01,
         '数据来源：秒针微短剧用户在线定量调研，2024年1月，N=1,000\n'
         'B1. 您日常观看微短剧的频率是？【单选】\n',
         fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.show()