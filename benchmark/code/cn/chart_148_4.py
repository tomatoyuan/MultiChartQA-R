import matplotlib.pyplot as plt
import numpy as np

# 数据准备
brands = [
    "元气森林", "可口可乐", "农夫山泉", "东方树叶", 
    "百事可乐", "王老吉", "维他奶", "三得利", 
    "怡泉", "屈臣氏", "依能", "名仁", "灵汽"
]
proportions = [49.54, 42.52, 42.38, 34.70, 
               34.44, 23.05, 21.19, 20.00, 
               14.83, 14.70, 9.93, 9.93, 9.27]  # 占比（%）

x = np.arange(len(brands))

fig, ax = plt.subplots(figsize=(10, 8))

# 绘制横向柱状图
bars = ax.barh(x, proportions, color='coral')
ax.set_title('2023年中国消费者偏好的无糖饮料品牌', fontsize=14)
ax.set_xlabel('占比（%）')
ax.set_ylabel('无糖饮料品牌')
ax.set_yticks(x)
ax.set_yticklabels(brands)
ax.set_xlim(0, 55)  # 调整x轴范围，适配最大占比（49.54%）

# 添加数值标注
for i, prop in enumerate(proportions):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# 添加图例和样本来源（若需还原原图，可调整位置）
ax.legend(bars, ['占比'], loc='lower right')
ax.text(0.8, -0.12, '样本来源：草莓派数据调查与计算系统 (Strawberry Pie)', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()