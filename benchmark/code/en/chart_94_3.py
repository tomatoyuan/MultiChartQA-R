import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Simplified labels (for legend)
short_labels = [
    "Slow process", "Device mismatch", 
    "Poor requirement communication", "Lack of one - stop service", 
    "Unsatisfied with design", "No installation and debugging service", 
    "Lack of supervision", "Unprofessional suppliers"
]

# Original data
percentages = np.array([43.6, 33.1, 27.8, 27.1, 25.6, 19.5, 15.0, 6.8])
dashed_box_indices = [0, 1]

# Polar coordinate angles
N = len(short_labels)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# Color gradient setting
norm = mcolors.Normalize(vmin=min(percentages), vmax=max(percentages))
cmap = cm.get_cmap("YlGnBu")
colors = [cmap(norm(p)) for p in percentages]

# Create figure and polar sub - plot
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw={'projection': 'polar'})

# Draw radar bar chart
bars = ax.bar(
    angles,
    percentages,
    width=2 * np.pi / N * 0.9,
    color=colors,
    edgecolor='white',
    linewidth=1
)

# Highlight the first two items
for i in dashed_box_indices:
    bars[i].set_edgecolor('deepskyblue')
    bars[i].set_linewidth(2.5)
    bars[i].set_alpha(1.0)

# Add data labels
for angle, bar, label, percent in zip(angles, bars, short_labels, percentages):
    rotation = np.rad2deg(angle)
    alignment = 'left' if np.pi/2 < angle < 3*np.pi/2 else 'right'
    ax.text(
        angle,
        bar.get_height() + 3,
        f"{percent}%",
        ha='center',
        va='center',
        fontsize=9,
        color="#333"
    )

# Set legend (each color + category)
for i in range(N):
    ax.bar(0, 0, color=colors[i], label=short_labels[i])

# Set radar chart properties
ax.set_ylim(0, 50)
ax.set_yticklabels([])
ax.set_xticks([])  # Do not display polar coordinate scales
ax.spines['polar'].set_visible(False)

# Add legend
ax.legend(
    loc='center left',
    bbox_to_anchor=(1.1, 0.5),
    fontsize=10,
    title='Difficulty categories',
    frameon=True
)

# Add title
ax.set_title(
    "Difficulties encountered by catering enterprises when opening new stores",
    fontsize=14,
    fontweight="bold",
    pad=30
)

plt.tight_layout()
plt.show()