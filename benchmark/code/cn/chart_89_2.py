import matplotlib.pyplot as plt
import numpy as np

# 消费场景
scenarios = ["朋友聚会", "家庭聚会", "商务应酬", "一人独酌", "情侣约会"]
# 18-29岁占比（%），数据与图表一致
age18_29 = [39.2, 21.1, 22.5, 13.2, 3.9]
# 30岁及以上占比（%），数据与图表一致
age30_up = [43.7, 28.4, 15.7, 10.1, 2.2]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 6))

# 绘制水平条形图（18-29岁，绿色）
y = np.arange(len(scenarios))
bar_width = 0.35
bars1 = ax.barh(y + bar_width/2, age18_29, height=bar_width, color="#A4C639", label="18-29岁（%）")
# 绘制水平条形图（30岁及以上，蓝色）
bars2 = ax.barh(y - bar_width/2, age30_up, height=bar_width, color="#87CEEB", label="30岁及以上（%）")

# 添加数据标注（18-29岁）
for bar in bars1:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 添加数据标注（30岁及以上）
for bar in bars2:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 绘制商务应酬、一人独酌的黄色虚线框
# 找到商务应酬和一人独酌的索引
start_idx = scenarios.index("商务应酬")
end_idx = scenarios.index("一人独酌")
# 计算框的坐标
y_min = y[start_idx] - bar_width/2 - 0.1
y_max = y[end_idx] + bar_width/2 + 0.1
x_min = 0
x_max = max(max(age18_29), max(age30_up)) + 5  # 适当扩展x轴范围

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(scenarios)
# 设置x轴标签
ax.set_xlabel("占比（%）")
# 设置标题
ax.set_title("白酒消费场景（分年龄）", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()