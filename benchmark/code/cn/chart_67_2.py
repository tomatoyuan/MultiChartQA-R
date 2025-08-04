import matplotlib.pyplot as plt
import numpy as np

# 行业名称
industries = ["科技", "金融", "专业服务", "制造业", "房地产", "医药与生命科学"]
# 对应数据（占比）
data = [33.6, 21.9, 8.8, 8.2, 6.0, 4.1]
# 颜色设置，贴近原图绿色系
colors = ["#A4C639"] * len(industries)

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制水平条形图
y = np.arange(len(industries))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=colors, edgecolor="white")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(industries)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2021年写字楼主力租户租赁需求占比", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.show()