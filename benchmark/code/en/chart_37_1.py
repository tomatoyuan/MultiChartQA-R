import matplotlib.pyplot as plt
import numpy as np

# Channel names
channels = ["Live Streaming Room", "Short Video", "Graphic"]
# Corresponding channel proportion data
percentages = [89, 34, 16]

x = np.arange(len(channels))  # x-axis positions
width = 0.5  # Bar width

fig, ax = plt.subplots()
# Draw a bar chart with a brown color similar to the original image
bars = ax.bar(x, percentages, width, color='#C09A7B')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(channels)
# Set the y-axis range
ax.set_ylim(0, 100)

# Display the percentage value on each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}%'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical distance of the value from the bar
                textcoords="offset points",
                ha='center', va='bottom')

# Set the chart title
ax.set_title('Main Channels for Consumers to Purchase Autumn and Winter Clothing on Douyin E-commerce')

plt.show()