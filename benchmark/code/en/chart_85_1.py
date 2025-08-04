import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Years
years = ["2020", "2030e", "2040e", "2050e", "2060e"]
# Hydrogen energy demand (10,000 tons), the data is consistent with the chart
demand = [3342, 3715, 5276, 9690, 13030]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, demand, width=bar_width, color="#C6395A")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y - axis label
ax.set_ylabel("China's hydrogen energy demand (10,000 tons)")
# Set the title
ax.set_title("China's hydrogen energy demand from 2020 to 2060", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()