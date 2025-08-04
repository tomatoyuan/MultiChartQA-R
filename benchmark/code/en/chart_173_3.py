import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['Total Population', 'Male', 'Female', 'Aged 18 - 34', 'Aged 35 - 64', 'High - tier Cities', 'Low - tier Cities']
values = [31.4, 29.8, 33.2, 26.7, 32.6, 28.6, 33.0]
colors = ['#bbbbbb'] + ['#ff2d55'] * 6  # The first item is gray, the rest are red

y = np.arange(len(groups))

# Create a chart
fig, ax = plt.subplots(figsize=(10, 6))

# Horizontal bar chart
bars = ax.barh(y, values, color=colors, height=0.6)

# Add value labels on the right
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2, f'{val:.1f}%', va='center', fontsize=10)

# Dotted reference line (aligned with the highest value)
ax.axvline(x=31.4, linestyle='--', color='gray', linewidth=2)

# Set labels and title
ax.set_yticks(y)
ax.set_yticklabels(groups, fontsize=11)
ax.set_xlim(0, 40)
ax.invert_yaxis()  # Make "Total Population" at the top
ax.set_xlabel('Weekly Penetration Rate (%)', fontsize=12)
ax.set_title('Weekly Penetration Rate of Micro - dramas\nin Each Sub - population', fontsize=14, fontweight='bold', pad=20)

# Remove the borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()