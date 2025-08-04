import matplotlib.pyplot as plt
import numpy as np

# 特长发展方向数据
skill_labels = ["热爱即可\n不求赚钱", "希望成为\n主业或副业"]
skill_sizes = [32, 68]
skill_colors = ["#D3D3D3", "#87CEEB"]

# 未来生活城市数据
city_labels = ["一线城市", "二线城市", "三线以下", "没想好"]
city_sizes = [36, 42, 16, 6]
city_colors = ["#A4C639", "#A4C639", "#A4C639", "#A4C639"]  # 统一绿色系，可微调

# 创建画布（两列布局）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# 绘制特长发展方向饼图
ax1.pie(skill_sizes, labels=skill_labels, colors=skill_colors, startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='white'))  # 环形饼图
ax1.set_title("特长发展方向", fontsize=12, fontweight="bold", y=-0.1)  # 标题下移

# 绘制未来生活城市柱状图
x = np.arange(len(city_labels))
bar_width = 0.6
ax2.bar(x, city_sizes, color=city_colors, width=bar_width)

# 添加城市柱状图数据标注
for bar in ax2.patches:
    height = bar.get_height()
    ax2.annotate(f'{height}%',
                 xy=(bar.get_x() + bar_width/2, height),
                 xytext=(0, 3),  # 标注位置：上方偏移 3
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color='black')

# 设置城市柱状图x轴刻度和标签
ax2.set_xticks(x)
ax2.set_xticklabels(city_labels)
ax2.set_title("未来生活城市", fontsize=12, fontweight="bold", y=-0.2)  # 标题下移

# 美化：隐藏饼图和柱状图的边框
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# 调整子图间距
plt.subplots_adjust(wspace=0.5)

plt.show()