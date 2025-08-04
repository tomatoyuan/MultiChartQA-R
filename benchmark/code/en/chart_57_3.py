import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
regions = [
    "USA", "Brazil", "India", "Indonesia",
    "UK", "Japan", "Spain", "Germany",
    "Italy", "France"
]
percentages = [22.7, 14.5, 6.7, 3.7, 3.4, 2.8, 2.4, 2.0, 2.0, 2.0]

# Close the data
values = percentages + [percentages[0]]
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=True)

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# -------------------- Draw a Radar Chart --------------------
ax.plot(angles, values, color="#ab47bc", linewidth=2)
ax.fill(angles, values, color="#ce93d8", alpha=0.4)

# -------------------- Set Coordinate Labels --------------------
ax.set_xticks(angles[:-1])
ax.set_xticklabels(regions, fontsize=10, color="#424242")

# -------------------- Set the Polar Axis Range --------------------
ax.set_rlabel_position(30)
ax.set_yticks([2.5, 5, 10, 15, 20, 25])
ax.set_yticklabels(["2.5%", "5%", "10%", "15%", "20%", "25%"], color="#757575", fontsize=9)
ax.set_ylim(0, 25)

# -------------------- Add Value Annotations (Method 3: Fine - tune the Position) --------------------
for i, val in enumerate(percentages):
    angle = angles[i]
    x = angle
    y = val + 2  # Offset outward
    ha = "left" if np.pi/2 < angle < 3*np.pi/2 else "right"
    ax.text(
        x, y, f"{val}%",
        fontsize=9,
        ha=ha,
        va="center",
        color="#424242",
        fontweight="bold",
        rotation_mode="anchor"
    )

# -------------------- Add a Legend --------------------
import matplotlib.patches as mpatches
patch = mpatches.Patch(color="#ab47bc", label="Proportion of each region (%)")
ax.legend(handles=[patch], loc="upper right", bbox_to_anchor=(1.3, 1.0), fontsize=10)

# -------------------- Add a Title --------------------
ax.set_title(
    "Distribution of Influencer Marketing Posts in Global Regions (Radar Chart)",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- Display the Chart --------------------
plt.tight_layout()
plt.show()