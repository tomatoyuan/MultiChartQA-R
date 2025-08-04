import matplotlib.pyplot as plt
import numpy as np

# 短视频平台名称
platforms = ["抖音", "快手", "小红书", "微信视频号", "B站", "西瓜视频", "微博", "皮皮虾", "秒拍"]
# 各平台用户使用占比（%）
percentages = [46.80, 35.93, 33.16, 31.66, 28.04, 25.59, 15.35, 14.07, 12.05]

x = np.arange(len(platforms))  # 用于设置柱状图的 x 轴位置

fig, ax = plt.subplots()
bars = ax.bar(x, percentages, color='orange')

# 在每个柱子上标注数值
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height,
            f'{height}',
            ha='center', va='bottom')

# 设置 x 轴刻度标签为平台名称
ax.set_xticks(x)
ax.set_xticklabels(platforms)
# 设置图表标题和坐标轴标签
ax.set_title('2025年中国用户使用过的短视频平台')
ax.set_ylabel('占比 (%)')

plt.show()