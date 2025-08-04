import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.array([2022, 2023, 2024, 2025, 2026])
# Market size data (in billions of yuan), roughly simulating the trend of the original data
market_size = np.array([1804, 2045, 2284, 2510, 2737])

# Create a figure and set a reasonable size
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart and save the returned container object
bars = ax.bar(years, market_size, color='r', label='Market Size (in billions of yuan)')
ax.set_xlabel('Year')
ax.set_ylabel('Market Size (in billions of yuan)', color='r')
ax.tick_params(axis='y', labelcolor='r')

# Set the x-axis tick marks to years
ax.set_xticks(years)

# Generate year labels with 'E'
year_labels = []
for year in years:
    if year in [2025, 2026]:
        year_labels.append(f"{year}E")  # Add 'E' for predicted years
    else:
        year_labels.append(str(year))   # Keep actual years unchanged

# Set year labels with 'E'
ax.set_xticklabels(year_labels)

# Label the value above each bar (without 'E')
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.,  # x-coordinate: center of the bar
        height + 15,  # y-coordinate: 15 units above the top of the bar
        f'{height}',  # Display the value
        ha='center',  # Horizontal center alignment
        va='bottom',  # Vertical bottom alignment
        color='r',    # Text color is the same as the bar
        fontsize=10   # Font size
    )

# Add a title
plt.title('Market Size of Spicy Snacks in China from 2022 to 2026 (in billions of yuan)')

# Use the fig.text() method to add annotations
fig.text(0.5, 0.85, 'Spicy snacks are about 1.6 times the CAGR of the snack food industry',
         ha='center', fontsize=10)

fig.text(0.15, 0.80, '*CAGR of the snack food industry = 6.0%', fontsize=8)

# Add a legend
ax.legend(loc='upper left')

# Adjust the layout
plt.tight_layout()
# Display the chart
plt.show()