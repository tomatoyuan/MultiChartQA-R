import matplotlib.pyplot as plt
import numpy as np

# 数据准备
drink_types = [
    "无糖碳酸饮料（如无糖可乐、元气森林系列、无糖苏打水等）",
    "无糖茶饮料（如东方树叶系列、无糖乌龙茶等）",
    "无糖果蔬汁（如NFC果汁、无糖蔬菜汁等）",
    "无糖含乳饮料（如无糖酸奶、无糖高钙奶等）",
    "其他无糖饮料（如无糖酸梅汁等）"
]
proportions = [76.07, 70.09, 46.16, 45.90, 11.31]  # 占比（%）

x = np.arange(len(drink_types))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向柱状图
bars = ax.barh(x, proportions, color='coral')
ax.set_title('2023年中国消费者喝过的无糖饮料类型', fontsize=14)
ax.set_xlabel('占比（%）')
ax.set_ylabel('无糖饮料类型')
ax.set_yticks(x)
ax.set_yticklabels(drink_types)

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', ha='left', va='center', color='black')

# 添加图例和样本来源说明
ax.legend(bars, ['占比'], loc='lower right')
ax.text(0.7, -0.2, '样本来源：草莓派数据调查与计算系统 (Strawberry Pie)', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()