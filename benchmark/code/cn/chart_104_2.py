import matplotlib.pyplot as plt
import numpy as np

# 课程名称
courses = ["键盘乐器（钢琴、管风琴、手风琴、电子琴等）", "弦乐器（提琴、吉他、二胡、古筝、琵琶等）", 
           "木管乐器（长笛、唢呐、双簧管、萨克斯管等）", "打击乐器（木琴、小鼓、大鼓、快板、扬琴等）", 
           "铜管乐器（小号、短号、长号、圆号、大号等）", "声乐"]
# 对应占比
proportions = [40.08, 35.22, 31.31, 29.82, 27.94, 17.95]

y = np.arange(len(courses))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平条形图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(courses)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国用户主要报名课程')

plt.show()