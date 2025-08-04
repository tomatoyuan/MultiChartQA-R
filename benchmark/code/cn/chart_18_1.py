import matplotlib.pyplot as plt
import numpy as np

# 数据定义
years = np.array([1950, 1960, 1970, 1980, 1990, 2016])
costs = np.array([10, 100, 500, 3000, 3000, 25])  # 2016年为示意性数值
labels = [
    "10元\n相当于当月1/5收入\n+组织证明",
    "100元\n相当于2个月收入\n+一套家具",
    "500元\n相当于15个月收入\n+三转一响",
    "3000元\n相当于30个月收入\n+冰箱、电视、洗衣机",
    "3000元\n相当于30个月收入\n+三金、婚宴、婚纱照",
    ">25万\n相当于30个月收入"
]

# 创建图形和坐标轴，增加顶部空间
fig, ax = plt.subplots(figsize=(12, 8))
fig.subplots_adjust(top=0.85)  # 调整顶部间距

# 绘制渐变色柱状图（使用颜色映射）
cmap = plt.cm.viridis
norm = plt.Normalize(min(costs), max(costs))
colors = [cmap(norm(c)) for c in costs]
bars = ax.bar(np.arange(len(years)), costs, width=0.6, color=colors, edgecolor='gray')

# 设置标题和标签
ax.set_title("中国结婚成本变迁史", fontsize=18, fontweight='bold', pad=30)
ax.set_ylabel("结婚成本（单位：元，2016年为示意性数值）", fontsize=12)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, fontsize=11)

# 添加网格线和背景色
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f8f9fa')

# 优化文本标注 - 使用方框标注替代直接在柱上标注
for i, (bar, label) in enumerate(zip(bars, labels)):
    height = bar.get_height()
    ax.annotate(label,
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 15),  # 垂直偏移
                textcoords="offset points",
                ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                fontsize=9)

# 添加图例说明
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1, frameon=False)

plt.tight_layout()
plt.show()