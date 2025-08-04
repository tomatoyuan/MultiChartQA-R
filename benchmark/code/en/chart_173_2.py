import matplotlib.pyplot as plt
import numpy as np

# Data definition
periods = ['Jun - Aug 2022', 'Sep - Dec 2022', 'Jan - Mar 2023', 'Apr - Jun 2023', 'Jul - Sep 2023', 'Oct - Dec 2023']
episodes = [420, 1402, 1848, 2686, 3321, 3532]  # Number of released episodes (right y - axis)
titles = [19, 64, 83, 116, 150, 153]           # Number of released titles (left y - axis)

x = np.arange(len(periods))
bar_width = 0.5

# Create the figure
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Bar chart (left y - axis): Number of released titles
bars = ax1.bar(x, titles, width=bar_width, color='#ff2d55', label='Number of released titles')

# Add labels on top of the bars
for i, val in enumerate(titles):
    ax1.text(x[i], val - 12, str(val), ha='center', fontsize=10, color='black')

# Line chart (right y - axis): Number of released episodes
ax2.plot(x, episodes, color='#586173', linewidth=2.5, marker='o', markersize=25, label='Number of released episodes', zorder=5)

# Add numeric labels at the nodes
for i, val in enumerate(episodes):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# Set axes and labels
ax1.set_xticks(x)
ax1.set_xticklabels(periods, fontsize=11)
ax1.set_ylabel('Number of released titles', fontsize=12, color='#ff2d55')
ax2.set_ylabel('Number of released episodes', fontsize=12, color='#586173')

ax1.set_ylim(0, 200)     # Left y - axis (number of titles)
ax2.set_ylim(0, 4000)    # Right y - axis (number of episodes)

# Title
plt.title('Micro - drama distribution licenses issued by the SARFT\nfrom June 2022 to December 2023', fontsize=14, fontweight='bold', pad=20)

# Combine legends from left and right axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# Grid & Beautification
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()