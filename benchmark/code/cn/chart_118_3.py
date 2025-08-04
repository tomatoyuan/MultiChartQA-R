import matplotlib.pyplot as plt
import numpy as np

# 企业使用 AI 数字人的目的
purposes = [
    "提升工作效率、质量", "提升企业数字化程度", "降低劳动成本", 
    "用于产品代言/带货", "降低经济成本", "增强客户互动与体验", 
    "提升企业形象", "数据收集与分析", "创新技术应用展示"
]
# 对应占比（%）
proportions = [48.80, 43.09, 36.44, 35.37, 27.13, 23.80, 23.14, 16.22, 8.11]

x = np.arange(len(purposes))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(purposes, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国企业使用AI数字人的目的')

plt.tight_layout()
plt.show()