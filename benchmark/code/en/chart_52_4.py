import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
categories = [
    "Academic exchange activities",
    "Research opportunities",
    "Access to academic resources",
    "Research tools and methods",
    "Disciplinary frontier trends",
    "Completely not interested in academic content"
]

values = [67.2, 52.6, 51.4, 40.6, 37.1, 0.9]

# Green color scheme similar to the original image
colors = [
    "#a5d6a7", "#81c784", "#c8e6c9", 
    "#e8f5e9", "#b9f6ca", "#f5f5f5"
]

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Draw a horizontal bar chart --------------------
y = np.arange(len(categories))

# Draw the basic bar chart
bars = ax.barh(
    y, 
    values, 
    color=colors, 
    edgecolor='white',
    linewidth=1
)

# Add numerical labels
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height()/2,
        f'{width}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# -------------------- Beautify the chart --------------------
# Set y - axis labels
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color='#424242')

# Hide the x - axis
ax.set_xticks([])

# Hide the borders
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust the position of the y - axis (make the bar chart closer to the left)
ax.tick_params(axis='y', left=False)

# Add a title
ax.set_title(
    "College students' attention to academic content", 
    fontsize=14, 
    fontweight='bold', 
    pad=20
)

# Adjust the layout
plt.subplots_adjust(left=0.3, right=0.9, top=0.85, bottom=0.2)

plt.show()