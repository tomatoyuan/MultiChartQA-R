import matplotlib.pyplot as plt
import numpy as np

# 数据类别
user_types = ["膏剂用户", "非膏剂用户"]
# 年龄段标签
age_labels = ["95后", "90后", "85后", "85前"]
# 修正数据结构：每个子列表代表一种用户类型在各年龄段的分布
data = [
    [36.5, 32.5, 18.9, 12.2],  # 膏剂用户
    [33.1, 29.0, 21.6, 16.4]   # 非膏剂用户
]
# 颜色设置
colors = ["#A4C639", "#8DB328", "#7EA11E", "#668718"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制堆积条形图
x = np.arange(len(user_types))
bar_width = 0.6

# 对每个用户类型分别绘制堆积条
for i, user_data in enumerate(data):
    bottom = 0
    for j, value in enumerate(user_data):
        ax.bar(
            x[i], value, bar_width, bottom=bottom, 
            color=colors[j], label=age_labels[j] if i == 0 else "",  # 只在第一次绘制时添加图例
            edgecolor="white"
        )
        # 在条中间添加数据标签
        ax.text(
            x[i], bottom + value/2, f"{value}%",
            ha='center', va='center', color='white', fontweight='bold'
        )
        bottom += value

# 设置坐标轴和标题
ax.set_xticks(x)
ax.set_xticklabels(user_types, fontsize=12)
ax.set_ylabel('百分比 (%)', fontsize=12)
ax.set_title('宠物主年龄分布（按用户类型）', fontsize=16, pad=15)

# 设置y轴范围
ax.set_ylim(0, 100)

# 添加图例（去掉重复项）
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right', bbox_to_anchor=(1.2, 1))

# 美化图表
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()