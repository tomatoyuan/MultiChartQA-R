import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2019", "2020", "2021"]
# 女性综艺题材数量，数据与图表一致
quantity = [4, 7, 10]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, quantity, width=bar_width, color="#C6395A")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")
    
# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title("SVC-2019-2021年女性综艺题材趋势", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()