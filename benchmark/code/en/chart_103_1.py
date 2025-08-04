import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# Years
years = np.arange(2015, 2025)
# Output data (in ten thousand tons)
outputs = [6210.97, 6379.48, 6445.33, 6457.66, 6480.36, 
           6549.02, 6690.29, 6865.91, 7116.24, 7366.50]

# Create a canvas and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(years, outputs, color='#FFA07A')  # Set the color of the bar chart

# Add numerical annotations
for bar, output in zip(bars, outputs):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, 
            f'{output}', ha='center', va='bottom')

# Set the title and axis labels
ax.set_title('Total Aquatic Product Output in China from 2015 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Output (in ten thousand tons)')

# Set the y-axis range
ax.set_ylim(5600, 7600)  

# Display the chart
plt.show()