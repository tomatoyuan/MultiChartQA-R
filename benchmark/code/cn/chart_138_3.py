import matplotlib.pyplot as plt

# 海底捞数据
haidilao_labels = ["一线", "新一线", "二线", "三线", "四线", "五线", "其他"]
haidilao_sizes = [17.3, 30.1, 21.7, 16.9, 8.5, 4.0, 1.5]
haidilao_provinces = {"广东省": 162, "浙江省": 111, "山东省": 77}
haidilao_colors = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

# 小龙坎数据
xiaolongkan_labels = ["一线", "新一线", "二线", "三线", "四线", "五线", "其他"]
xiaolongkan_sizes = [8.9, 18.8, 24.0, 8.3, 25.7, 13.0, 1.3]
xiaolongkan_provinces = {"安徽省": 76, "广东省": 62, "江苏省": 44}
xiaolongkan_colors = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制海底捞环形饼图
wedges, texts, autotexts = ax1.pie(haidilao_sizes, colors=haidilao_colors, autopct='%1.1f%%', startangle=90,
                                    wedgeprops=dict(width=0.4))
ax1.set_title('海底捞门店分布')
# 绘制省份文本框
province_text = "\n".join([f"{province}：{count}家" for province, count in haidilao_provinces.items()])
ax1.text(-1.3, 0.5, province_text, fontsize=10, bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
# 调整图例，放在饼图右侧
ax1.legend(wedges, haidilao_labels, title="城市线级", loc="center left", bbox_to_anchor=(1, 0.5))
# 让标注文字颜色更清晰（区分深色/浅色切片）
for autotext in autotexts:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

# 绘制小龙坎环形饼图
wedges2, texts2, autotexts2 = ax2.pie(xiaolongkan_sizes, colors=xiaolongkan_colors, autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.4))
ax2.set_title('小龙坎门店分布')
# 绘制省份文本框
province_text2 = "\n".join([f"{province}：{count}家" for province, count in xiaolongkan_provinces.items()])
ax2.text(1.3, 0.5, province_text2, fontsize=10, ha='right',
         bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
ax2.legend(wedges2, xiaolongkan_labels, title="城市线级", loc="center right", bbox_to_anchor=(-0.2, 0.5))
for autotext in autotexts2:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('2023年中国部分热门火锅品牌门店分布', fontsize=14)
plt.tight_layout()
plt.show()