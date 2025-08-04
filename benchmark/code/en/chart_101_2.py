import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023E", "2024E", "2025E"]
user_scale = [0.5, 1.0, 1.9, 3.0, 3.6, 4.2, 4.8, 5.3, 5.7, 6.1, 6.4]  # User scale (hundred million people)
yoy_growth = [100.0, 95.8, 56.9, 20.7, 17.4, 14.1, 10.5, 8.5, 7.1, 4.8]  # Year-on-year growth rate (%), note that there is no year-on-year data for 2015 (or logically, the growth rate in 2016 corresponds to the change from 2015 - 2016, here aligned with the chart data)

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Draw the left y - axis (user scale, bar chart)
ax1.bar(x, user_scale, color="#ee8208", width=0.6, label="User Scale (Hundred Million People)")
ax1.set_ylabel("User Scale (Hundred Million People)", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# Create the right y - axis (year - on - year growth rate, line chart)
ax2 = ax1.twinx()
ax2.plot(x[1:], yoy_growth, color="#ffd700", marker="o", label="Year-on-Year Growth Rate (%)")  # The growth rate starts from 2016 (x[1:]) corresponding to the data
ax2.set_ylabel("Year-on-Year Growth Rate (%)", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# Add user scale value annotations (on the bar chart)
for i, scale in enumerate(user_scale):
    ax1.text(x[i], scale + 0.2, f'{scale}', ha="center", va="bottom", color="#ee8208")

# Add year - on - year growth rate value annotations (on the points of the line chart)
for i, growth in enumerate(yoy_growth):
    ax2.text(x[i + 1], growth + 2, f'{growth}%', ha="center", va="bottom", color="#ffd700")  # Corresponding to x[1:], index +1 for alignment

# Combine legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="center left")

ax1.set_title("Scale and Forecast of Chinese Knowledge Payment Consumers from 2015 to 2025", fontsize=14)
plt.tight_layout()
plt.show()