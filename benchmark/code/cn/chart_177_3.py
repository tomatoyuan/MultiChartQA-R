import matplotlib.pyplot as plt

# 中文显示支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 数据
labels = [
    "AI的功能越来越强大\n（42%）",
    "AI适度使用\n（23%）",
    "AI应与家庭教育相辅相成\n（22%）",
    "对AI持怀疑态度\n（13%）"
]
sizes = [42, 23, 22, 13]
colors = ['#FF0000', '#FF6666', '#FF9999', '#CCCCCC']

# 绘制环状图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.0f%%', startangle=90,
    colors=colors, wedgeprops=dict(width=0.4), textprops={'fontsize': 12}
)

# 添加中心文字
plt.text(0, 0.1, "87%", fontsize=26, fontweight='bold', ha='center')
plt.text(0, -0.1, "的家长对AI\n持积极态度", fontsize=14, ha='center')

# 设置为等比
ax.axis('equal')
plt.title("家长对于AI教育的态度", fontsize=16)
plt.tight_layout()
plt.show()