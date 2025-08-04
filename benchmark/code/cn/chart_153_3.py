# 图表 1.2-10：毛孔粗大带来的其他皮肤问题

labels = [
    "皮肤易出油", "黑头闭口多", "肤色暗沉",
    "粗糙", "爆痘", "泛红"
]
values = [77.33, 74.33, 61.33, 55.33, 45.00, 34.33]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=['#245b5b'] * 3 + ['#b4d4d4'] * 3)

# 添加百分比标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.2f}%', va='center', fontsize=10)

ax.set_xlabel('比例（%）')
ax.set_title("图 1.2-10 毛孔粗大带来的其他皮肤问题")
fig.text(0.9, 0.02, "N=300", ha='right', fontsize=10)

plt.tight_layout()
plt.show()