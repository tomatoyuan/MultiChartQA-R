import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# 年份
years = ["2020", "2030e", "2040e", "2050e", "2060e"]
# 氢能源需求量（万吨），数据与图表一致
demand = [3342, 3715, 5276, 9690, 13030]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, demand, width=bar_width, color="#C6395A")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")
    
# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴标签
ax.set_ylabel("中国氢能源需求量（万吨）")
# 设置标题
ax.set_title("2020-2060年中国氢能源需求量", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()