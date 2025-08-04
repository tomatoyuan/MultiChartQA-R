import matplotlib.pyplot as plt
import numpy as np

# Title and content list
title = "Attention on AIDS Knowledge and Prevention"
items = [
    "AIDS transmission routes",
    "Initial symptoms of AIDS",
    "How long can people with AIDS live",
    "AIDS vaccine",
    "Pictures of initial symptoms of AIDS",
    "AIDS publicity materials",
    "AIDS pictures",
    "Three major manifestations of AIDS latency"
]
# Set progress values according to the length ratio of the red bars in the original picture
progress = np.array([0.95, 0.85, 0.85, 0.85, 0.75, 0.74, 0.70, 0.70])  

# Create a canvas and an axis
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#F5F5F5")
# Hide the axes
ax.axis("off")  

# Draw the title
plt.text(
    0.03, 0.95, title, 
    fontsize=16, fontweight="bold", fontfamily="SimSun"
)

# Draw each item one by one
for i, (text, p) in enumerate(zip(items, progress), start=1):
    # Draw the background of the progress bar
    rect_bg = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94, 0.07, 
        facecolor="#F8D7DA", edgecolor="white"
    )
    ax.add_patch(rect_bg)
    # Draw the filled part of the progress bar (using different progress values)
    rect_fill = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94 * p, 0.07, 
        facecolor="#F1C2C6", edgecolor="white"
    )
    ax.add_patch(rect_fill)
    # Draw the progress percentage text
    plt.text(
        0.03 + 0.94 * p + 0.01, 0.9 - 0.1 * i + 0.035, f"{p*100:.0f}%", 
        fontsize=10, va="center", color="#8B0000"
    )
    # Draw the serial number circle
    circle = plt.Circle(
        (0.02, 0.9 - 0.1 * i + 0.035), 0.03, 
        facecolor=f"C{i-1}", edgecolor="white"
    )
    ax.add_artist(circle)
    # Draw the serial number text
    plt.text(
        0.02, 0.9 - 0.1 * i + 0.032, f"{i}", 
        fontsize=10, color="white", ha="center", va="center"
    )
    # Draw the item text
    plt.text(
        0.07, 0.9 - 0.1 * i + 0.035, text, 
        fontsize=12, va="center"
    )

plt.tight_layout(pad=2)
plt.show()