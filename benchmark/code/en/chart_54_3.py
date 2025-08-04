import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- Data Definition --------------------
categories = [
    "Immunity issues",
    "Growth and development issues",
    "Strengthen bones / Promote bone development",
    "Vision problems",
    "Promote gastrointestinal digestion",
    "Concentration"
]
percentages = [76.0, 63.8, 63.3, 61.2, 48.0, 39.8]

# -------------------- Angle and Color Mapping --------------------
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
colors = cm.get_cmap("viridis")(mcolors.Normalize()(percentages))  # Can be replaced with 'coolwarm', 'viridis', etc.

# -------------------- Create Canvas (Polar Coordinates) --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
bars = ax.bar(
    angles,
    percentages,
    width=2*np.pi/N * 0.8,  # Control the width
    color=colors,
    edgecolor="white",
    linewidth=1
)

# -------------------- Add Annotations --------------------
for angle, height in zip(angles, percentages):
    ax.text(
        angle,
        height - 7,  # Offset outside the arc
        f"{height:.1f}%",
        ha='center', va='center',
        fontsize=10,
        color="black",
        fontweight="bold"
    )

# -------------------- Set Category Labels (Place around the circle) --------------------
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=9, color="#333333")

# Hide the default radius lines and scales of the polar coordinates
ax.set_yticklabels([])
ax.set_yticks([])
ax.spines["polar"].set_visible(False)

# Add a title
plt.title("Health concerns for children aged 4 - 6 (%)", fontsize=14, fontweight="bold", pad=30)

plt.tight_layout()
plt.show()