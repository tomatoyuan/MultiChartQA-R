import matplotlib.pyplot as plt

# Data
labels = ["Opposite - sex with undetermined relationship", "Boyfriend", "Husband"]
values = [119, 1115, 139]

# Create a bar chart with adjusted figure size
plt.figure(figsize=(9, 6))  # 增加宽度以容纳倾斜标签
bars = plt.bar(labels, values, color="#F48FB1")  # Pink - based color

# 设置横坐标标签倾斜角度和对齐方式
plt.xticks(rotation=30, ha='right', fontsize=11)  # 30度倾斜+右对齐

# Add title and labels
plt.title("Proportion of female gift - giving recipients", fontsize=16, fontweight="bold")
plt.xlabel("Gift - giving recipients", fontsize=12)
plt.ylabel("Quantity", fontsize=12)

# Display values above the bars
for i, v in enumerate(values):
    plt.text(i, v + 20, str(v), ha="center", fontsize=10)  # 调整数值标签位置

# 隐藏顶部和右侧边框，优化视觉效果
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Optimize the layout and display
plt.tight_layout()
plt.show()