import matplotlib.pyplot as plt
import numpy as np

# Scenario names
scenarios = [
    "Shopping for thirst quenching", "Social gathering", "Office work", "Staying awake during late - night", 
    "Family reception", "Daily meal accompaniment", "Late - night overtime", "Business entertainment", 
    "Carrying on business trips", "Gifting during festivals", "Following the trend to experience"
]

# Corresponding percentage data for each scenario
percentages = [51, 47, 46, 46, 41, 38, 33, 23, 23, 22, 13]

# Data sorting (optional)
sort_data = True
if sort_data:
    # Sort by percentage in descending order
    sorted_data = sorted(zip(percentages, scenarios), reverse=True)
    percentages, scenarios = zip(*sorted_data)

# Create a canvas and sub - plot, set the chart size
fig, ax = plt.subplots(figsize=(12, 7))

# Use gradient colors to fill the bar chart
cmap = plt.cm.Greens
norm = plt.Normalize(min(percentages), max(percentages))
colors = cmap(norm(percentages))

# Create a bar chart
bars = ax.bar(scenarios, percentages, color=colors, edgecolor='black', linewidth=0.5)

# Add title and labels
ax.set_title("Consumer daily tea - drinking scenario survey", fontsize=16, pad=20)
ax.set_ylabel("Percentage (%)", fontsize=12, labelpad=10)

# Set the rotation angle and font size of the x - axis labels
plt.xticks(rotation=30, ha='right', fontsize=10)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add numerical labels above each bar
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.,
        height + 0.8,  # Fine - tune the label position
        f'{percentage}%',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# Set the y - axis range
plt.ylim(0, max(percentages) + 5)

# Add background color
ax.set_facecolor('#f8f9fa')

# Optimize the layout
plt.tight_layout()

# Display the chart
plt.show()