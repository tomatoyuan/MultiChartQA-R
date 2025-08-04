import matplotlib.pyplot as plt
import numpy as np

# Platform names
platforms = ["Tiktok", "Youtube", "Instagram", "Facebook", "Twitter", "Others"]
# Corresponding data
data = [30.0, 22.0, 22.0, 14.0, 4.0, 13.0]

x = np.arange(len(platforms))  # Used to set the position of the x-axis
bar_width = 0.5  # Width of the bar chart

fig, ax = plt.subplots()
# Draw the bar chart, set the color, width, etc. The color is as close to blue as possible
bars = ax.bar(x, data, width=bar_width, color="#64B5F6", edgecolor="white")  

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical distance of the label from the bar chart
                textcoords="offset points",
                ha='center', va='bottom')

# Set the x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(platforms)
# Set the y-axis label (The original chart does not show the y-axis label. You can decide whether to add it according to your needs)
# ax.set_ylabel("Percentage (%)")
# Set the chart title
ax.set_title("Platforms Preferred by Overseas Creators for Content Publishing")

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.show()