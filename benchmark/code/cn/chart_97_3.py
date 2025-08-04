import matplotlib.pyplot as plt

# 观看比赛年限分类及占比（模拟数据，贴近原图）
labels = ["5年以上", "2-5年", "2年以内"]
sizes = [89.9, 7.6, 2.5]
# 自由配色（可调整）
colors = ["#A4C639", "#87CEEB", "#FFD700"]

# 创建画布
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')  # 环形饼图效果（可选，若要实心饼图可删除）
)

# 设置标题
ax.set_title("2022年中国足球球迷观看比赛年限", fontsize=14, fontweight="bold", y=1.05)

# 美化标注（颜色、大小）
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
    autotext.set_color('black')
    autotext.set_fontsize(10)

# 隐藏边框（饼图无实际边框，仅规范布局）
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()