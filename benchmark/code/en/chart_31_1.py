import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare data
# City names
cities = ["Beijing", "Xiamen", "Hangzhou", "Harbin"]
# Simulate search heat values here (unit: 10,000 times)
search_heat = [8, 6, 4, 2]

x = np.arange(len(cities))  # Used to locate the bars of each city on the X - axis

# 2. Create a chart
fig, ax = plt.subplots()
# Draw a bar chart and set the bar color, width and other styles
rects = ax.bar(x, search_heat, color=['#FF6347', '#FFA07A', '#FFD700', '#FFFF00'])

# 3. Customize the chart content
ax.set_xticks(x)  # Set the tick positions on the X - axis
ax.set_xticklabels(cities)  # Use city names as tick labels on the X - axis
ax.set_ylabel("Search Heat (10,000 times)")  # Set the title of the Y - axis and add the unit
ax.set_title("Regional Distribution of Search for Travel Safety during Short Holidays", fontsize=14, fontweight='bold')  # Set the chart title

# Label the values on the bars and add the unit
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}K',  # Add "K" to represent 10,000
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # The vertical distance of the value label from the top of the bar
                textcoords="offset points",
                ha='center', va='bottom')

# 4. Display the chart
plt.show()