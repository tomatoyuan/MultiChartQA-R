import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Data
labels = ['Post - 2005', 'Post - 2000', 'Post - 1995', 'Post - 1990', 'Post - 1985', 'Post - 1980', 'Pre - 1980']
values = [105, 73, 115, 115, 110, 80, 80]

# Color setting: Light pink -> Dark pink gradient
cmap = mcolors.LinearSegmentedColormap.from_list("pink_gradient", ["#fddde6", "#ec6fa8"])
colors = [cmap(i / (len(values) - 1)) for i in range(len(values))]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# Auxiliary lines and annotations
ax.axhline(100, color='deeppink', linestyle='--', linewidth=1.5)
for bar, val in zip(bars, values):
    va = 'bottom' if val >= 100 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2, val + (2 if val >= 100 else -5), f'{val}',
            ha='center', va=va, fontsize=12, color='black')

# Title and description
ax.set_title('Research on the Attention of Women of Different Generations to Oral Health', fontsize=14)
ax.set_ylabel('TGI')
ax.set_ylim(50, 130)
ax.text(-0.5, 110, 'High attention\nTGI>100', color='deeppink', fontsize=10)
ax.text(-0.5, 90, 'Low attention\nTGI<100', color='deeppink', fontsize=10)

plt.tight_layout()
plt.show()