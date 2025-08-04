import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Consumption locations
locations = ["High - end and mid - range restaurants", "Popular restaurants", "Home/Dormitory", "Bars/Pubs", "Others"]
# Proportion of 18 - 29 years old (%)
age18_29 = [41.7, 21.1, 18.6, 10.8, 7.8]
# Proportion of 30 years old and above (%)
age30_up = [30.6, 34.7, 19.8, 11.2, 3.7]
# Reference proportions for middle annotation (for alignment)
ref_rates = [35.4, 28.8, 19.3, 11.0, 5.5]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart for 18 - 29 years old (green)
y = np.arange(len(locations))
bar_width = 0.35
bars1 = ax.barh(y + bar_width/2, age18_29, height=bar_width, color="#A4C639", label="Proportion of 18 - 29 years old (%)")
# Draw a horizontal bar chart for 30 years old and above (blue)
bars2 = ax.barh(y - bar_width/2, age30_up, height=bar_width, color="#87CEEB", label="Proportion of 30 years old and above (%)")

# Add data annotations for 18 - 29 years old
for i, bar in enumerate(bars1):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(-5, 0),  # Left - side annotation
                textcoords="offset points",
                ha='right', va='center',
                color='white' if i == 0 else 'black')  # The first annotation is white (simulating red - circle emphasis)

# Add data annotations for 30 years old and above
for i, bar in enumerate(bars2):
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Right - side annotation
                textcoords="offset points",
                ha='left', va='center',
                color='white' if i == 1 else 'black')  # The second annotation is white (simulating red - circle emphasis)

# Set y - axis ticks and labels (adjust the position to center the categories)
ax.set_yticks(y)
ax.set_yticklabels(locations)
ax.set_yticklabels(locations, ha='center', va='center')

# Set the title
ax.set_title("Liquor consumption locations", fontsize=16, fontweight="bold")

# Add a legend
ax.legend(loc='upper right')

# Beautify: Hide the top, right, and bottom borders
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

# Adjust the x - axis range to leave space for annotations
ax.set_xlim(0, max(max(age18_29), max(age30_up)) + 10)

plt.tight_layout()
plt.show()