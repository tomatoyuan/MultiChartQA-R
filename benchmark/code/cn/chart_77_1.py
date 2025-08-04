import matplotlib.pyplot as plt

# 预算变化类别
labels = ["明显减少", "略有减少", "基本持平", "略有增长", "明显增长"]
# 各类别占比（%），数据大体一致即可
sizes = [10.5, 40.8, 34.9, 12.5, 1.3]
# 饼图各部分颜色，尽量贴近原图
colors = ["#A4D68C", "#87D3F2", "#A4C639", "#74BCEF", "#F2D387"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# 美化标注文本（调整大小等）
for text in texts + autotexts:
    text.set_fontsize(12)

# 设置标题
ax.set_title("2022年企业培训的客户预算变化", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # 自动调整布局
plt.show()