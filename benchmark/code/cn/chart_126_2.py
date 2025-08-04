import matplotlib.pyplot as plt
import numpy as np

# 左侧区域分布数据
regions = ["华东", "华南", "西南", "华北", "华中", "西北", "东北", "港澳台"]
proportions_region = [24.2, 21.5, 17.6, 17.0, 9.8, 6.8, 3.0, 0.1]

# 右侧城市分布数据
city_types = ["一线城市", "新一线城市", "二线城市", "三线城市", "四线及其他城市"]
proportions_city = [20.2, 27.4, 29.6, 14.8, 8.0]
colors_city = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513", "#808000"]

fig = plt.figure(figsize=(16, 8))
# 左侧子图（区域分布）
ax1 = fig.add_subplot(121)
x = np.arange(len(regions))
bars = ax1.bar(x, proportions_region, color=plt.cm.autumn(np.linspace(0, 1, len(regions))))
for i, proportion in enumerate(proportions_region):
    ax1.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax1.set_ylabel("占比（%）")
ax1.set_xlabel("区域")
ax1.set_xticks(x)
ax1.set_xticklabels(regions)
ax1.set_title("2024年中国消费者区域分布")

# 右侧子图（城市分布）
ax2 = fig.add_subplot(122)
wedges, texts, autotexts = ax2.pie(proportions_city, labels=city_types, colors=colors_city, autopct="%1.1f%%", 
                                  pctdistance=0.8, startangle=90)
for autotext in autotexts:
    autotext.set_color("white")
ax2.set_title("2024年中国消费者城市分布")

plt.tight_layout()
plt.show()