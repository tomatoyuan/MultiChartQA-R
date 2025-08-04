import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2019", "2020", "2021"]
# Proportion of female variety shows (%)
percentage = [9.8, 10.5, 14.7]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a line chart
line, = ax.plot(years, percentage, marker='o', color="#C6395A", label="Proportion of female variety shows (%)", linewidth=2)

# Add data labels
for x, y in zip(years, percentage):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 15),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Set the x - axis ticks and labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
# Hide the y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("SVC - Trend of the proportion of female variety shows from 2019 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend(loc='upper left')

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()