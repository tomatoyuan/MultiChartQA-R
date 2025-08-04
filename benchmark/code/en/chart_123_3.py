import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025E", "2026E", "2027E"]
# Market size (in billions of yuan)
market_size = [3013, 4597, 5980, 6680, 10036, 11161, 15254, 16357, 17469, 18503, 19567]
# Year-on-year growth (%)
yoy_growth = [52.6, 30.1, 16.9, 11.7, 50.2, 11.2, 36.7, 7.2, 6.8, 5.9, 5.8]
# Penetration rate of the online food delivery industry (%)
penetration_rate = [7.6, 10.9, 12.8, 11.7, 21.4, 25.4, 28.8, 28.0, 28.0, 28.0, 28.0]  # The penetration rate for some years needs to be confirmed according to the graph. Here, it is assumed to remain at 28.0 after 2023 and can be adjusted according to the actual situation.

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Draw the bar chart of market size
ax1.bar(x, market_size, color='orange', label='Market Size (in billions of yuan)')
ax1.set_ylabel('Market Size (in billions of yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and draw the line charts of year-on-year growth and penetration rate
ax2 = ax1.twinx()
ax2.plot(x, yoy_growth, marker='o', color='brown', label='Year-on-Year Growth (%)')
ax2.plot(x, penetration_rate, marker='o', color='blue', label='Penetration Rate of Online Food Delivery Industry (%)')
ax2.set_ylabel('Percentage (%)')
ax2.legend(loc='upper right')

# Add value labels for market size
for i, size in enumerate(market_size):
    ax1.text(i, size + 200, f'{size}', ha='center', va='bottom')

# Add value labels for year-on-year growth
for i, growth in enumerate(yoy_growth):
    ax2.text(i, growth + 1, f'{growth}%', ha='center', va='bottom')

# Add value labels for penetration rate
for i, rate in enumerate(penetration_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('China Online Food Delivery Market Size and Penetration Rate from 2017 to 2027')

plt.tight_layout()
plt.show()