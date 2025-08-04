import matplotlib.pyplot as plt
import numpy as np

# Data settings
categories = ["Over 3 years", "2 - 3 years (inclusive)", "1 - 2 years (inclusive)", "6 - 12 months (inclusive)", "3 - 6 months (inclusive)", "1 - 3 months (inclusive)", "≤ 1 month (inclusive)"]
data = [8.4, 12.5, 30.7, 22.9, 11.6, 6.5, 7.4]
# Indices of the categories to be boxed (corresponding to "Over 3 years", "2 - 3 years (inclusive)", "1 - 2 years (inclusive)", with indices 0, 1, 2)
boxed_indices = [0, 1, 2]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color="#A4C639", edgecolor="white")

# Draw a blue dashed box
min_y = min(y[i] - bar_height / 2 for i in boxed_indices)
max_y = max(y[i] + bar_height / 2 for i in boxed_indices)
min_x = 0
max_x = max(data[i] for i in boxed_indices)
rect = plt.Rectangle((min_x, min_y), max_x, max_y - min_y, 
                     fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  
                textcoords="offset points",
                ha='left', va='center')

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(categories)
# Hide x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Cumulative usage time of users' commonly used platforms", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()