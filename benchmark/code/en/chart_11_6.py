import matplotlib.pyplot as plt
import numpy as np

# Data (sorted in descending order)
universities = [
    "Harvard University", "Massachusetts Institute of Technology", "Stanford University",
    "Johns Hopkins University", "University of California, Berkeley",
    "University of Washington, Seattle", "University of Toronto",
    "University of Oxford", "University of California, Los Angeles", "University College London"
]

# Search proportion (sorted in descending order)
search_proportion = [1.0, 0.9, 0.85, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3]

# Color scheme (enhanced contrast)
colors = [
    "#FF5252", "#FF9800", "#FFEB3B",
    "#42A5F5", "#42A5F5", "#42A5F5",
    "#5C6BC0", "#5C6BC0", "#5C6BC0", "#5C6BC0"
]

# Create a canvas (increase clarity)
plt.rcParams['figure.dpi'] = 300
fig, ax = plt.subplots(figsize=(10, 7), facecolor="#E8F5E9")

# Reverse the order of the data
universities = universities[::-1]
search_proportion = search_proportion[::-1]
colors = colors[::-1]  # Reverse the colors if you need to keep the color correspondence

# Draw a horizontal bar chart (add shadow effect)
bars = ax.barh(universities, search_proportion, color=colors, height=0.7,
               edgecolor='black', linewidth=0.5, alpha=0.9)

# Add a title (improve the design)
title_bg = plt.Rectangle((0, 1.02), 1, 0.1, color="#D32F2F", transform=ax.transAxes,
                        clip_on=False, zorder=3)
ax.add_patch(title_bg)
ax.text(0.5, 1.06, "Top Overseas Universities Most Concerned About",
        fontsize=18, fontweight="bold", color="white",
        transform=ax.transAxes, va="center", ha="center")

# Add the "Search Index" label (improve the position)
ax.text(-0.15, 0.98, "Search Index",
        fontsize=14, fontweight="bold", color="#D32F2F",
        transform=ax.transAxes, va="center", rotation=0)

# Beautify the y-axis labels (add padding and borders)
for i, txt in enumerate(ax.get_yticklabels()):
    txt.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.3'))

# Hide the borders and ticks
ax.spines[:].set_visible(False)
ax.set_xticks([])
ax.tick_params(axis='y', labelsize=12, pad=15)

# Add grid lines (horizontal direction)
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a bottom decorative line
footer_line = plt.Line2D([0, 1], [-0.03, -0.03], color='#D32F2F',
                        transform=ax.transAxes, linewidth=3, clip_on=False)
ax.add_artist(footer_line)

plt.tight_layout()
plt.show()