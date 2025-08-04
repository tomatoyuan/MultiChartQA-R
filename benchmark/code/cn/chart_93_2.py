import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 分组类别
groups = ["成交额同期增长", "件单价同期增长"]
# 数据类别（对应图例）
categories = ["美护发整体 (天猫国际)", "美护发整体 (天猫+淘宝)"]
# 模拟数据（可调整）
data = [[35, 25],  # 成交额同期增长：天猫国际、天猫+淘宝
        [18, 10]]  # 件单价同期增长：天猫国际、天猫+淘宝

# 说明文字
annotation_text = "天猫国际在成交额同期增长、\n件单价同期增长上优势明显"
# 箭头参数
arrowprops = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制分组柱状图
x = np.arange(len(groups))
bar_width = 0.35
for i in range(len(categories)):
    offset = bar_width * i
    ax.bar(x + offset, data[i], width=bar_width, 
           color="#C63974" if i==0 else "#87CEEB",
           label=categories[i])

# 添加数据标注
for i in range(len(groups)):
    for j in range(len(categories)):
        height = data[j][i]
        ax.annotate(f'{height}%',
                    xy=(x[i] + bar_width*j, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# 设置x轴刻度和标签
ax.set_xticks(x + bar_width/len(categories))
ax.set_xticklabels(groups)
# 设置y轴刻度
ax.set_ylim(0, 40)
# 设置标题
ax.set_title("2021年3月&2022年3月中国美护发整体：近1个月同比去年同期增长情况", 
             fontsize=14, fontweight="bold", y=1.1)

# 自定义图例（避免自动生成的图例顺序问题）
legend_elements = [Patch(facecolor="#C63974", label=categories[0]),
                   Patch(facecolor="#87CEEB", label=categories[1])]
ax.legend(handles=legend_elements, loc="upper right")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()