import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# Categories and corresponding data
categories = ["Diapers", "Pull - up Diapers", "Disposable Diaper Sheets"]
data = [78.2, 76.4, 51.6]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a horizontal bar chart
x = np.arange(len(categories))
bar_width = 0.4
bars = ax.barh(x, data, height=bar_width, color="#C63982")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set y - axis ticks and labels
ax.set_yticks(x)
ax.set_yticklabels(categories)
# Hide x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("2022 Purchased Categories of Baby Diaper Products by Chinese Consumers", fontsize=12, fontweight="bold")

# Beautify the chart by hiding the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()