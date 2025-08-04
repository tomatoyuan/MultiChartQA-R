import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Data
years = np.array([2018, 2019, 2020, 2021, 2025])
sales_scales = np.array([6531, 7562, 8848, 10458, 17218])

# Normalize for color mapping
norm = mcolors.Normalize(vmin=min(sales_scales), vmax=max(sales_scales))
cmap = cm.get_cmap('BuGn')

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 5))

# Calculate bubble sizes (area): the area is proportional to the value to avoid being too large
bubble_sizes = (sales_scales / max(sales_scales)) * 25000

# Draw a bubble chart
sc = ax.scatter(
    years, 
    [1]*len(years),  # Centered vertically
    s=bubble_sizes,
    c=sales_scales,
    cmap=cmap,
    alpha=0.8,
    edgecolors='white',
    linewidth=1.5
)

# Add text annotations (sales volume)
for i, (x, y, val) in enumerate(zip(years, [1]*len(years), sales_scales)):
    ax.text(x, y, f"{val}", ha="center", fontsize=10, fontweight="bold", color="#333")

# Add CAGR annotation text
ax.annotate("CAGR 17% →", xy=(2018.2, 1.15), fontsize=10, color="#388e3c", weight="bold")
ax.annotate("→ CAGR 13.3%", xy=(2021.3, 1.15), fontsize=10, color="#1976d2", weight="bold")

# Beautify the x - axis
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=11)
ax.set_xlim(2017.5, 2025.5)

# Hide the y - axis
ax.set_yticks([])
ax.spines['left'].set_visible(False)

# Beautify the border
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_alpha(0.2)

# Add a title
ax.set_title("China IC Market Sales Scale (100 million yuan) from 2018 to 2025", fontsize=14, fontweight='bold', pad=20)

# Remove grid lines, only emphasize bubbles + text
ax.grid(False)

plt.tight_layout()
plt.show()