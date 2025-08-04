import matplotlib.pyplot as plt

# 数据
labels = ['非常了解', '比较了解', '一般了解', '不了解']
sizes = [35, 50, 10, 5]
colors = ['#955c23', '#d8b77f', '#f3e7d3', '#f5f3ef']

# 绘图
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts = ax.pie(
    sizes, labels=labels, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.4, edgecolor='w'), colors=colors
)

# 添加标题
plt.title('消费者对于原生木浆的认知', fontsize=14)

# 添加文字说明
plt.text(-1.6, -1.0, '50%', fontsize=24, color='#d8b77f', weight='bold')
plt.text(-2.1, -1.3, '的消费者比较了解原生木浆的概念，\n知道其特点并有意愿购买', color='#d8b77f',  fontsize=12)

plt.text(1.1, -0.2, '35%', fontsize=24, color='#955c23', weight='bold')
plt.text(1.0, -0.7, '的消费者对原生木浆的概念非常了解，\n并表示在选购时会\n优先考虑这类原材料的纸巾',  color='#955c23', fontsize=12)

# 添加数据来源
plt.text(-2.2, -1.8,
         '数据来源：CBNData2024年3月中国消费者生活用纸趋势的调研\n数据说明：请问您对原生木浆（天然木制作的木浆，不添加其他纤维）的认知接近以下哪一种？N=1000',
         fontsize=8, color='gray')

plt.tight_layout()
plt.show()