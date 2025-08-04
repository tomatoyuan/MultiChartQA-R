import matplotlib.pyplot as plt
import numpy as np

# 招聘数字化服务需求类型
needs = ["高效筛选简历", "人才聚合搜集", "简化简历入库程序", "高效管理职位", 
         "精准岗位建模", "精准解析简历", "AI虚拟面试官"]
# 对应占比（%）
proportions = [35.47, 33.76, 33.55, 33.12, 32.69, 31.84, 29.70]

x = np.arange(len(needs))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(needs, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国企业对招聘数字化服务的需求')

plt.tight_layout()
plt.show()