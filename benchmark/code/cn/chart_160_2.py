import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm


# 数据
labels = [
    "掉粉50W以上", "掉粉50W-掉粉30W", "掉粉30W-掉粉10W", "掉粉10W-0",
    "0-涨粉10W", "涨粉10W-涨粉30W", "涨粉30W-涨粉50W", "涨粉50W以上"
]
values = [0.3, 0.4, 12.7, 38.3, 14.1, 14.1, 7.8, 12.2]
colors = ['#a0c8f0'] * 4 + ['#c09ee6'] * 4

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(range(len(labels)), values, color=colors)

# 添加数值标签
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{values[i]}%", va='center', fontsize=10)

# 添加分组注释
ax.text(40, 1.5, "掉粉达人\n占51.7%", fontsize=12, color='white', backgroundcolor='#619de2', ha='center', va='center')
ax.text(40, 6.5, "涨粉达人\n占48.3%", fontsize=12, color='white', backgroundcolor='#a460e8', ha='center', va='center')

# 添加虚线分界
ax.axhline(y=3.5, color='orange', linestyle='--', linewidth=2)
ax.text(35, 5, '平均涨粉量35.1W', fontsize=13, weight='bold')

# 格式设置
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlim(0, 60)
ax.set_xlabel("占比（%）")
ax.set_title("涨跌粉区间分布")

plt.tight_layout()
plt.show()