import matplotlib.pyplot as plt

# 数据
labels = ['轻度', '中度', '中重度', '重度', '无']
sizes = [29.3, 25.3, 17.7, 11.9, 15.8]
colors = ['#65D1DD', '#6449A6', '#FF7B9C', '#FFA01B', '#F5C447']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # 使各部分稍微突出

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%',
    startangle=90, counterclock=False, colors=colors,
    explode=explode, textprops={'fontsize': 12}, wedgeprops={'width': 0.3}
)

ax.set_title('心理评估用户抑郁情况测评', fontsize=16, pad=20)
ax.axis('equal')  # 保持饼图为圆形
plt.tight_layout()
plt.show()