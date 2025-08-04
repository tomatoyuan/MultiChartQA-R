import matplotlib.pyplot as plt
import numpy as np

# 左侧饼图数据
pie_labels = ["两年", "三年", "四年及以上", "一年之内"]
pie_sizes = [49.0, 33.7, 9.3, 8.0]
pie_colors = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

# 右侧柱状图数据
bar_factors = ["性能", "屏幕尺寸", "电池续航", "品牌", "运行内存", "价格", "拍照功能", "存储容量", "其他"]
bar_proportions = [57.6, 57.0, 54.2, 47.2, 41.8, 38.4, 34.3, 31.1, 0.2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 左侧饼图
wedges, texts, autotexts = ax1.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct="%1.1f%%", startangle=90)
for autotext in autotexts:
    autotext.set_color("white")
ax1.set_title("中国消费者换手机的频率")

# 右侧柱状图
x = np.arange(len(bar_factors))
bars = ax2.bar(x, bar_proportions, color="#FF8C00")
for i, proportion in enumerate(bar_proportions):
    ax2.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax2.set_ylabel("占比（%）")
ax2.set_xlabel("考虑因素")
ax2.set_xticks(x)
ax2.set_xticklabels(bar_factors, rotation=45)
ax2.set_title("中国消费者选择手机时考虑的因素")

plt.tight_layout()
plt.show()