import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ["2019", "2020", "2021", "2022", "2023E", "2024E"]
market_size = [1945.3, 2283.0, 2793.7, 3387.1, 4020.8, 4744.5]  # Market size (in billions of yuan)
growth_rates = [17.4, 22.4, 21.2, 18.7, 18.0]  # Year-on-year growth rate (%), no previous data for 2019

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 7))

# Draw the bar chart of market size
bars = ax1.bar(x, market_size, color='coral', label='Market Size (in billions of yuan)')
ax1.set_ylabel('Market Size (in billions of yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and draw the line chart of year-on-year growth rate
ax2 = ax1.twinx()
line, = ax2.plot(x[1:], growth_rates, marker='o', color='gold', label='Year-on-Year Growth Rate (%)', linewidth=2)
ax2.set_ylabel('Year-on-Year Growth Rate (%)')
ax2.legend(loc='center right')

# Adjust y-axis limits to create space for annotations
ax2.set_ylim(0, max(growth_rates) * 1.2)

# Add annotations for growth rate values near the line
for i, rate in enumerate(growth_rates):
    x_pos = x[i+1]  # Align with corresponding year
    y_pos = rate
    # Adjust label position based on line slope
    if i < len(growth_rates) - 1:
        next_rate = growth_rates[i+1]
        if next_rate > rate:  # Upward slope
            va = 'bottom'
            y_offset = 0.5
        else:  # Downward slope
            va = 'top'
            y_offset = -0.5
    else:
        va = 'bottom'
        y_offset = 0.5
    
    ax2.annotate(f'{rate}%',
                xy=(x_pos, y_pos),
                xytext=(0, y_offset),
                textcoords="offset points",
                ha='center',
                va=va,
                color='black',
                fontweight='bold')

# Add annotations for market size values
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 50,
            f'{height}',
            ha='center', va='bottom', color='black')

ax1.set_title('Market Size and Forecast of Chinese Functional Slimming Foods from 2019 to 2024')
plt.tight_layout()
plt.show()