import matplotlib.pyplot as plt
import numpy as np

# Edible scenarios classification
scenarios = [
    "After dinner/gathering", "While watching TV shows/variety shows/movies", 
    "Afternoon tea", "During work/study", 
    "After sports/fitness", "Outdoor travel", "Home - made food scenario"
]
# Simulate percentage data (close to the original figure)
percentages = [64.0, 59.6, 55.4, 51.8, 47.5, 44.0, 42.2]
# Free color matching (can be adjusted, using orange series as an example)
bar_color = "#F6FF7A"  # Can be replaced with other colors such as "#87CEEB"
# Indices of the first four items covered by the blue dashed box
dashed_box_indices = [0, 1, 2, 3]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(scenarios))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

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

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(scenarios)
# Set x - axis ticks (0 - 70%)
ax.set_xlim(0, 70)
# Set the title
ax.set_title("Fruit consumption scenarios", fontsize=14, fontweight="bold")

# Beautify: hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()