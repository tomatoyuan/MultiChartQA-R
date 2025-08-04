import matplotlib.pyplot as plt
import numpy as np

# 满意度类别
categories = ["非常满意", "满意", "一般", "不满意"]
# 对应占比（%），数据与图表一致
percentages = [14.5, 45.7, 32.7, 7.1]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 绘制红色边框圈出“非常满意”和“满意”
x1, y1 = bars[0].get_xy()
x2, y2 = bars[1].get_xy() + np.array([bars[1].get_width(), bars[1].get_height()])
rect = plt.Rectangle((x1 - 0.1, y1 - 0.1), x2 - x1 + 0.2, y2 - y1 + 0.2,
                     fill=False, edgecolor='red', linewidth=2, linestyle='--')
ax.add_patch(rect)

# 添加说明文本
ax.text(0.7, 0.9, "近6成居民对目前健康状态表示满意",
        transform=ax.transAxes, fontsize=12, color='red', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签
ax.set_ylabel("健康满意度评价占比（%）")
# 设置标题
ax.set_title("2022年中国居民健康满意度", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()