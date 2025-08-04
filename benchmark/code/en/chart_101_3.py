import matplotlib.pyplot as plt
import numpy as np

# Data preparation
content_types = ["Short videos", "Live broadcasts", "Graphics and texts", "Audio", "Others"]
proportions = [75.7, 25.6, 22.0, 13.2, 7.6]  # Proportion (%)
colors = ["#ff7f27"]  # Orange, similar to the original image color scheme

x = np.arange(len(content_types))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart
bars = ax.barh(x, proportions, color=colors * len(content_types))
ax.set_title('Distribution of content types consumed by knowledge - paying users in 2022', fontsize=14)
ax.set_xlabel('Proportion (%)')
ax.set_ylabel('Content types')
ax.set_yticks(x)
ax.set_yticklabels(content_types)
ax.set_xlim(0, 80)  # Adjust the x - axis range to fit the maximum proportion (75.7%)

# Add numerical annotations
for i, prop in enumerate(proportions):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

plt.tight_layout()
plt.show()