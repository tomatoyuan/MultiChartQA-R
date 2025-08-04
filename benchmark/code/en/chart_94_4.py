import matplotlib.pyplot as plt
import numpy as np

# Pain point categories
pain_points = [
    "Traditional and non - intelligent equipment", "Single - function equipment", "High dependence on manpower",
    "Loud noise during equipment use", "Large footprint of equipment", "High damage rate of equipment",
    "Heavy fumes during equipment use", "Short lifespan and high scrappage rate of equipment", "High equipment cost and difficult to recover investment",
    "Low operation/dish - serving efficiency of equipment", "Complex and inconvenient operation of equipment"
]
# Simulated proportion data (can be adjusted, the first three are similar to the original figure)
percentages = [48.9, 48.1, 48.1, 37.6, 36.8, 33.8, 28.6, 27.8, 25.6, 24.8, 16.5]
# Indices of the first three items covered by the blue dashed box
dashed_box_indices = [0, 1, 2]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 7))

# Draw a horizontal bar chart
y = np.arange(len(pain_points))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color="#A4C639")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # Label position: offset 5 to the right
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Draw a blue dashed box
min_y = min([bars[i].get_y() for i in dashed_box_indices])
max_y = max([bars[i].get_y() + bar_height for i in dashed_box_indices])
max_width = max([bars[i].get_width() for i in dashed_box_indices])

# Draw the dashed box (top, right, bottom, left)
ax.plot([0, max_width], [max_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([max_width, max_width], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, max_width], [min_y, min_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, 0], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(pain_points)
# Set the x - axis ticks (0 - 50%)
ax.set_xlim(0, 55)
# Set the title
ax.set_title("Pain points in the use of kitchen appliances", fontsize=14, fontweight="bold")

# Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()