import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
# Market size data (roughly simulated, close to the actual situation)
market_size = np.array([2000, 2500, 2700, 2800, 3000, 3300])  

# Create a canvas
fig, ax = plt.subplots()
# Draw a bar chart, set the color to blue, similar to the original image
ax.bar(years, market_size, color='#4B79A1')  

# Add a title, match the title format of the original image
ax.set_title('Urban (Big Cat) Consumption Market Size from 2020 to 2025', fontdict={'fontsize': 12})  
# Set the x-axis label
ax.set_xlabel('Year')  
# Set the y-axis label
ax.set_ylabel('Market Size (Billion Yuan)')  

# Mark the text annotation for the first time exceeding 300 billion in 2024, the position can be fine - tuned
ax.text(2024, 3000 + 50, 'First exceeded 300 billion', ha='center', va='bottom', fontsize=10, color='orange')  

# Set the x-axis ticks, display 2025 as 2025E
ax.set_xticks(years)
ax.set_xticklabels([str(year) + 'E' if year == 2025 else str(year) for year in years])

# Set the y-axis tick range to make the display more suitable for the data
ax.set_ylim(0, 3500)  

# Display the chart
plt.show()