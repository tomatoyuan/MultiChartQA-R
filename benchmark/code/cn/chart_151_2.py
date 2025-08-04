# 图表2：健康膳食品类占比 + 增速（饼图+柱状图组合）

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [1, 1.2]})
fig.suptitle('整体线上 | 保健膳食分品类占比及销售额增长率% | MAT2406', fontsize=14)

# 饼图数据
labels = ['膳食营养补充食品', '传统滋补']
sizes = [74.9, 25.1]
colors = ['#003399', '#99bbff']
explode = (0, 0.05)

# 饼图（圆环）
wedges, texts, autotexts = ax1.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False,
    colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), explode=explode, textprops={'fontsize': 10}
)
ax1.set_title('品类占比')

# 柱状图数据
sub_categories = ['保健膳食', '膳食营养补充食品', '传统滋补']
growth_rates = [10.1, 11.5, 5.9]
bar_colors = ['#002060', '#0056d6', '#7faaff']

bars = ax2.bar(sub_categories, growth_rates, color=bar_colors)

# 添加数值标签
for bar, value in zip(bars, growth_rates):
    ax2.text(bar.get_x() + bar.get_width()/2, value + 0.3, f'{value}%', ha='center', va='bottom', fontsize=11)

# 样式细节
ax2.set_ylim(0, 13)
ax2.set_ylabel('同比增长率 (%)')
ax2.set_title('销售额增长率')
ax2.grid(axis='y', linestyle='--', alpha=0.5)
ax2.set_facecolor('#f5f7fa')

plt.tight_layout()
plt.show()