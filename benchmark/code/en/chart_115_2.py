import matplotlib.pyplot as plt
import numpy as np

# Enterprise scale categories and their proportion data
labels = ["Small Enterprises", "Medium - sized Enterprises", "Micro Enterprises", "Large Enterprises"]
sizes = [60.47, 25.64, 10.47, 3.42]
# Corresponding colors
colors = ['blue', 'green', 'orange', 'purple']
# Descriptive information for each category (used for annotation)
descriptions = [
    "Small Enterprises (Number of employees: 20 ≤ X < 300 or Operating income: 300 ≤ Y < 2000 million yuan)",
    "Medium - sized Enterprises (Number of employees: 300 ≤ X < 1000 or Operating income: 2000 ≤ Y < 40000 million yuan)",
    "Micro Enterprises (Number of employees: X < 20 or Operating income: Y < 300 million yuan)",
    "Large Enterprises (Number of employees: X ≥ 1000 or Operating income: Y ≥ 40000 million yuan)"
]

# Construct the polygon vertex coordinates of the funnel chart (roughly simulate, can be fine - tuned as needed)
# Assume the funnel is horizontally symmetric and layered vertically
y_positions = [0.8, 0.6, 0.4, 0.2]  # Vertical positions of each layer
widths = [1, 0.6, 0.3, 0.1]  # Widths of each layer, decreasing from top to bottom to simulate a funnel
vertices_list = []
for y, w in zip(y_positions, widths):
    left = -w / 2
    right = w / 2
    vertices = [(left, y), (right, y), (right, y - 0.1), (left, y - 0.1)]
    vertices_list.append(vertices)

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(vertices_list)):
    # Draw each layer of the polygon (funnel layers)
    polygon = plt.Polygon(vertices_list[i], color=colors[i])
    ax.add_patch(polygon)
    # Add proportion and description annotations, located in the middle of the layer
    center_x = 0
    center_y = y_positions[i] - 0.05
    ax.text(center_x, center_y, f'{labels[i]}\n{descriptions[i]}\nProportion: {sizes[i]}%',
            ha='center', va='center', fontsize=9)

ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes
ax.set_title('Scale of Chinese Digital Transformation Enterprises in 2025')

plt.tight_layout()
plt.show()