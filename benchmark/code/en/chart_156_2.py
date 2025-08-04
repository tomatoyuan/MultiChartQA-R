import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Scenarios and corresponding percentages
scenarios = ['Dating', 'Commuting to work', 'Dining out', 'Photo - taking', 'Traveling', 'Staying warm at home', 'Attending classes']
percentages = [55, 52, 50, 44, 43, 18, 12]

# Sort in reverse order (to display from top to bottom)
scenarios = scenarios[::-1]
percentages = percentages[::-1]
y_pos = np.arange(len(scenarios))

# Create a gradient color map
cmap = LinearSegmentedColormap.from_list("softpink", ["#ffe6e6", "#ffb3b3"])

# Plot the graph
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(y_pos, percentages, color=cmap(percentages / np.max(percentages)))

# Add text labels
for i, (p, label) in enumerate(zip(percentages, scenarios)):
    ax.text(p + 1, i, f"{p}%", va='center', fontsize=11)

# Set the title and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(scenarios, fontsize=12)
ax.invert_yaxis()  # The most popular scenario is displayed at the top
ax.set_xlim(0, 60)
ax.set_title("Research on Consumers' Wearing Scenarios of Bare - Leg Socks", fontsize=15, weight='bold')

# Remove the frame and redundant tick marks
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# Add the data source
source_text = "Data Source: CBNData Research Data in July 2024\nBig Data: Full Insight"
plt.figtext(0.5, -0.05, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()