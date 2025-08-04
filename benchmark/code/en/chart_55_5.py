import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
income_groups = [
    "Below 4000 yuan", "4001 - 6000 yuan", "6001 - 8000 yuan",
    "8001 - 10000 yuan", "10001 - 15000 yuan", "Above 15000 yuan"
]
percentages = [4.6, 18.3, 26.5, 21.2, 18.9, 10.4]

# -------------------- Polar Coordinate Settings --------------------
N = len(percentages)
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = percentages
width = 2 * np.pi / N * 0.9  # Angle width of each sector

# Gradient color scheme (Red → Orange → Yellow → Green → Blue → Purple)
colors = ["#e57373", "#ffb74d", "#fff176", "#81c784", "#64b5f6", "#ba68c8"]

# -------------------- Create Polar Coordinate Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
bars = ax.bar(theta, radii, width=width, color=colors, edgecolor="white", linewidth=1, align="edge")

# -------------------- Add Labels --------------------
for i, (angle, radius) in enumerate(zip(theta, radii)):
    ax.text(
        angle + width / 2, radius + 2, 
        f"{income_groups[i]}\n{radius}%", 
        ha="center", va="center",
        fontsize=10, fontweight="bold", color="#424242", rotation_mode='anchor'
    )

# -------------------- Beautify the Chart --------------------
ax.set_theta_zero_location('N')   # Set the starting point to the top
ax.set_theta_direction(-1)        # Clockwise direction
ax.set_rticks([])                 # Do not display radial scale
ax.set_yticklabels([])            # Do not display radial labels
ax.spines["polar"].set_visible(False)  # Remove the polar coordinate border

# Add title
plt.title(
    "Monthly Personal Income Level of Chinese E - sports Users in 2025",
    fontsize=14, fontweight="bold", pad=20
)

plt.tight_layout()
plt.show()