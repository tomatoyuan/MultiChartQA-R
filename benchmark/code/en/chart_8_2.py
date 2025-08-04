import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Computer - side retrieval proportion', 'Mobile - side retrieval proportion']
sizes = [12.03, 87.97]
# Colors, can be adjusted as needed
colors = ['#b3d1ff', '#ff9966']  

# Create a figure and a subplot
fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops is used to set the ring width
ax.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=colors,
       wedgeprops={'width': 0.3})  

# Set the title (optional, add according to needs)
ax.set_title('Retrieval proportion distribution in the divorce litigation industry')  

plt.show()