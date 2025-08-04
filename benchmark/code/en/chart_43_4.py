import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Audio-visual equipment (Smart speakers, Smart headphones)", "Electronic education products (Learning machines, etc.)", "Computer hardware/Monitors/Computer peripherals", 
              "Photography and videography products", "Game consoles and accessories (Switch, PS, etc.)", "Never purchased"]
percentages = [51.1, 36.4, 34.2, 23.0, 17.5, 13.1]

# Create a figure and axes
fig, ax = plt.subplots()

# Draw a bar chart
bars = ax.bar(categories, percentages, color='cyan')

# Set the title and labels
ax.set_title('Proportion of women who purchased various digital 3C products in the past year')
ax.set_ylabel('Proportion (%)')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Add numerical labels above each bar
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{percentage}%', ha='center', va='bottom')

# Display the graph
plt.tight_layout()
plt.show()