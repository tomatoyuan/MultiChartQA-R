import matplotlib.pyplot as plt
import numpy as np

# Sleep quality feedback classification
labels = ["No problems, slept very well", "Okay, occasional sleep problems", "Yes, occasional sleep problems", "Yes, have relatively serious sleep problems", "Yes, have very serious sleep problems"]
# Simulate percentage data (close to the original image)
percentages = [18.7, 47.0, 23.2, 8.7, 2.4]
# Free color scheme (can be adjusted, using green series as an example)
bar_color = "#6339C6"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart
x = np.arange(len(labels))
bar_width = 0.5
bars = ax.bar(x, percentages, width=bar_width, color=bar_color)

# Add data annotations
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=40, ha='right', fontsize=9)
# Set y-axis ticks (0 - 50%, adapted to the data)
ax.set_ylim(0, 50)
# Set the title
ax.set_title("User feedback on their own sleep quality", fontsize=14, fontweight="bold")

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()