import matplotlib.pyplot as plt
import numpy as np

# Chart 1: Frequency of cooking at home - Bar chart + Gradient color
labels = ["Cook at home every weekday", "Cook at home no more than 3 days a week", "Can't even guarantee once"]
values = [38, 37, 5]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(np.arange(len(labels)), values, height=0.6,
               color=["limegreen", "mediumseagreen", "turquoise"],
               edgecolor='black')

# Add value labels
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f"{values[i]}%", va='center', fontsize=12, color='black')

# Set the y - axis
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels, fontsize=12)
ax.invert_yaxis()  # Highest value on top

# Chart title and source
ax.set_title("Frequency of cooking at home", fontsize=14, fontweight='bold')
plt.text(0, -0.8, "Data source: CBNData", fontsize=10)

# Remove redundant lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

fig.tight_layout()
plt.show()