import matplotlib.pyplot as plt
import numpy as np

# 数据
sources = ["医生", "母婴专业媒体编辑", "普通同圈层妈妈网友", "身边朋友", "备孕产品品牌方", "KOL"]
percentages = [77.0, 61.1, 55.1, 44.2, 38.5, 20.4]

x = np.arange(len(sources))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange', label='信赖占比（%）')
ax.set_ylabel('信赖占比（%）')
ax.set_xlabel('备孕信息来源')
ax.set_xticks(x)
ax.set_xticklabels(sources)
ax.set_title('2023年中国备孕人群信赖的备孕信息来源')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()