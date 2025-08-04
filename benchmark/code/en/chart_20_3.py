import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# ======================== 1. Data and basic configuration ========================
labels = ["Melamine", "Indoor decoration", "Skin care products", "Alcohol consumption", "Henna powder", "Air pollution"]
sizes = [33, 10, 8, 8, 8, 7]

# Coordinates for hexagonal ring distribution (convert polar coordinates to Cartesian coordinates)
theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
radius = 1.2  # Control the radius of the hexagonal ring
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Custom gradient color palette (from light pink to dark pink)
cmap = LinearSegmentedColormap.from_list(
    'pink_cmap',
    ['#FFE6F0', '#FFABCD', '#E66493', '#CC3377', '#B30059', '#8B003C'],
    N=len(labels)
)

# ======================== 2. Initialize the canvas and axes ========================
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#F8F8FF')  # Light blue background
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Hide the axes

# ======================== 3. Draw 3D hexagons (with shadows and gradients) ========================
for i in range(len(labels)):
    # Main hexagon (gradient fill)
    hex_main = RegularPolygon(
        (x[i], y[i]), numVertices=6, radius=0.5,
        facecolor=cmap(i), edgecolor='white', linewidth=2
    )
    ax.add_patch(hex_main)

    # Shadow hexagon (simulate 3D effect)
    hex_shadow = RegularPolygon(
        (x[i] + 0.05, y[i] - 0.05), numVertices=6, radius=0.5,
        facecolor='gray', alpha=0.2, edgecolor='none'
    )
    ax.add_patch(hex_shadow)

    # Draw the percentage number (centered, bold)
    ax.text(
        x[i], y[i], f"{sizes[i]}%",
        ha='center', va='center',
        fontsize=14, fontweight='bold',
        color='white'
    )

    # Draw the label text (surrounding layout, adjust the angle)
    text_angle = np.rad2deg(theta[i]) - 90  # Adjust the text angle for the hexagon
    ax.text(
        x[i] * 1.8, y[i] * 1.8, labels[i],
        ha='center', va='center',
        fontsize=12, color='#333333',
        rotation=text_angle
    )

# ======================== 4. Add title and decoration ========================
# Center title
ax.text(
    0, 0, "Proportion of cancer - causing reasons",
    ha='center', va='center',
    fontsize=20, fontweight='bold',
    color='#CC3377'
)

# Bottom description
ax.text(
    0, -2.2, "Data source: Simulated statistics | Unit: %",
    ha='center', va='center',
    fontsize=10, color='#666666',
)

# Gradient background (diffusing from the center)
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient_img = np.tile(gradient, (256, 1))
ax.imshow(
    gradient_img, extent=(-2.5, 2.5, -2.5, 2.5),
    cmap=cm.get_cmap('Blues_r'), alpha=0.3
)

plt.tight_layout()
plt.show()