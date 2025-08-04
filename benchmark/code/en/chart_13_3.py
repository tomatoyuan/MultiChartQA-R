import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# Data
groups = ["Foodie", "Housewife", "Tech Enthusiast", "Music Lover", "Backpacker", 
          "Military Fan", "Home Decorator", "Sports Fan", "Financial Family", "Gamer"]
values = [1.2359, 1.1635, 1.0763, 1.0363, 1.0128, 
          1.0078, 0.9645, 0.8671, 0.7860, 0.5915]

# Symbol mapping (built - in markers in matplotlib)
markers = ['o', 's', '^', 'D', 'p', '*', 'h', 'v', 'X', 'P']
marker_sizes = [100, 80, 90, 70, 85, 95, 80, 90, 75, 85]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f0f8ff")
ax.set_facecolor("#f0f8ff")

# Draw a bar chart (using gradient colors)
cmap = plt.cm.get_cmap('Blues', 12)
for i, (value, group) in enumerate(zip(values, groups)):
    color_idx = int(value * 5) if value > 1 else int(value * 5) + 2
    color = cmap(color_idx)
    
    ax.barh(i, value, height=0.6, color=color, edgecolor='white', alpha=0.85)
    ax.text(value + 0.02, i, f"{value:.4f}", 
            ha="left", va="center", color='navy', fontsize=10, fontweight='bold')

# Set the title
ax.set_title("Interest Distribution of Rainstorm Public Opinion (Differentiation)", 
             fontdict={"fontsize":20, "fontweight":"bold", "color":"navy"},
             pad=20)
ax.text(0, 1.02, "Which groups are most concerned about rainstorms", 
        transform=ax.transAxes, fontsize=14, color='navy')

# Add symbols and category labels
for i, (group, marker, size) in enumerate(zip(groups, markers, marker_sizes)):
    color_idx = int(values[i] * 5) if values[i] > 1 else int(values[i] * 5) + 2
    color = cmap(color_idx)
    
    ax.scatter(-0.05, i, marker=marker, s=size, color=color, edgecolor='white', zorder=3)
    ax.text(0.01, i, group, fontsize=12, ha="left", va="center", 
            color='navy', fontweight='bold')

# Add a reference line (Differentiation = 1)
ax.axvline(x=1, color='navy', linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(1.01, -0.8, "Differentiation = 1", fontsize=10, color='navy', alpha=0.8)

# Hide the axes
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set the x - axis range
ax.set_xlim(-0.1, 1.5)
ax.set_ylim(-1, 10)

# Add a legend (move it down)
legend_elements = [
    Line2D([0], [0], color=cmap(8), lw=10, label='Differentiation > 1: More Concerned'),
    Line2D([0], [0], color='navy', linestyle='--', lw=1.5, label='Differentiation = 1: Average Level'),
    Line2D([0], [0], color=cmap(3), lw=10, label='Differentiation < 1: Less Concerned')
]
ax.legend(handles=legend_elements, 
          loc='lower right',  # Position it in the lower right corner
          bbox_to_anchor=(1, -0.1),  # Move it down by 10% of the height
          frameon=False, 
          fontsize=10, 
          labelcolor='navy')

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.3, color='lightblue')

plt.tight_layout()
plt.show()