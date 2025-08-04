import matplotlib.pyplot as plt


# 数据
categories = ['地方标准', '团体标准', '企业标准']
values = [27, 289, 90]

# 绘图
fig, ax = plt.subplots(figsize=(6, 6))
bars = ax.bar(categories, values, color='red')

# 添加数值标签
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{int(yval)}',
            ha='center', va='bottom', fontsize=12)

# 添加标题和标签
ax.set_title('2024年我国现行预制菜相关标准分布情况', fontsize=14)
ax.set_ylabel('单位：项', fontsize=12)

plt.tight_layout()
plt.show()