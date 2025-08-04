import matplotlib.pyplot as plt

# 数据准备
labels = ["100-1000元", "1001-2000元", "2001-4000元", "4001-8000元", "8001-10000元", "10000元以上"]
sizes = [20.1, 26.3, 32.7, 14.2, 5.3, 1.4]
colors = ["blue", "orange", "gray", "yellow", "cyan", "green"]

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=140)

ax.set_title('2023年中国网民瘦身支出金额占比')

# 调整图例
ax.legend(wedges, labels, title="支出区间", loc="center left", bbox_to_anchor=(1, 0.5))

# 调整标注文字颜色（让深色切片的标注文字为白色，浅色为黑色，更清晰）
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()