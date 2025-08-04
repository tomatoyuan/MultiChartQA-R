import matplotlib.pyplot as plt

# 功效分类及其占比
labels = ['增强免疫力', '抗疲劳', '护肝', '护眼', '助眠', '其他']
sizes = [42, 15, 13, 8, 2, 20]
colors = ['#0057FF', '#7DECF6', '#00B388', '#93B6FF', '#CED6F8', '#EDEDED']

# 绘制饼图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.0f%%',
    startangle=90, textprops={'fontsize': 10}, pctdistance=0.8
)

# 设置标题
ax.set_title("2023H1保健食品新产品注册功效分布", fontsize=14, fontweight='bold')

# 添加数据来源说明
plt.figtext(
    0.5, 0.01,
    '注释：抗疲劳对应保健食品中的“缓解体力疲劳”功能，护肝对应“对化学系肝损伤有辅助保护作用”功能，护眼对应“缓解视疲劳”功能\n数据来源：国家市场监督管理总局，公开资料整理',
    wrap=True, horizontalalignment='center', fontsize=9
)

plt.tight_layout()
plt.show()