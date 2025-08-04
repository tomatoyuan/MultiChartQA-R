import matplotlib.pyplot as plt
import numpy as np

# Date labels
labels = ["15th of the 12th lunar month", "16th of the 12th lunar month", "17th of the 12th lunar month",
          "18th of the 12th lunar month", "19th of the 12th lunar month", "20th of the 12th lunar month",
          "21st of the 12th lunar month", "22nd of the 12th lunar month", "23rd of the 12th lunar month",
          "24th of the 12th lunar month", "25th of the 12th lunar month", "26th of the 12th lunar month",
          "27th of the 12th lunar month", "28th of the 12th lunar month", "29th of the 12th lunar month",
          "New Year's Eve"]
# Simulated data, generally showing a peak trend, can be fine - tuned according to actual situation
data = [5, 8, 10, 7, 9, 11, 12, 13, 14, 18, 15, 16, 17, 20, 19, 6]
# Index of peak dates (24th and 28th of the 12th lunar month, corresponding to indices 9 and 13 in the above labels)
peak_indices = [9, 13]

x = np.arange(len(labels))  # x - axis positions
width = 0.6  # Bar width

fig, ax = plt.subplots(figsize=(10, 6))  # Create a canvas and axes
# Draw the bar chart, most bars in one color, peak bars in another color
bars = []
for i in range(len(x)):
    if i in peak_indices:
        bar = ax.bar(x[i], data[i], width, color='#e65142')  # Peak color, similar to the red in the original chart
    else:
        bar = ax.bar(x[i], data[i], width, color='#80cbc4')  # Other bars' color, similar to the cyan - green in the original chart
    bars.append(bar)

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# Set the title
ax.set_title('Two peaks for ticket - grabbing: 24th and 28th of the 12th lunar month', fontsize=16, pad=20)

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add some decorative elements, simulating the small sun and clouds in the original chart (simply indicated, can be refined according to requirements)
import matplotlib.patches as patches
# Draw a small sun
sun = patches.Circle((1, max(data) + 2), radius=1, color='yellow', alpha=0.8)
ax.add_patch(sun)
# Draw clouds (simulated by simple rectangles, can be drawn more precisely)
cloud1 = patches.Rectangle((3, max(data) + 1.5), 2, 1, color='white', alpha=0.8)
cloud2 = patches.Rectangle((6, max(data) + 1), 2, 1, color='white', alpha=0.8)
ax.add_patch(cloud1)
ax.add_patch(cloud2)

plt.tight_layout()  # Automatically adjust the layout
plt.show()