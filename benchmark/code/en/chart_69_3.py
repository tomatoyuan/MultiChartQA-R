import matplotlib.pyplot as plt
import numpy as np

# Accommodation preference categories
categories = ["Hygiene and Safety", "Unique Experience", "Family - Friendly Programs", "Pet - Friendly", "Photo Spots", "All - Inclusive", "Others"]
# Corresponding data (proportion), the data can be approximately the same
data = [91.2, 49.8, 36.6, 28.7, 27.0, 12.0, 10.5]
# Color setting, close to the green color scheme in the original image
color = "#C6395C"

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, data, width=bar_width, color=color, edgecolor="white")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=25)
# Hide y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("Accommodation Preferences of Micro - vacationers", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.show()