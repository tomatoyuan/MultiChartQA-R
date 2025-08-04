import matplotlib.pyplot as plt
import numpy as np

# Year data
years = np.arange(2018, 2025)
# Simulated CR5 data
cr5_data = [56, 57, 53, 52, 52, 52, 53]

# Create a figure
plt.figure(figsize=(10, 6))

# Plot a line chart with data markers using a more professional blue color
line, = plt.plot(years, cr5_data, color='#1f77b4', marker='o', markersize=8, 
                 linewidth=2.5, markeredgecolor='white', markeredgewidth=1.5)

# Add data labels
for x, y in zip(years, cr5_data):
    plt.annotate(f'{y}', (x, y), textcoords='offset points',
                 xytext=(0, 10), ha='center', fontsize=10)

# Set axes and tick marks
plt.xticks(years, fontsize=12)
plt.ylim(48, 60)  # Adjust the Y-axis range to make the chart more compact
plt.yticks(np.arange(48, 61, 2), fontsize=12)

# Add grid lines to enhance readability
plt.grid(True, linestyle='--', alpha=0.7)

# Add a title and labels with a more professional font size
plt.title('Analysis of Market Concentration in China\'s Laundry and Cleaning Care Market from 2018 to 2024', fontsize=16, pad=15)
plt.xlabel('Year', fontsize=14, labelpad=10)
plt.ylabel('Market Concentration (%)', fontsize=14, labelpad=10)

# Beautify the legend
plt.legend([line], ['CR5 Market Concentration'], fontsize=12, loc='upper right')

# Adjust the chart layout
plt.tight_layout()

# Display the chart
plt.show()