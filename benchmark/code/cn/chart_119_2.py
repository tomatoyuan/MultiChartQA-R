import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 数据
labels = ["冰雪运动项目", "民俗冰雪活动", "冰雪观赏体验", "陆地冰雪活动"]
sizes = [27, 37, 25, 11]
# 对应颜色（尽量匹配原图，可根据实际微调）
colors = ['#4B9CD3', '#FF7F27', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 在环形中间添加自定义的“¥”符号，模拟原图效果
center_circle = Circle((0, 0), 0.3, color='white')
ax.add_artist(center_circle)
ax.text(0, 0, '¥', ha='center', va='center', fontsize=40, color='orange')

# 调整标注文字大小和颜色等（可选），让标注更清晰
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')  # 让数值在彩色块上更清晰

ax.set_title('2023-2024年冰雪季不同冰雪运动的消费占比情况')

plt.tight_layout()
plt.show()