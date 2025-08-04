import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["花胶", "蓝莓", "越桔", "蓝莓果", "野生莓"]
# 抗氧化能力（VE含量mg/100g），数据大体一致即可
antioxidant = [1.52, 0.91, 0.45, 0.33, 0.27]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, antioxidant, width=bar_width, color="#399CC6", label="抗氧化能力（VE含量mg/100g）")

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
# 设置y轴标签
ax.set_ylabel("抗氧化能力（VE含量mg/100g）")
# 设置标题
ax.set_title("花胶的抗氧化能力", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()