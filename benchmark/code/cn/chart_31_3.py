import matplotlib.pyplot as plt
import numpy as np

# 数据
age_groups = ['25岁以下', '25岁 - 40岁', '40岁以上']
percentages = [18, 37, 45]

# 绘制柱状图
x = np.arange(len(age_groups))
width = 0.5

fig, ax = plt.subplots(figsize=(8, 6))
rects = ax.bar(x, percentages, width, color=['#FF7F50', '#FFD700', '#4B0082'])

# 添加标题和标签
ax.set_title('网络传销套路TOP5 - 以“善心汇”等为典型代表的网络传销事件年龄分布', fontsize=14, fontweight='bold')
ax.set_xlabel('年龄分组', fontsize=12)
ax.set_ylabel('搜索占比（%）', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(age_groups)

# 在柱子上标注百分比
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# 补充显示相关搜索次数信息（可在标题或文本框等展示，这里用文本框示例）
search_info = f'相关搜索次数：32.2万'
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
ax.text(0.02, 0.95, search_info, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()