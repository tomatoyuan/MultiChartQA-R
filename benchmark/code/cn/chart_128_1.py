import matplotlib.pyplot as plt

# 数据
labels = ["Meta", "Pico", "DPVR", "HTC", "HP Inc", "其他"]
sizes = [75, 6, 6, 5, 3, 5]
colors = ["#FF7F24", "#FFD700", "#32CD32", "#8B4513", "#808000", "#228B22"]

fig, ax = plt.subplots(figsize=(8, 8))
# 绘制饼图，autopct 显示百分比，pctdistance 调整百分比位置，startangle 设置起始角度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", 
                                  pctdistance=0.8, startangle=90)

# 调整标注文字颜色为白色（可选，让数值更清晰）
for autotext in autotexts:
    autotext.set_color("white")

ax.set_title("全球VR头显设备出货量市场份额")

plt.tight_layout()
plt.show()