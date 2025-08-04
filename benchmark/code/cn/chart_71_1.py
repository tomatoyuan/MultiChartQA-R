import matplotlib.pyplot as plt
import numpy as np

# 类别及数据
categories = [
    "体育用品及相关产品制造", "体育用品及相关产品销售", "体育场地和设施管理",
    "体育教育与培训", "体育健身休闲活动", "其他体育服务",
    "体育管理活动", "体育传媒与信息服务", "体育经纪与代理",
    "体育竞赛表演活动", "体育场地设施建设"
]
data = np.array([44.9, 16.5, 7.9, 7.4, 5.8, 5.7, 3.2, 3.1, 1.2, 1.0, 3.5])

# 构造伪时间轴
x = np.linspace(0, 10, 100)
stack_data = np.array([np.ones_like(x) * v for v in data])

# 配色增强（彩色+柔和）
colors = [
    "#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF",
    "#A0C4FF", "#BDB2FF", "#FFC6FF", "#FFFFFC", "#D0F4DE", "#B0D0D3"
]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制堆积面积图
stacked = ax.stackplot(x, stack_data, labels=categories, colors=colors, alpha=0.95)

# 计算中间高度位置（用于添加文本）
cumsum_data = np.cumsum(stack_data, axis=0)
mid_height = cumsum_data - stack_data / 2

# 添加百分比文本，交替左右排布
for i in range(len(categories)):
    y_mid = mid_height[i, len(x)//2]  # 取中间点的高度
    align = 'right' if i % 2 == 0 else 'left'
    x_pos = 2 if i % 2 == 0 else 8  # 左右分布

    ax.text(
        x_pos, y_mid,
        f"{data[i]}% {categories[i]}",
        fontsize=9,
        ha=align,
        va='center',
        color='black',
        fontweight='bold'
    )

# 标题和图例
ax.set_title("2020年中国体育产业构成情况（堆积面积图）", fontsize=14, fontweight="bold", pad=20)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=9, frameon=False)

# 美化图表
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()