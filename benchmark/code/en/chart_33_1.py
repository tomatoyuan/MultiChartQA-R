import matplotlib.pyplot as plt
import numpy as np

# Year data
years = np.arange(2017, 2030)
# Simulated market size data (general trend is close, values can be fine - tuned according to actual situation)
market_size = [120, 125, 130, 133, 136, 139, 142, 145, 147, 149, 151, 153, 155]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart
bars = ax.bar(years, market_size, color='#6699cc', width=0.8)

# Add numerical labels above each bar
for bar, value in zip(bars, market_size):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{value}', ha='center', va='bottom')

# Mark the Compound Annual Growth Rate (CAGR) for two periods, manually find the position to mark here, and fine - tune the coordinates according to the actual situation
ax.text(2019, 140, '2017 - 2023\nCAGR: 1.85%', ha='center')
ax.text(2026, 140, '2024 - 2029E\nCAGR: 1.31%', ha='center')

# Add a vertical line to separate the two periods
ax.axvline(x=2024, color='gray', linestyle='--')

# Set the x - axis tick labels, add the "E" identifier to the years after 2025
xtick_labels = [str(year) if year < 2025 else f"{year}E" for year in years]
ax.set_xticks(years)
ax.set_xticklabels(xtick_labels, rotation=45)

# Set the chart title
ax.set_title('China Clothing Cleaning Market Size from 2014 to 2029')

# Display the chart
plt.tight_layout()  # Adjust the layout to avoid label occlusion
plt.show()