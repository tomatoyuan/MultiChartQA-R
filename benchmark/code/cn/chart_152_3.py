# 图表4（再优化）：在每个扇形区域旁添加中文标签与百分比数值，提升可读性

labels = [
    "精致妈妈", "小镇青年", "资深中产", "新锐白领",
    "小镇中老年", "Gen Z", "都市银发", "都市蓝领", "资深蓝领"
]
sizes = [22, 20, 19, 16, 9, 8, 3, 2, 1]
colors = plt.cm.PuRd(np.linspace(0.2, 0.9, len(labels)))

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4),
    textprops=dict(color="black", fontsize=9)
)

# 标题美化
ax.set_title("鲨鱼裤人群偏好分布（占比由高到低）", fontsize=13)

plt.tight_layout()
plt.show()