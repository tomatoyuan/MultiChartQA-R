import matplotlib.pyplot as plt
import numpy as np

# Educational attainment categories
labels = ['Postgraduate and above', 'Undergraduate', 'High school', 'Junior high school', 'Below junior high school']
# Hypothetical proportion of people interested in each educational attainment level (replace with actual data, this is just an example)
sizes = [10, 30, 25, 20, 15]  

# Create a figure and a sub - plot
fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       wedgeprops={'width': 0.3})  
ax.axis('equal')  # Ensure the pie chart (donut) is drawn as a circle

plt.title('Educational attainment distribution of the interested population')
plt.show()