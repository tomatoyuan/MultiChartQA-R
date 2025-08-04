import matplotlib.pyplot as plt
import numpy as np

# Data definition
items = [
    {"name": "Learning Professional Courses", "rate": 69.3, "color": "#a8e6cf"},
    {"name": "Completing Graduation Thesis", "rate": 64.0, "color": "#dcedc1"},
    {"name": "Gaining Internship Experience", "rate": 51.1, "color": "#ffd3b6"},
    {"name": "Taking External Exams", "rate": 50.8, "color": "#c8e6c9"},
    {"name": "Participating in Campus Practice", "rate": 42.5, "color": "#e8eaf6"},
]

# Path node coordinates
node_coords = [
    (0.1, 0.8),   # Learning Professional Courses
    (0.3, 0.65),  # Completing Graduation Thesis
    (0.5, 0.5),   # Gaining Internship Experience
    (0.7, 0.6),   # Taking External Exams
    (0.9, 0.3),   # Participating in Campus Practice
]

# Connection order
connections = [(0, 1), (1, 2), (2, 3), (3, 4)]

fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Draw connections
for start, end in connections:
    x1, y1 = node_coords[start]
    x2, y2 = node_coords[end]
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle='--', linewidth=1.5)

# Draw bubbles and text
for i, item in enumerate(items):
    x, y = node_coords[i]

    # Draw bubble
    bubble = plt.Circle((x + 0.05, y), 0.05, color=item["color"], zorder=2)
    ax.add_artist(bubble)

    # Draw text
    text = f"{item['rate']}%\n{item['name']}"
    ax.text(x + 0.12, y, text,
            ha='left', va='center',
            fontsize=10, color='black')

# Title
ax.text(0.5, 0.92, "Top 5 Most Important Things in College",
        ha='center', va='center',
        fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()