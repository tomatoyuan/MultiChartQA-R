import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["花胶", "玻尿酸水"]
# 透明质酸含量占比（mg/100g），数据大体一致即可
hyaluronic_acid = [230.0, 19.8]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, hyaluronic_acid, width=bar_width, color="#C6395C", label="透明质酸含量占比(mg/100g)")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title("花胶透明质酸含量", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()