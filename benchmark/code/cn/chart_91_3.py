import matplotlib.pyplot as plt

# 外层饼图数据
outer_sizes = [25, 17, 75]
outer_labels = ['营收前10企业市场占有率 (%)', '营收前5企业市场占有率 (%)', '其他企业市场占有率 (%)']
outer_colors = ['#A4C639', '#87CEEB', '#D3D3D3']

# 内层饼图数据
inner_sizes = [25 + 17, 75]  # 前10（含前5）、其他
inner_labels = ['', '']
inner_colors = ['white', 'white']  # 内层空白圈

# 创建画布
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制外层饼图
outer_wedges, outer_texts, outer_autotexts = ax.pie(outer_sizes, labels=outer_labels, autopct='%1.1f%%',
                                                    colors=outer_colors, startangle=90,
                                                    textprops={'color': 'black'})
# 设置标题
ax.set_title('2021年中国杯壶行业市场集中度', fontsize=14, fontweight='bold', y=1.05)

# 让饼图保持圆形
ax.axis('equal')

plt.tight_layout()
plt.show()