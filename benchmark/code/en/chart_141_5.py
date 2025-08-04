import matplotlib.pyplot as plt
import numpy as np

# Data
platforms = ["Maternal and infant apps \n(e.g., Mama.cn Pregnancy, Babytree Pregnancy, Mama Community)",
             "Women's health management apps (e.g., Meiyou)",
             "Content community platforms (e.g., Xiaohongshu)",
             "Social platforms (e.g., WeChat groups)",
             "Short - video platforms (e.g., Douyin)"]
percentages = [61.5, 16.6, 12.0, 5.0, 4.9]

x = np.arange(len(platforms))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart
bars = ax.barh(x, percentages, color='orange', label='Contact proportion (%)')
ax.set_xlabel('Contact proportion (%)')
ax.set_ylabel('Platform types')
ax.set_yticks(x)
ax.set_yticklabels(platforms)
ax.invert_yaxis()  # Make the first platform appear at the top
ax.set_title('Distribution of platforms most frequently accessed by Chinese pre - pregnancy population for pre - pregnancy products in 2023')

# Add numerical labels
for bar in bars:
    length = bar.get_width()
    ax.text(length + 1, bar.get_y() + bar.get_height() / 2,
            f'{length}%', ha='left', va='center')

plt.tight_layout()
plt.show()