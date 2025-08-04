import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Years
years = np.arange(2012, 2017)  
# Simulated data, roughly following the trend of the original chart, copyright income, commercial sponsorship, resource exchange
copyright_income = [0.5, 0.6, 0.6, 1, 10]  
sponsorship_income = [1, 2, 4.5, 8, 5]
resource_swap = [1, 1.2, 1.5, 1.6, 1.7]  

# Create a chart
fig, ax = plt.subplots(figsize=(10, 6))  # Increase the chart size

# Set the background grid and color
ax.set_facecolor('#f8f9fa')
ax.grid(True, linestyle='--', alpha=0.7)

# Draw three lines with more beautiful colors and markers
line1, = ax.plot(years, copyright_income, color='#3498db', label='Copyright Income', linewidth=3, marker='o', markersize=8)
line2, = ax.plot(years, sponsorship_income, color='#e74c3c', label='Commercial Sponsorship', linewidth=3, marker='s', markersize=8)
line3, = ax.plot(years, resource_swap, color='#2ecc71', label='Resource Exchange', linewidth=3, marker='^', markersize=8)

# Set the title and subtitle
ax.set_title('Income Trend Analysis from 2012 to 2016', fontsize=18, fontweight='bold', pad=20)

# Set the axis labels and ticks
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Income (Billion Yuan)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels([f'{year}' for year in years], fontsize=10)
ax.set_yticks(np.arange(0, 11, 2.5))

# Add numerical labels to each data point
for x, y in zip(years, copyright_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)
for x, y in zip(years, sponsorship_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)
for x, y in zip(years, resource_swap):
    ax.annotate(f'{y}', (x, y), textcoords='offset points', 
                xytext=(0,10), ha='center', fontsize=9)

# Highlight the growth of copyright income
ax.fill_between(years, copyright_income, 0, color='#3498db', alpha=0.1)

# Adjust the legend position and style
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), 
          fancybox=True, shadow=True, ncol=3, fontsize=11)

plt.tight_layout()  # Adjust the layout
plt.show()