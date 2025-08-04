import matplotlib.pyplot as plt

# 设置主类数据
main_labels = ['其他包装', '可持续包装']
main_sizes = [75, 25]
main_colors = ['#E0E0E0', '#8BC34A']

# 设置可持续包装内部细分类数据
inner_labels = ['重复使用包装', '其他可持续包装', '其他包装（不细分）']
inner_sizes = [10, 15, 75]
inner_colors = ['#AED581', '#A1887F', '#FFFFFF00']  # 第三项透明（让“其他包装”不再重复显示）

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))

# 外圈（主分类）
wedges1, _ = ax.pie(
    main_sizes,
    radius=1,
    labels=[f'{v}%' for v in main_sizes],
    colors=main_colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# 内圈（可持续包装细分类）
wedges2, _ = ax.pie(
    inner_sizes,
    radius=1 - 0.3,
    labels=['10%', '15%', ''],
    colors=inner_colors,
    startangle=0,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# 添加标题
plt.title('2020全球包装行业产品结构', fontsize=16, color='green', weight='bold')

# 图例说明
custom_legend = [
    plt.Line2D([0], [0], marker='o', color='w', label='其他包装', markerfacecolor='#E0E0E0', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='可持续包装', markerfacecolor='#8BC34A', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='重复使用包装', markerfacecolor='#AED581', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='其他可持续包装', markerfacecolor='#A1887F', markersize=12)
]
plt.legend(handles=custom_legend, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=10, frameon=False)

plt.tight_layout()
plt.show()