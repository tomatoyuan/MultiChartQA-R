import matplotlib.pyplot as plt
import numpy as np

# Channels for getting information about figurines
channels = ["Payment platforms", "Introductions from relatives and friends", "Short - video platforms (Douyin, Kuaishou, etc.)",
            "Content - sharing platforms (Xiaohongshu, Weibo, Douban, Zhihu, etc.)", "Video - sharing platforms (Bilibili, Tencent Video, etc.)"]
# Corresponding proportions (%)
proportions = [24.31, 28.94, 41.20, 50.23, 52.55]

y = np.arange(len(channels))  # y - axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('Proportion (%)')
ax.set_title('Channels for Chinese figurine consumers to get information about figurines in 2025')

plt.tight_layout()
plt.show()