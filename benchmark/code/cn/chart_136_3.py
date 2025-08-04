import matplotlib.pyplot as plt

# 串饰数据
charm_labels = ["700元以上", "500-700元", "350-500元", "350元以下"]
charm_sizes = [12.0, 23.0, 41.0, 24.0]
charm_colors = ["#E4725F", "#F6C85F", "#94B49F", "#92574C"]

# 手链数据
bracelet_labels = ["1000元以上", "600-1000元", "600元以下"]
bracelet_sizes = [14.0, 46.0, 40.0]
bracelet_colors = ["#E4725F", "#F6C85F", "#94B49F"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制串饰饼图
wedges, texts, autotexts = ax1.pie(charm_sizes, colors=charm_colors, autopct='%1.1f%%', startangle=90,
                                    wedgeprops=dict(width=0.4))
ax1.set_title('潘朵拉串饰中国价格分布')
# 调整图例，放在饼图右侧
ax1.legend(wedges, charm_labels, title="价格区间", loc="center left", bbox_to_anchor=(1, 0.5))
# 让标注文字颜色更清晰（区分深色/浅色切片）
for autotext in autotexts:
    autotext.set_color('blue' if autotext.get_position()[1] > 0.5 else 'black')

# 绘制手链饼图
wedges2, texts2, autotexts2 = ax2.pie(bracelet_sizes, colors=bracelet_colors, autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.4))
ax2.set_title('潘朵拉手链中国价格分布')
ax2.legend(wedges2, bracelet_labels, title="价格区间", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('blue' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()