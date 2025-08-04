import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024E", "2025E"]
# Market size (trillion yuan)
market_size = [22.6, 27.2, 31.3, 35.8, 39.2, 45.5, 50.2, 56.1, 63.2, 70.8]
# Year-on-year growth (%)
yoy_growth = [20.4, 21.4, 15.1, 14.4, 9.5, 16.1, 10.3, 11.7, 12.7, 12.1]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw the bar chart of market size (simulate the icon style, approximate with custom symbols)
for i in range(len(years)):
    # Draw the bar chart of the "¥" symbol representing the market size (simplified as an orange rectangle + text symbol)
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, market_size[i], color='orange')
    ax1.add_patch(rect)
    ax1.text(x[i], market_size[i] + 1, f'¥{market_size[i]}', ha='center', va='bottom')

ax1.set_ylabel('Market Size (Trillion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylim(0, max(market_size) + 5)  # Reserve space for labels
ax1.legend(['Market Size (Trillion Yuan)'], loc='upper left')

# Create a secondary y-axis and draw the line chart of year-on-year growth
ax2 = ax1.twinx()
ax2.plot(x, yoy_growth, marker='o', color='gold', label='Year-on-Year Growth (%)')
ax2.set_ylabel('Year-on-Year Growth (%)')
ax2.legend(loc='upper right')

# Add labels for year-on-year growth values
for i, growth in enumerate(yoy_growth):
    ax2.text(i, growth + 0.5, f'{growth}%', ha='center', va='bottom')

ax1.set_title('China\'s Total Digital Economy Scale and Forecast from 2016 to 2025')

plt.tight_layout()
plt.show()