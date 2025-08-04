import matplotlib.pyplot as plt

# 提取图表数据
age_groups = ["19岁及以下", "20-29岁", "30-39岁", "40-49岁", "50岁以上"]
percentages = [22, 36, 28, 9, 5]

# 自定义颜色方案（使用柔和的蓝绿色调）
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# 突出显示最大的扇形（20-29岁组）
explode = (0, 0.1, 0, 0, 0)

# 创建绘图对象
fig, ax = plt.subplots(figsize=(10, 7))

# 绘制美化后的饼图
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=age_groups,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 12}
)

# 设置百分比标签的颜色与饼图颜色一致
for text, autotext, color in zip(texts, autotexts, colors):
    text.set_color('gray')
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# 设置饼图为正圆形
ax.axis('equal')

# 添加标题
ax.set_title('“最爱后悔”的消费者年龄分布', fontsize=16, fontweight='bold', pad=20)

# 添加图例，并调整位置
ax.legend(wedges, age_groups, title="年龄分组", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 设置图表背景色
fig.set_facecolor('#f8f9fa')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()