import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# Labels and data
labels = [
    "Celebrity Emojis", "Comic Emojis", "QQ & WeChat Built - in Emojis",
    "Emoji", "Middle - aged and Elderly Emojis", "Text Emojis"
]
values = [64, 58, 51, 47, 46, 14]

# Generate gradient color series
def get_gradient_colors(base_color, num_layers, lightness_range=(0.6, 1.0)):
    """Generate gradient colors from dark to light"""
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.colors as mcolors

    # Convert hex color to RGB
    rgb = mcolors.hex2color(base_color)

    # Create gradient color mapping
    cmap = LinearSegmentedColormap.from_list(
        f'custom_{base_color}',
        [(rgb[0]*lightness_range[0], rgb[1]*lightness_range[0], rgb[2]*lightness_range[0]),
         (rgb[0]*lightness_range[1], rgb[1]*lightness_range[1], rgb[2]*lightness_range[1])]
    )

    return [cmap(i/num_layers) for i in range(num_layers)]

# Use green color series as the base
base_color = '#2c6f66'
colors = get_gradient_colors(base_color, len(labels))

# Graph parameters
num_layers = len(labels)
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Coordinates of the bottom vertex
bottom_x = 0.5
bottom_y = 0.05

# Top width (the upper side of the whole inverted triangle)
top_left = (0.1, 0.95)
top_right = (0.9, 0.95)

# Height of each layer (evenly divided)
layer_height = (top_left[1] - bottom_y) / num_layers

# Draw the background gradient
gradient_bg = np.zeros((100, 100, 3))
for i in range(100):
    for j in range(100):
        y_norm = i / 100
        # Background color from light green to lighter green
        gradient_bg[i, j] = [0.95 - y_norm*0.1, 0.98 - y_norm*0.1, 0.95 - y_norm*0.05]
ax.imshow(gradient_bg, extent=[0, 1, 0, 1], aspect='auto', zorder=0)

# Add shadow effect
shadow_offset = 0.015
for i in range(num_layers):
    # Top y and bottom y
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # Calculate the x - coordinates of the left and right boundaries of the triangle at the corresponding height
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # Construct the shadow shape
    shadow_points = [
        (x_left_top + shadow_offset, y_top - shadow_offset),
        (x_right_top + shadow_offset, y_top - shadow_offset),
        (x_right_bottom + shadow_offset, y_bottom - shadow_offset),
        (x_left_bottom + shadow_offset, y_bottom - shadow_offset)
    ]
    shadow = Polygon(shadow_points, closed=True, facecolor='black', alpha=0.15, zorder=i+1)
    ax.add_patch(shadow)

# Draw the main chart
for i in range(num_layers):
    # Top y and bottom y
    y_top = top_left[1] - i * layer_height
    y_bottom = top_left[1] - (i + 1) * layer_height

    # Calculate the x - coordinates of the left and right boundaries of the triangle at the corresponding height
    x_left_top = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_top) / top_left[1]
    x_right_top = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_top) / top_right[1]
    x_left_bottom = top_left[0] + (bottom_x - top_left[0]) * (top_left[1] - y_bottom) / top_left[1]
    x_right_bottom = top_right[0] - (top_right[0] - bottom_x) * (top_right[1] - y_bottom) / top_right[1]

    # Construct the trapezoid/triangular strip shape
    points = [
        (x_left_top, y_top),
        (x_right_top, y_top),
        (x_right_bottom, y_bottom),
        (x_left_bottom, y_bottom)
    ]

    # Add a slight transparency change to make the bottom more obvious
    alpha = 0.95 - i * 0.03 if i < num_layers - 1 else 0.95
    tri = Polygon(points, closed=True, facecolor=colors[i], edgecolor='white', linewidth=1.5, alpha=alpha, zorder=i+2)
    ax.add_patch(tri)

    # Write text in the middle of each layer
    y_text = (y_top + y_bottom) / 2
    ax.text(0.5, y_text, f"{labels[i]}",
            color='black', ha='right', va='center', fontsize=13, fontweight='medium',
            transform=ax.transAxes, zorder=10)

    # Add percentage labels
    ax.text(0.52, y_text, f"{values[i]}%",
            color='white', ha='left', va='center', fontsize=13, fontweight='bold',
            transform=ax.transAxes, zorder=10)

# Add new title - related text, adjust the title and subtitle content as required
plt.text(0.5, 1.02, "Female Version", ha='center', fontsize=22, weight='bold', color=base_color, transform=ax.transAxes)
plt.text(0.5, 0.98, "Contempt Logic: Entertainment Attribute - Female Usage Rate", ha='center', fontsize=14, color='#666666', transform=ax.transAxes)

# Adjust the layout
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.05)
plt.show()