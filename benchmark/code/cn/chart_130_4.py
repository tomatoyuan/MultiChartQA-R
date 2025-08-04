import matplotlib.pyplot as plt
import numpy as np

# 数据
causes = ["情绪原因", "睡前使用手机过久", "工作压力", "个人身体健康问题", 
          "生活压力", "环境问题", "饮食问题", "睡眠姿势不正确"]
proportions = [47.3, 37.7, 37.4, 32.7, 32.0, 30.8, 27.7, 21.9]

y = np.arange(len(causes))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注，在柱子右侧
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center')

ax.set_yticks(y)
ax.set_yticklabels(causes)
ax.set_xlabel('占比（%）')
ax.set_title('中国居民出现睡眠质量问题的主要原因')

plt.tight_layout()
plt.show()