import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ["Shenzhen", "Beijing", "Guangzhou", "Wuhan", "Changsha"]
ranking = [1, 2, 3, 4, 5]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(cities, ranking, color='#6CB4EE')

# Add ranking numbers to each bar
for i, v in enumerate(ranking):
    plt.text(v + 0.1, i, str(v), va='center', fontsize=12)

# Add title and labels
plt.title('Ranking List of Cities for Blind Dates', fontsize=16, pad=15)
plt.xlabel('Ranking', fontsize=12, labelpad=10)
plt.ylabel('City', fontsize=12, labelpad=10)

# Set the x-axis range
plt.xlim(0, max(ranking) + 1)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()