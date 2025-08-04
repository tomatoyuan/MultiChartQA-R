import matplotlib.pyplot as plt

# 使用频次数据
frequency_labels = ["几乎没有使用", "偶尔使用", "需要就使用", "较常使用"]
frequency_sizes = [10.0, 45.5, 33.7, 10.8]
frequency_colors = ["#FF9933", "#FF5733", "#FFD700", "#FFC300"]

# 体验数据
experience_labels = ["改善了购物体验", "对购物体验没有太大影响", "使购物体验变差", "不清楚", "其他（请注明）"]
experience_sizes = [33.3, 37.4, 25.2, 3.9, 0.2]
experience_colors = ["#FFB6C1", "#FF8C69", "#FFDAB9", "#D8BFD8", "#C0C0C0"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制使用频次饼图
wedges, texts, autotexts = ax1.pie(frequency_sizes, colors=frequency_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('使用频次')
# 调整图例，放在饼图右侧
ax1.legend(wedges, frequency_labels, title="使用频次分类", loc="center left", bbox_to_anchor=(1, 0.5))
# 让标注文字颜色更清晰（区分深色/浅色切片）
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# 绘制体验饼图
wedges2, texts2, autotexts2 = ax2.pie(experience_sizes, colors=experience_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('体验')
ax2.legend(wedges2, experience_labels, title="体验分类", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('2024年中国消费者对于AI电商中的人工干预功能的使用频次及其体验', fontsize=14)
plt.tight_layout()
plt.show()