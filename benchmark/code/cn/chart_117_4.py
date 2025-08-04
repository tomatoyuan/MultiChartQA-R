import matplotlib.pyplot as plt
import numpy as np

# 智能家居功能
functions = [
    "智能灯光控制系统", "智能安全控制系统", "智能窗帘控制系统", 
    "智能环境监测系统", "智能家庭影音控制系统", "远程家电控制系统", 
    "智能语音助手", "一键控制情景模式", "背景音乐系统", "能源管理系统"
]
# 对应占比（%）
proportions = [35.40, 35.24, 31.59, 31.59, 30.79, 29.84, 29.84, 29.52, 22.70, 21.75]

x = np.arange(len(functions))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方居中位置
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(functions, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国消费者感兴趣的智能家居功能')

plt.tight_layout()
plt.show()