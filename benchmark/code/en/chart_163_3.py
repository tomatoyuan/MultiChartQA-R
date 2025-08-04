import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import cm

# Data
years = list(range(2012, 2023))
gdp_percent = [55, 54, 56, 56, 44, 42, 42, 40, 40, 40, 41]

# Color gradient (from light red to dark red)
colors = cm.Reds(np.linspace(0.3, 0.8, len(gdp_percent)))

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(years, gdp_percent, color=colors, edgecolor='black')

# Add value labels
for bar, value in zip(bars, gdp_percent):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
            f'{value}%', ha='center', va='bottom', fontsize=11)

# Title and labels
ax.set_title("Proportion of County - level Economic Scale in National GDP (2012–2022)", fontsize=15)
ax.set_ylabel("Proportion (%)", fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()