import matplotlib.pyplot as plt
import numpy as np

# Functional expectations
functions = [
    "High accuracy",
    "Comprehensive analysis of examination results",
    "Quick understanding of eye health status",
    "Early warning for eye health problems",
    "Provision of subsequent eye health solutions",
    "Availability of health tracking archives",
    "Recording of each screening result",
    "Convenient examination methods",
    "Fast examination speed",
    "Online report interpretation service",
    "A wide range of examination items"
]
# Corresponding percentages (%), the data is consistent with the chart
percentages = [40.9, 40.3, 37.1, 36.4, 35.8, 34.4, 33.9, 27.6, 27.0, 26.9, 22.1]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 7))

# Draw a horizontal bar chart
y = np.arange(len(functions))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#395AC6")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set the y - axis ticks and labels (adjust the order so that the first function is at the top)
ax.set_yticks(y)
ax.set_yticklabels(functions)
# Hide the x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Parents' expectations for the functions of children and adolescents' visual health products", fontsize=14, fontweight="bold")

# Beautify the chart by hiding the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()