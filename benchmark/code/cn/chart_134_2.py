import matplotlib.pyplot as plt
import numpy as np

# 左侧：使用频率数据
labels_freq = ["经常使用", "每天", "偶尔", "很少使用"]
sizes_freq = [62.3, 23.4, 12.6, 1.7]
colors_freq = ["#FF7F24", "#FFD700", "#90EE90", "#FFC0CB"]

# 右侧：价格接受度数据
labels_price = ["50元-99元", "100元-149元", "150元及以上", "50元以下"]
sizes_price = [46.1, 41.2, 7.0, 5.7]
colors_price = ["#FF7F24", "#FFD700", "#90EE90", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制左侧使用频率饼图
wedges, texts, autotexts = ax1.pie(sizes_freq, colors=colors_freq, autopct='%1.1f%%', startangle=90)
ax1.set_title('中国消费者使用防晒化妆品的频率')
# 调整图例位置，让标注更清晰
ax1.legend(wedges, labels_freq, title="使用频率", loc="center left", bbox_to_anchor=(1, 0.5))

# 绘制右侧价格接受度饼图（带3D效果，近似原图）
wedges2, texts2, autotexts2 = ax2.pie(sizes_price, colors=colors_price, autopct='%1.1f%%', startangle=90,
                                      explode=[0, 0, 0, 0.1], shadow=True)
ax2.set_title('中国消费者防晒化妆品价格接受度（以60g一瓶为例）')
ax2.legend(wedges2, labels_price, title="价格区间", loc="center left", bbox_to_anchor=(1, 0.5))

# 优化自动标注的文字颜色（区分深色/浅色切片）
for autotext in autotexts + autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()