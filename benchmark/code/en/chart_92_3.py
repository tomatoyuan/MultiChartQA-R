import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2016, 2017, 2018, 2019, 2020, 2021])
percentages = np.array([1.8, 2.7, 4.6, 4.8, 5.4, 13.6])

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw an area chart with gradient color filling
from matplotlib.collections import PolyCollection

# Create coordinates for the filled area
verts = [(years[0], 0)] + list(zip(years, percentages)) + [(years[-1], 0)]
poly = PolyCollection([verts], facecolors=['#b2dfdb'], edgecolors='none', alpha=0.7)
ax.add_collection(poly)

# Overlay a line chart + dots
ax.plot(years, percentages, marker='o', color='#00796B', linewidth=2.5, label='New energy vehicle production ratio (%)')

# Add data labels
for x, y in zip(years, percentages):
    ax.text(x, y + 0.5, f'{y}%', ha='center', fontsize=10, color='#004d40', fontweight='bold')

# Set the axes
ax.set_xticks(years)
ax.set_ylim(0, max(percentages) + 3)
ax.set_ylabel("New energy vehicle production ratio (%)")

# Add a title
ax.set_title("New energy vehicle production ratio in China from 2016 to 2021", fontsize=14, fontweight='bold')

# Legend
ax.legend(loc='upper left', fontsize=10)

# Beautify the chart
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_alpha(0.2)
ax.spines["left"].set_alpha(0.2)

plt.tight_layout()
plt.show()