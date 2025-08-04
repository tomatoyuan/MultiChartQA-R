import matplotlib.pyplot as plt

# 数据
labels = ["中国", "欧洲", "北美", "日本", "其他"]
sizes = [65, 9, 8, 7, 10]
# 颜色设置，尽量贴近原图
colors = ["#A4C639", "#8EBF8F", "#87CEEB", "#ADD8E6", "#FFD700"]  

# 创建画布
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  
    startangle=90,     
    colors=colors,
    textprops={"color": "black"}
)

# 设置标题，模拟顶部绿色背景标题（用普通标题+调整位置实现）
ax.set_title("全球不锈钢保温杯产量占比", fontsize=14, fontweight="bold", y=1.08, backgroundcolor="#8EBF8F", pad=8)

# 美化：让饼图保持圆形
ax.axis("equal")

plt.tight_layout()
plt.show()