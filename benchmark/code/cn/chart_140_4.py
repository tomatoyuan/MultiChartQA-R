import matplotlib.pyplot as plt

# 数据
labels = ["纯电动汽车（车载电机）", "混合动力车（油电新能源）", "氢燃料电动车", 
          "燃料电池汽车（化学反应发电）", "燃气汽车（天然气）", "替代燃料汽车（如乙醇）"]
sizes = [61.3, 22.0, 8.4, 4.7, 2.9, 0.7]
colors = ["#FAD6A5", "#F9CB9C", "#F7B787", "#F4A460", "#E9967A", "#CD5C5C"]

fig, ax = plt.subplots(figsize=(10, 7))

# 绘制饼图
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)

ax.set_title('2023年中国消费者认为最有发展前景的新能源汽车类型')
ax.legend(wedges, labels, title="汽车类型", loc="center left", bbox_to_anchor=(1, 0.5))

# 调整标注文字颜色，确保在深色/浅色切片上清晰可见
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()