import matplotlib.pyplot as plt
import numpy as np

# Information channels
channels = ["New media content platforms (e.g., WeChat, official accounts, etc.)", "Comprehensive e - commerce platforms (e.g., Taobao, JD.com, etc.)", "Content sharing platforms (e.g., Xiaohongshu, Weibo, etc.)", 
            "Video sharing platforms (e.g., Bilibili, etc.)", "Short - video live - streaming platforms", "Offline brand stores", "Brand official websites", "Outdoor advertisements (wall and building advertisements, etc.)", 
            "Introductions from relatives and friends", "Subway or elevator advertisements"]
# Corresponding proportions (%)
proportions = [36.43, 34.27, 32.36, 30.70, 27.90, 26.75, 25.86, 24.20, 21.40, 20.25]

y = np.arange(len(channels))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('Proportion (%)')
ax.set_title('Information channels for Chinese consumers to learn about smart products in 2025')

plt.tight_layout()
plt.show()