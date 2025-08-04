import matplotlib.pyplot as plt
import numpy as np

# 数据定义
periods = ['2022年6-8月', '2022年9-12月', '2023年1-3月', '2023年4-6月', '2023年7-9月', '2023年10-12月']
episodes = [420, 1402, 1848, 2686, 3321, 3532]  # 发片集数（右轴）
titles = [19, 64, 83, 116, 150, 153]           # 发片部数（左轴）

x = np.arange(len(periods))
bar_width = 0.5

# 创建图形
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# 柱状图（左轴）：发片部数
bars = ax1.bar(x, titles, width=bar_width, color='#ff2d55', label='发片部数')

# 添加柱顶标签
for i, val in enumerate(titles):
    ax1.text(x[i], val - 12, str(val), ha='center', fontsize=10, color='black')

# 折线图（右轴）：发片集数
ax2.plot(x, episodes, color='#586173', linewidth=2.5, marker='o', markersize=25, label='发片集数', zorder=5)

# 添加节点数字标签
for i, val in enumerate(episodes):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# 设置坐标轴与标签
ax1.set_xticks(x)
ax1.set_xticklabels(periods, fontsize=11)
ax1.set_ylabel('发片部数', fontsize=12, color='#ff2d55')
ax2.set_ylabel('发片集数', fontsize=12, color='#586173')

ax1.set_ylim(0, 200)     # 左轴（部数）
ax2.set_ylim(0, 4000)    # 右轴（集数）

# 标题
plt.title('2022年6月-2023年12月\n广电总局微短剧发行许可数', fontsize=14, fontweight='bold', pad=20)

# 图例合并左右轴
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# 网格 & 美化
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()