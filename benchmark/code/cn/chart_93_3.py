import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 人群分类
groups = ["女性人群", "本科以上学历人群", "30岁以下人群", "一二线人群", "高收入人群", "高消费人群"]
# 数据类别（对应图例）
categories = ["(天猫国际) 美护发整体人群占比", "(天猫+淘宝) 美护发整体人群占比"]
# 修正数据结构：转置以匹配人群分类（6个类别）
data = np.array([
    [85, 55, 60, 65, 50, 40],  # 天猫国际：各人群占比
    [70, 35, 50, 55, 38, 20]   # 天猫+淘宝：各人群占比
]).T  # 转置后形状为 (6, 2)，与人群分类数量匹配

# 说明文字
annotation_text = "天猫国际拥有更多高\n学历、高消费人群"
# 箭头参数
arrowprops = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# 创建画布
fig, ax = plt.subplots(figsize=(10, 7))

# 绘制分组横向柱状图
y = np.arange(len(groups))
bar_height = 0.35
for i in range(len(categories)):
    offset = bar_height * i
    ax.barh(y + offset, data[:, i], height=bar_height, 
            color="#A4C639" if i==0 else "#EBD487",
            label=categories[i])

# 添加数据标注
for i in range(len(groups)):
    for j in range(len(categories)):
        width = data[i, j]
        ax.annotate(f'{width}%',
                    xy=(width, y[i] + bar_height*j),
                    xytext=(5, 0),  # 标注位置：右侧偏移 5
                    textcoords="offset points",
                    ha='left', va='center',
                    color='black')

# 设置y轴刻度和标签（居中显示分组）
ax.set_yticks(y + bar_height/2)
ax.set_yticklabels(groups)
# 设置x轴刻度（0-100%）
ax.set_xlim(0, 100)
ax.set_xticks([0, 50, 100])
# 设置标题
ax.set_title("美护发人群画像：天猫国际 vs 天猫+淘宝", 
             fontsize=16, fontweight="bold", y=1.03)

# 自定义图例
legend_elements = [Patch(facecolor="#A4C639", label=categories[0]),
                   Patch(facecolor="#EBD487", label=categories[1])]
ax.legend(handles=legend_elements, loc="upper right")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()