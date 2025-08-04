import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# Year data
years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
# Internet penetration rate data
rates = np.array([59.6, 64.5, 70.4, 73.0, 75.6, 77.5, 78.6])

# Create a bar chart
fig, ax = plt.subplots()
bars = ax.bar(years, rates, color='orange')

# Label the value on each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height,
            f'{height}',
            ha='center', va='bottom')

# Set the chart title and axis labels
ax.set_title('China Internet Penetration Rate from 2018 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Penetration Rate (%)')

# Display the chart
plt.show()