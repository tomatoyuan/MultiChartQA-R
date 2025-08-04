import matplotlib.pyplot as plt

# Data
labels = ["Once every six months", "Once a year", "Once every two years", "No check - up without illness", "Never had a physical examination", "Other"]
sizes = [3.94, 35.48, 39.41, 11.49, 9.52, 0.16]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots(figsize=(10, 8))

# Draw a donut chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct="%1.2f%%",  # 显示百分比
    startangle=90, 
    wedgeprops={"width": 0.4},
    pctdistance=1.15,  # 控制百分比文本与圆心的距离（>1表示外侧）
    labeldistance=1.3   # 控制标签与圆心的距离
)

# 设置百分比文本格式（外侧显示）
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')
    # 添加连接线（可选，增强可读性）
    autotext.set_bbox(dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white", alpha=0.8))

# 调整标签格式
for text in texts:
    text.set_fontsize(9)
    text.set_color('black')

# 设置标题
ax.set_title("Physical examination situation of Chinese consumers in 2025", fontsize=12, pad=50)

# 保证饼图是正圆形
ax.axis('equal')

plt.tight_layout()
plt.show()