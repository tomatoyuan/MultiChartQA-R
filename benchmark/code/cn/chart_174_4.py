import matplotlib.pyplot as plt

# 数据
labels = ['价格优惠', '酒店积分', '其他']
sizes = [58.7, 36.9, 4]
colors = ['#009C8A', '#A1D4A2', '#F3ECD9']

# 绘图
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 14}
)

plt.title('消费者期待的鼓励措施', fontsize=16)
plt.axis('equal')  # 使饼图为正圆
plt.tight_layout()
plt.show()