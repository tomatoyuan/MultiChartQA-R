import matplotlib.pyplot as plt

# 数据
labels = ['原料相关', '品牌相关', '医美相关', '其他']
sizes = [46.6, 24.7, 16.4, 12.3]

# 更粉嫩的淡色系（使用柔和的粉红色调）
colors = ['#FADADD', '#F9C6D0', '#F7B0C4', '#F59EB7']

# 绘制饼图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12, 'color': 'black'}
)

# 添加标题和数据来源
plt.title('2023年不同领域投资事件数占比', fontsize=14, pad=20)
plt.figtext(0.1, 0.01, '*取数范围：中国本土美妆行业相关投融资事件', ha='left', fontsize=10)

# 保证饼图为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()