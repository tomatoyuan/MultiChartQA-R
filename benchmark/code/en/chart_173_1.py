import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2021', '2022', '2023']
online_counts = [107, 336, 584]      # Online filing counts (Left axis - Bar chart)
filming_counts = [935, 3293, 3574]   # Filming filing counts (Right axis - Line chart)

x = np.arange(len(years))
bar_width = 0.5

# Create the main figure and dual axes
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()  # Create the right axis

# Bar chart (Left axis): Online filing counts
bars = ax1.bar(x, online_counts, width=bar_width, color='#ff2d55', label='Online Filing Counts')

# Add numbers on top of the bars
for i, val in enumerate(online_counts):
    ax1.text(x[i], val - 10, str(val), ha='center', fontsize=10, color='black')

# Line chart (Right axis): Filming filing counts
ax2.plot(x, filming_counts, color='#586173', linewidth=2.5, marker='o', markersize=25, label='Filming Filing Counts', zorder=5)

# Add text labels to the markers
for i, val in enumerate(filming_counts):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# Axes and labels settings
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.set_ylabel('Online Filing Counts', fontsize=12, color='#ff2d55')
ax2.set_ylabel('Filming Filing Counts', fontsize=12, color='#586173')

ax1.set_ylim(0, 700)      # Left axis for bar chart
ax2.set_ylim(0, 4000)     # Right axis for line chart

# Chart title
plt.title('Micro - drama Filing Counts of the State Administration \nof Radio and Television from 2021 to 2023', fontsize=14, fontweight='bold', pad=20)

# Legend (Combine legends from two axes)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# Grid and style
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['right'].set_visible(True)

# Data source
fig.text(0.01, 0.01, 'Data Source: National Radio and Television Administration', fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()