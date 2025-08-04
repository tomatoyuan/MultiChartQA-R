import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 人群分类
groups = ["新锐白领", "Gen Z", "小镇青年", "小镇中老年", "资深中产", "精致妈妈", "都市蓝领", "都市银发"]
# 数据类别（对应图例）
categories = ["(天猫国际) 美护发整体人群占比", "(淘宝天猫) 美护发整体人群占比"]
# 模拟数据（可调整），范围 0-25（示例值）
data = np.array([
    [22, 12],  # 新锐白领
    [20, 16],  # Gen Z
    [18, 17],  # 小镇青年
    [15, 24],  # 小镇中老年
    [12, 8],   # 资深中产
    [10, 5],   # 精致妈妈
    [8, 15],   # 都市蓝领
    [3, 4]     # 都市银发
]).T  # 转置后形状 (2, 8)，匹配平台-人群结构

# 创建画布
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制分组柱状图
x = np.arange(len(groups))
bar_width = 0.35
for i in range(len(categories)):
    offset = bar_width * i
    ax.bar(x + offset, data[i], width=bar_width, 
           color="#A4C639" if i==0 else "#87CEEB",
           label=categories[i])

# 添加数据标注
for i in range(len(groups)):
    for j in range(len(categories)):
        height = data[j][i]
        ax.annotate(f'{height}%',
                    xy=(x[i] + bar_width*j, height),
                    xytext=(0, 3),  # 标注位置：上方偏移 3
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# 设置x轴刻度和标签
ax.set_xticks(x + bar_width/2)
ax.set_xticklabels(groups, rotation=45, ha='right')  # 旋转标签避免重叠
# 设置y轴刻度（0-40%）
ax.set_ylim(0, 40)
ax.set_yticks([0, 20, 40])
# 设置标题
ax.set_title("天猫国际：美护发阿里大快消八大人群占比", 
             fontsize=16, fontweight="bold", y=1.05)

# 自定义图例
legend_elements = [Patch(facecolor="#A4C639", label=categories[0]),
                   Patch(facecolor="#87CEEB", label=categories[1])]
ax.legend(handles=legend_elements, loc="upper right")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()