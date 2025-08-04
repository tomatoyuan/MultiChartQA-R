import matplotlib.pyplot as plt
import numpy as np

# Data settings
categories = ["5 times or more per month", "3 - 4 times per month", "1 - 2 times per month", "1 - 2 times per quarter", "1 - 2 times per year"]
data = [8.0, 33.0, 41.5, 14.5, 3.0]
# The indices of the categories to be boxed (corresponding to "3 - 4 times per month", "1 - 2 times per month", "1 - 2 times per quarter", with indices 1, 2, 3)
boxed_indices = [1, 2, 3]

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
ax.set_title("Usage frequency of users' commonly used instant delivery platforms", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()