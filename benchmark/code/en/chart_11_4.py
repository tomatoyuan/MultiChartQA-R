import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['School Strength', 'Professional Interest', 'Geographical Location', 'Others']
values = [24, 36, 13, 27]
colors = ['#FF7F0E', '#2CA02C', '#FFD700', '#1F77B4']  # Corresponding colors

# Create a canvas and axes
fig, ax = plt.subplots()

# Draw a horizontal bar chart
ax.barh(labels, values, color=colors)

# Add data labels
for i, v in enumerate(values):
    ax.text(v + 1, i, str(v) + '%', va='center')

# Set the title
ax.set_title('When you have multiple schools to choose from, what do you pay more attention to?')

# Display the chart
plt.show()