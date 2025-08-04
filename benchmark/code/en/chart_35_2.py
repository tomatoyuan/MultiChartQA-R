import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Death from chronic diseases', 'Death from other causes']
sizes = [88.5, 100 - 88.5]  # Proportions, the sum is 100
colors = ['#008040', '#D3D3D3']  # Green and gray similar to the original chart

# Create a figure and axes
fig, ax = plt.subplots()

# Draw a donut chart, wedgeprops is used to set the width of the ring
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       colors=colors, wedgeprops={'width': 0.3})

# Set the title
ax.set_title('Proportion of deaths caused by chronic diseases in the total number of deaths in China in 2019', y=-0.15, fontsize=12, fontweight='bold')

# Make the pie chart circular
ax.axis('equal')

# Display the chart
plt.show()