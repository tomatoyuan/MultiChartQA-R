import matplotlib.pyplot as plt
import numpy as np

# Data preparation
constellations = [
    "Taurus", "Aquarius", "Capricorn", "Leo", "Pisces", "Aries", "Sagittarius", "Cancer",
    "Libra", "Gemini", "Virgo", "Scorpio"
]
percentages = [4, 4, 7, 10, 5, 9, 6, 6, 6, 10, 18, 15]
# Manually set the coordinates of each constellation for layout convenience (can be fine - tuned according to the design)
coords = [
    (0.2, 0.8), (0.1, 0.6), (0.3, 0.4), (0.2, 0.2), (0.4, 0.1), (0.6, 0.2),
    (0.7, 0.3), (0.8, 0.5), (0.7, 0.7), (0.5, 0.8), (0.6, 0.6), (0.4, 0.7)
]
# Corresponding bubble colors (example color scheme, can be adjusted by yourself)
colors = [
    "#D4AF37", "#ADD8E6", "#C0C0C0", "#87CEFA", "#F0E68C", "#90EE90",
    "#FFD700", "#FF6347", "#FFC0CB", "#BA55D3", "#FF69B4", "#1E90FF"
]
# Special annotation text for Virgo
virgo_text = "Although Virgo is noble and aloof,\n the most proficient thing is hiding anxiety."

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
# Hide the axes
ax.set_xticks([])
ax.set_yticks([])

# Draw bubbles + annotations
for constellation, p, (x, y), color in zip(constellations, percentages, coords, colors):
    # Draw bubbles (simulated by scatter plot)
    ax.scatter(
        x, y, 
        s=p * 120,  # Bubble size is related to the anxiety percentage
        c=color, 
        alpha=0.8,
        edgecolors='white', 
        linewidths=1
    )
    # Draw the percentage text
    text_color = 'white' if p != 18 else 'black'  # Reverse the text color for Virgo
    ax.text(
        x, y, 
        f"{p}%", 
        ha='center', 
        va='center', 
        fontsize=10, 
        color=text_color, 
        fontweight='bold'
    )
    # Draw the constellation name
    ax.text(
        x, y - 0.05, 
        constellation, 
        ha='center', 
        va='top', 
        fontsize=9, 
        color='white'
    )

# Special description text for Virgo
virgo_x, virgo_y = coords[constellations.index("Virgo")]
ax.text(
    virgo_x, virgo_y - 0.18, 
    virgo_text, 
    ha='center', 
    va='bottom', 
    fontsize=10, 
    color='white', 
    linespacing=1.2,
    # Fix: Change the CSS color format to RGBA tuple format
    bbox=dict(facecolor=(1, 1, 1, 0.1), edgecolor='white', pad=5)
)

# Add a title
ax.text(
    0.5, 0.95, 
    "The Most Anxious Constellations Ranking", 
    ha='center', 
    va='center', 
    fontsize=20, 
    color='white', 
    fontweight='bold'
)

plt.tight_layout()
plt.show()