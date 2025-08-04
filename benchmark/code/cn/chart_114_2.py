import matplotlib.pyplot as plt
import numpy as np

# 健康指标
indicators = ["HPV", "肿瘤标志物", "幽门螺旋杆菌", "临床检查项目（血压、BMI、口腔、耳鼻喉）", 
              "功能检查（放射影像、彩超、心电图）", "生化及实验室检测（血常规、尿常规、生化、肝功、肾功、甲功、血糖）"]
# 对应占比（%）
proportions = [23.77, 30.67, 35.57, 44.83, 46.28, 61.89]

y = np.arange(len(indicators))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(indicators)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国健康体检消费者最关注的健康指标')

plt.tight_layout()
plt.show()