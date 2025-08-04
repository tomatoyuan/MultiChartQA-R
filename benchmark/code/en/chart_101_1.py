import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E", "2025E"]
market_size = [15.9, 26.5, 49.1, 148.3, 278.0, 392.0, 675.0, 1126.5, 1802.7, 2296.6, 2808.8]  # Market size (in billions of yuan)
yoy_growth = [66.7, 85.3, 202.0, 87.5, 41.0, 72.2, 66.9, 60.0, 27.4, 22.3]  # Year-on-year growth rate (%), note that there is no year-on-year growth for 2015 (or it can be adjusted according to requirements). Here, the growth rate data starts from 2016, aligning with the chart logic

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the left y-axis (market size, bar chart)
ax1.bar(x, market_size, color="#ee8208", width=0.6, label="Market Size (in billions of yuan)")
ax1.set_ylabel("Market Size (in billions of yuan)", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# Create the right y-axis (year-on-year growth rate, line chart)
ax2 = ax1.twinx()
ax2.plot(x[1:], yoy_growth, color="#ffd700", marker="o", label="Year-on-Year Growth Rate (%)")  # Start plotting the line from 2016, corresponding to x[1:]
ax2.set_ylabel("Year-on-Year Growth Rate (%)", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# Add market size value annotations (on the bar chart)
for i, size in enumerate(market_size):
    ax1.text(x[i], size + 50, f'{size}', ha="center", va="bottom", color="#ee8208")

# Add year-on-year growth rate value annotations (on the points of the line chart)
for i, growth in enumerate(yoy_growth):
    ax2.text(x[i + 1], growth + 2, f'{growth}%', ha="center", va="bottom", color="#ffd700")  # Corresponding to x[1:], so the index is +1

# Combine legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

ax1.set_title("2015 - 2025 China Knowledge Payment Market Size and Forecast", fontsize=14)
plt.tight_layout()
plt.show()