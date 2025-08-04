import matplotlib.pyplot as plt

# 类别
labels = ["关注度和信任度提高", "其他"]
# 各类别占比（%），数据大体一致即可
sizes = [65.0, 35.0]
# 饼图各部分颜色，尽量贴近原图
colors = ["#A4C639", "#64B5F6"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=90, colors=colors, 
    textprops={'color': 'black'}
)

# 美化标注文本（调整大小等）
for text in texts + autotexts:
    text.set_fontsize(12)

# 添加底部说明文本
ax.text(0.5, -0.2, "● 65%消费者表明疫情后，对中医药的关注度和信任度提高", 
        ha='center', va='bottom', fontsize=10, color='green')

# 设置标题
ax.set_title("2021年中医药新冠诊疗关注度与信任度", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # 自动调整布局
plt.show()