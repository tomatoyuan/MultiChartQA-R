import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2023", "2024e", "2025e", "2026e", "2027e", "2028e"]
# Technology investment (in billions of yuan), roughly simulated and can be adjusted according to actual situation
tech_investment = [517.6, 586.7, 672.9, 771.3, 881.5, 1020.1]
# Growth rate (%), roughly simulated and can be adjusted according to actual situation
growth_rate = [13.4, 14.7, 14.6, 14.3, 15.7, 16.8]

x = np.arange(len(years))  # x-axis tick positions
bar_width = 0.5  # Bar width

fig, ax1 = plt.subplots(figsize=(14, 7))  # Further increase the chart width

# Draw the technology investment bar chart
bars = ax1.bar(x, tech_investment, width=bar_width, label='Technology Investment (Billion Yuan)', color='greenyellow')
ax1.set_ylabel('Technology Investment (Billion Yuan)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)

# Add numerical labels to the bar chart
for i, bar in enumerate(bars):
    height = bar.get_height()
    # Special handling for the last label position
    if i == len(bars) - 1:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(15, 10),  # Offset to the upper right
                    textcoords="offset points",
                    ha='left', va='bottom',  # Left-aligned, bottom-aligned
                    fontsize=10)
    else:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 8),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

# Create a second y-axis and draw the growth rate line chart
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_rate, marker='o', markersize=7, label='Growth Rate (%)', 
                color='dodgerblue', linewidth=2)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Add numerical labels to the line chart
for i, rate in enumerate(growth_rate):
    # Special handling for the last label position
    if i == len(growth_rate) - 1:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(15, -15),  # Offset to the lower right
                    textcoords="offset points",
                    ha='left', va='top',  # Left-aligned, top-aligned
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    else:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(-10, 10) if rate > 14.5 else (-10, -15),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# Add a title
ax1.set_title('China Insurance Industry Technology Investment from 2023 to 2028', fontsize=14, pad=15)

# Combine legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=11)

# Beautify the chart
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
plt.tight_layout()  # Automatically adjust the layout

plt.show()