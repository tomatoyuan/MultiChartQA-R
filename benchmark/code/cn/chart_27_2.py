import matplotlib.pyplot as plt

# 日期数据
dates = ["3月28日", "3月30日", "4月1日", "4月3日", "4月5日", "4月7日", "4月9日"]
# 对应数值数据
values = [290000, 290000, 580000, 870000, 1160000, 1450000, 1740000]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图，marker='o' 显示圆点，linewidth=2.5 加粗线条
ax.plot(dates, values, color='red', marker='o', linewidth=2.5)  

# 设置 y 轴刻度和标签
ax.set_yticks([290000, 580000, 870000, 1160000, 1450000, 1740000, 2030000])
ax.set_yticklabels(["29万", "58万", "87万", "116万", "145万", "174万", "203万"])

# 设置 x 轴标签，旋转 30 度更美观
ax.set_xticklabels(dates, rotation=30, ha='right', fontsize=10)  

# 添加网格线增强可读性
ax.grid(True, linestyle='--', alpha=0.7)

# 添加标题和轴标签
plt.title("《人民的名义》网络搜索指数走势", fontsize=15, pad=20)
plt.xlabel("日期", fontsize=12)
plt.ylabel("搜索指数", fontsize=12)

# 美化图表边框
for spine in ax.spines.values():
    spine.set_color('gray')

# 添加数据标签
for x, y in zip(dates, values):
    ax.annotate(f'{y:,}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)

# 显示图形
plt.tight_layout()
plt.show()