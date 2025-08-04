import matplotlib.pyplot as plt
import numpy as np

# First pie chart data
labels_1 = ['Made a deal between April and May', 'Others']
sizes_1 = [86, 14]  # Data is roughly consistent, and the sum is 100
colors_1 = ['#4fa3e1', '#c7b8e0']  # Colors are close to the original image

# Second pie chart data
labels_2 = ['Visited between April and May', 'Others']
sizes_2 = [94, 6]  # Data is roughly consistent, and the sum is 100
colors_2 = ['#4fa3e1', '#f1c4e0']  # Colors are close to the original image

# Create a canvas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Set the overall title
fig.suptitle('Analysis of the behavior of users who made a deal during the 618 promotion between April and May', fontsize=16, fontweight='bold')

# Draw the first pie chart
ax1.pie(sizes_1, labels=labels_1, autopct='%1.0f%%', startangle=90, colors=colors_1)

# Draw the second pie chart
ax2.pie(sizes_2, labels=labels_2, autopct='%1.0f%%', startangle=90, colors=colors_2)

# Make the pie charts appear as perfect circles
for ax in [ax1, ax2]:
    ax.axis('equal')

plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Adjust the distance between the sub - plots and the top
plt.show()