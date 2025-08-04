import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ['Beijing', 'Shenzhen', 'Chengdu', 'Shanghai', 'Hangzhou']
# Search percentages corresponding to each city (estimated based on the chart, you can replace with accurate data)
percentages = [5.5, 3.5, 2.9, 2.8, 2.7]  

x = np.arange(len(cities))  # x-axis coordinates

fig, ax = plt.subplots()
# Draw a bar chart and set the bar color to blue
rects = ax.bar(x, percentages, color='blue')  

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(cities)
# Set the y-axis range
ax.set_ylim([0, 6])  
# Set y-axis ticks
ax.set_yticks(np.arange(0, 7, 1))  
# Add a chart title
ax.set_title('Top 5 Cities for Legal Services Industry Search in May')  
# Add a y-axis label
ax.set_ylabel('Search Percentage (%)')  

# Annotate the values on the bars (optional, to make the chart information more intuitive)
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # Vertical distance of the value annotation from the bar
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()