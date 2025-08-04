import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- Data Definition --------------------
categories = [
    "Promote brain development",
    "Immunity issues",
    "Promote gastrointestinal digestion",
    "Strengthen bones/Promote bone development",
    "Growth and development issues",
    "Promote visual development"
]
percentages = [73.5, 72.3, 68.1, 64.5, 63.9, 53.6]

# -------------------- Color Mapping: Gradient Color Scheme --------------------
# Use colormap (plasma/magma/turbo, etc.)
cmap = cm.get_cmap("plasma")
norm = mcolors.Normalize(vmin=min(percentages), vmax=max(percentages))
colors = [cmap(norm(p)) for p in percentages]

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- Draw a "Progress Bar Style" Horizontal Bar Chart --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
    height=0.5,
    edgecolor="gray",
    linewidth=1.2
)

# Add percentage text
for i, (bar, value) in enumerate(zip(bars, percentages)):
    ax.text(
        value + 1, bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}%",
        va="center", ha="left",
        fontsize=10, fontweight="bold", color="#333333"
    )

# -------------------- Beautify the Chart --------------------
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color="#333333")

# Hide x-axis ticks
ax.set_xticks([])
# Remove extra borders
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)

# Add title
ax.set_title("Health Concerns in the 0 - 3 Year Old Infant Stage (%)", fontsize=14, fontweight="bold", pad=20)

# Add white space
plt.tight_layout()
plt.show()