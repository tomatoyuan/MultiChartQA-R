# 图表3：不良反应的应对措施（高亮特定扇区的环形图）

# 数据
labels = [
    '注意休息多喝水', '改善饮食', '自行用药',
    '服用益生菌调理', '不予处理', '立即去正规医院就诊', '向家人和朋友寻求建议'
]
sizes = [18.5, 17.4, 20.3, 15.0, 2.9, 12.4, 13.5]
highlight_index = 3  # 高亮“服用益生菌调理”

# 定义颜色和突出项
colors = ['#555', '#666', '#777', '#0056d6', '#999', '#bbb', '#99c']
explode = [0.01 if i == highlight_index else 0 for i in range(len(labels))]

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=None, autopct='%1.1f%%', startangle=90,
    counterclock=False, colors=colors,
    explode=explode, wedgeprops=dict(width=0.4, edgecolor='white'),
    textprops={'fontsize': 10}
)

# 设置图例
ax.legend(wedges, labels, title="应对方式", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# 中心文本
ax.text(0, 0, '出现不良反应\n的应对措施', ha='center', va='center', fontsize=12, fontweight='bold')

# 标题
ax.set_title("出现不良反应的应对措施（用户占比）", fontsize=14)
plt.tight_layout()
plt.show()