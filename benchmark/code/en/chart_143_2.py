import matplotlib.pyplot as plt
import numpy as np

# Data preparation
channels = [
    ("Offline Retail", 50.2, "#FF6347"),
    ("Acquaintance Recommendation", 36.4, "#FFD700"),
    ("Traditional Advertising", 40.6, "#FFDAB9"),
    ("Content Sharing Platforms", 24.0, "#F4A460"),
    ("Short - video Platforms", 42.3, "#FFB6C1"),
    ("E - commerce Platforms", 49.6, "#FFA07A"),
]

# Hexagonal layout coordinates (manually adjusted to approximate the original layout)
hex_coords = [
    (0, 1),   # Offline Retail
    (1, 0),   # Acquaintance Recommendation
    (1, -1),  # Traditional Advertising
    (0, -2),  # Content Sharing Platforms
    (-1, -1), # Short - video Platforms
    (-1, 0),  # E - commerce Platforms
]

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # Hide the axes

# Draw hexagons and add text
for (channel, perc, color), (x, y) in zip(channels, hex_coords):
    # Draw a hexagon (simulated with a circle)
    hexagon = plt.Circle((x, y), 0.4, color=color, alpha=0.8)
    ax.add_artist(hexagon)
    # Add the channel name and percentage
    ax.text(x, y + 0.1, channel, ha='center', va='bottom', fontsize=10)
    ax.text(x, y - 0.1, f'{perc}%', ha='center', va='top', fontsize=9, color='white')

# Title
ax.text(0, 1.8, '2023 Survey on Cosmetics Information Channels of Chinese Consumers', ha='center', fontsize=12, fontweight='bold')
ax.text(0, 1.5, '2023 Survey on the Information Channels of Cosmetics of Consumers in China', 
        ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()