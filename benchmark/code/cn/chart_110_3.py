import matplotlib.pyplot as plt
import numpy as np

# 考虑因素
factors = ["有声书的内容", "主播的声线及能力", "有声书的时长", "有声书是否由IP改编", "有声书的价格", "有声书的更新频率"]
# 对应占比（%）
proportions = [40.82, 38.70, 34.71, 34.57, 34.04, 33.38]

x = np.arange(len(factors))  # x轴坐标

fig, ax = plt.subplots(figsize=(8, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(factors)
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国有声书用户选择有声书首要考虑因素')

plt.tight_layout()
plt.show()