import matplotlib.pyplot as plt
import numpy as np

# Data preparation
elements = [
    "Chinese traditional elements and national fashion style", "Zodiac elements", "Innovation and creativity",
    "Minimalism", "Technology elements", "Internet celebrity trendy", "Comic and anime", "Other"
]
percentages = [62.2, 41.6, 38.7, 37.4, 28.9, 23.8, 19.8, 0.3]

# Calculate the number of squares corresponding to each element
block_counts = [int(p / 3) + (1 if p % 3 > 1.5 else 0) for p in percentages]

# 增加图表宽度以适应右移的文本
fig, ax = plt.subplots(figsize=(14, 6))  # 宽度从10增加到14
ax.set_xlim(0, max(block_counts) + 15)  # 增大x轴范围，为右移文本留出空间
ax.set_ylim(0, len(elements) * 1.5)
ax.set_axis_off()  # Hide the axes

# Draw orange squares and annotations with right-shifted text
for i, (element, perc, blocks) in enumerate(zip(elements, percentages, block_counts)):
    # Draw squares
    for j in range(blocks):
        ax.add_patch(plt.Rectangle((j + 1, i * 1.5 + 0.3), 0.8, 0.8, color='orange'))

    # 文本右移：将x坐标从blocks + 2调整为blocks + 5
    # Draw the element name
    ax.text(blocks + 5, i * 1.5 + 0.7, element, fontsize=12, va='center')
    # Draw the percentage value (进一步右移以避免与元素名重叠)
    ax.text(blocks + 5 + len(element) * 0.3, i * 1.5 + 0.7, f'{perc}%', ha='left', va='center', fontsize=12, color='orange')

ax.set_title('Consumer preferences for product elements in Chinese New Year gift boxes in 2023', fontsize=14, y=1.05)
plt.tight_layout()
plt.show()