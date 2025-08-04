import matplotlib.pyplot as plt

# 数据
labels = ['面料柔软', '贴合亲肤', '透气，保持干燥', '轻盈，易携带', '弹性，方便伸展', '保暖']
values = [75, 72, 69, 66, 57, 55]
colors = ['#c49e6c', '#b88d59', '#a87d4a', '#98703d', '#88612f', '#7a5325']

# 创建柱状图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# 图表美化
ax.set_title("消费者对舒适度的具体要求（柱状图形式展示）", fontsize=14)
ax.set_ylabel("占比（%）")
ax.set_ylim(0, 80)
plt.xticks(rotation=30)
plt.tight_layout()

# 添加数据来源说明
plt.figtext(0.5, -0.05,
            "数据来源：CBNData2024年5月中国奢华户外服饰流行趋势的调研\n数据说明：请问您对户外服饰的舒适度有以下哪些具体要求？N=571",
            wrap=True, horizontalalignment='center', fontsize=10)

plt.show()