import matplotlib.pyplot as plt

# 年龄占比数据（估算）
age_labels = ['18-24', '25-29', '30-34', '35-39', '40+']
age_shares = [25, 25, 20, 15, 15]

# 同比增速数据（估算）
growth_rates = [80, 10, 50, 85, 70]  # 估算柱形高度代表的增速

# 设置图表风格
colors = ['#FF4C88', '#FFA6C1', '#FDBACD', '#FECEDC', '#FEE5EA']

# 创建并排图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制饼图
ax1.pie(age_shares, labels=age_labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.set_title("2023年送爱人人群年龄占比")
ax1.axis('equal')

# 绘制柱状图
bars = ax2.bar(age_labels, growth_rates, color=colors)
ax2.set_title("同比增速")
ax2.set_ylabel("增速指数")
ax2.set_ylim(0, 100)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()