import matplotlib.pyplot as plt
import numpy as np

# Time period labels
labels = ["00:00", "05:00", "10:00", "15:00", "20:00"]
# Simulated proportion data (can be replaced according to actual needs, values here are for demonstration), values are just examples
sizes = [10, 10, 50, 15, 15]  
# Gap in the donut chart (to make the donut more obvious), here set uniformly to 0.3, can be adjusted
explode = [0.3] * len(labels)  

fig, ax = plt.subplots()

# Draw a donut chart, wedgeprops controls the width and other styles of the donut
ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",  # Display percentage
    startangle=90,      # Starting angle
    wedgeprops={"width": 0.3, "edgecolor": "white"},  # Donut width, edge color
    textprops={"fontsize": 12}  # Text font size
)
ax.set_title("When do people most want to 'shop till they drop' on 'Double Eleven'?", fontsize=16, fontweight="bold")

# Keep the pie chart circular (to avoid stretching and distortion)
ax.axis("equal")  

plt.show()