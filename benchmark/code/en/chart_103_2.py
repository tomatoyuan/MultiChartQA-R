import matplotlib.pyplot as plt
import numpy as np

# 1. Extract chart data
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
# Market size of various ready-to-eat food categories (in billions of yuan)
meat = [714, 829, 977, 1224, 1544, 2069, 2668, 3289]        # Meat
seafood = [648, 733, 856, 1047, 1237, 1595, 2089, 2576]     # Seafood
vegetable = [350, 480, 588, 676, 835, 1186, 1416, 1625]     # Vegetable
# Total market size (in billions of yuan)
total = [1712, 2042, 2421, 2947, 3616, 4850, 6173, 7490]
# Year-on-year growth rate (%)
growth = [19.3, 18.6, 21.7, 22.7, 34.2, 27.3, 21.3]

# 2. Draw combined chart (bar chart + line chart)
x = np.arange(len(years))  # x-axis coordinates
width = 0.2  # Bar width

fig, ax1 = plt.subplots(figsize=(14, 8))

# Draw stacked bar chart for three categories of ready-to-eat foods
bottom = np.zeros(len(years))
for i, (data, label, color) in enumerate(zip(
    [meat, seafood, vegetable], 
    ['Meat Ready-to-Eat', 'Seafood Ready-to-Eat', 'Vegetable Ready-to-Eat'], 
    ['#FF5722', '#FF9800', '#FFC107']
)):
    bars = ax1.bar(x, data, width, bottom=bottom, label=label, color=color)
    # Annotate the values of each category
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 50:  # Only annotate bars with sufficient height to avoid overcrowding
            ax1.text(
                bar.get_x() + bar.get_width()/2., 
                bottom[j] + height/2,
                f'{data[j]}',
                ha='center', va='center',
                color='black', fontsize=8
            )
    bottom += data

# Annotate total market size values
for i, val in enumerate(total):
    ax1.text(x[i], total[i] + 80, f'{val}', ha='center', fontsize=10, color='#333')

# Configure left y-axis (market size)
ax1.set_ylabel('Market Size (Billion Yuan)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create right y-axis for year-on-year growth rate
ax2 = ax1.twinx()
ax2.plot(x[:-1], growth, marker='o', color='#FDD835', label='YoY Growth (%)', linewidth=2)

# Annotate growth rate values
for i, val in enumerate(growth):
    ax2.text(x[i], val + 1, f'{val}%', ha='center', fontsize=9, color='#FDD888')

ax2.set_ylabel('Year-on-Year Growth (%)', fontsize=12, color='#FDD888')
ax2.tick_params(axis='y', labelcolor='#FDD888')
ax2.legend(loc='center right')

# 3. Overall chart configuration
plt.title('Market Size and Forecast of China\'s Ready-to-Eat Food Industry, 2019-2026', fontsize=14, pad=20)
plt.tight_layout()
plt.show()