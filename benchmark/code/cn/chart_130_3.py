import matplotlib.pyplot as plt
import numpy as np

# 睡眠质量问题类型
labels = ["睡眠浅", "入睡困难", "易醒", "嗜睡", "醒后感觉乏力", 
          "肌肉酸痛、关节不适", "睡眠呼吸障碍", "夜惊症", 
          "睡眠的时间太短", "多梦", "说梦话", "梦游症", "其他"]
# 各问题对应的占比（%）
proportions = [32.1, 28.0, 27.7, 26.5, 26.5, 
               24.5, 23.9, 21.9, 21.7, 20.6, 
               13.1, 10.3, 4.2]

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注，在柱子上方
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")

# 设置坐标轴
ax.set_ylabel("占比（%）")
ax.set_xlabel("睡眠质量问题类型")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')  # 旋转标签，避免重叠

ax.set_title("中国居民出现过的睡眠质量问题")

plt.tight_layout()
plt.show()