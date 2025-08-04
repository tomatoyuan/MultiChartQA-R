import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.font_manager as fm

# Data
dates = ["July 19th", "July 20th"]
searches = [234381, 534381]
increase = 41  # Growth rate

# Create a custom gradient color
colors = [(0.9, 0.95, 1), (0.1, 0.3, 0.6)]  # From light blue to dark blue
custom_cmap = LinearSegmentedColormap.from_list("custom_blue", colors, N=100)

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f8fafc")
ax.set_facecolor("#f8fafc")

# Draw the background grid
for y in np.linspace(0, max(searches), 6):
    ax.axhline(y, color='lightblue', alpha=0.15, linewidth=1)

# Draw a bar chart (with a three - dimensional effect)
x_pos = np.arange(len(dates))
bar_width = 0.6

for i, (date, search) in enumerate(zip(dates, searches)):
    # Main bar chart (gradient fill)
    rect = Rectangle((i - bar_width/2, 0), bar_width, search, 
                    facecolor='none', edgecolor='none')
    ax.add_patch(rect)
    
    img = np.ones((100, 1)) * np.linspace(0.3, 1, 100).reshape(-1, 1)
    ax.imshow(img, aspect='auto', extent=[i - bar_width/2, i + bar_width/2, 0, search],
              cmap=custom_cmap, alpha=0.9, clip_path=rect)
    
    # Top highlight
    top_highlight = Rectangle((i - bar_width/2, search - 10000), bar_width, 10000, 
                             facecolor='white', alpha=0.3)
    ax.add_patch(top_highlight)
    
    # Numerical label (with shadow effect)
    label_bg = Rectangle((i - 0.25, search + 15000), 0.5, 30000, 
                        facecolor='navy', alpha=0.8, zorder=3)
    ax.add_patch(label_bg)
    
    ax.text(i, search + 30000, f'{search:,}', 
            ha='center', va='center', color='white', fontsize=18, 
            fontweight='bold', zorder=4)

# Add growth rate indication (using arrows and percentage signs)
class CustomArrow(FancyArrowPatch):
    def __init__(self, posA, posB, **kwargs):
        super().__init__(posA, posB, arrowstyle='-|>', 
                         mutation_scale=20, **kwargs)

arrow = CustomArrow((1.1, searches[0]), (1.1, searches[1]*0.85), 
                   color='navy', alpha=0.8, linewidth=2)
ax.add_patch(arrow)

# Growth rate percentage marker
growth_bg = Rectangle((1.1 - 0.15, searches[1]*0.85), 0.3, 30000, 
                     facecolor='navy', alpha=0.9, zorder=3)
ax.add_patch(growth_bg)

ax.text(1.1, searches[1]*0.85 + 15000, f'{increase}%', 
        ha='center', va='center', color='white', fontsize=20, 
        fontweight='bold', zorder=4)

# Set the title (with decorative lines)
title = ax.set_title('Takeaway search times on rainy days', 
                     fontdict={'fontsize':26, 'fontweight':'bold', 'color':'navy'},
                     pad=40, loc='center')

# Decorative line under the title
line_start = 0.35
line_end = 0.65
ax.plot([line_start, line_end], [0.94, 0.94], transform=ax.transAxes, 
        color='navy', alpha=0.3, linewidth=2)

# Hide the axes
ax.set_xticks(x_pos)
ax.set_xticklabels(dates, color='navy', fontsize=18, fontweight='bold')
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set the y - axis range
ax.set_ylim(0, max(searches) * 1.3)

# Add a bottom decorative bar
bottom_bar = Rectangle((-0.5, -30000), 2.5, 30000, 
                      facecolor='navy', alpha=0.1)
ax.add_patch(bottom_bar)

# Optimize the layout
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Make space for the title
plt.show()