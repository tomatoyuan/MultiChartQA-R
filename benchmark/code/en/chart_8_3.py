import matplotlib.pyplot as plt
import numpy as np

# City levels
city_levels = ['First-tier cities', 'Second-tier cities', 'Third-tier cities', 'Fourth-tier cities']
# Proportion data (for bar chart)
proportion = [52, 15, 14, 10]
# Growth rate data (for line chart)
growth_rate = [3, -18, -30, -18]

x = np.arange(len(city_levels))  # X-axis indices

fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the chart size

# Draw the bar chart (proportion)
bars = ax1.bar(x, proportion, color='blue', label='Proportion')
ax1.set_ylabel('Proportion (%)', color='blue')
ax1.set_xlabel('City levels')
ax1.set_xticks(x)
ax1.set_xticklabels(city_levels)
ax1.tick_params(axis='y', labelcolor='blue')

# Add data labels to the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center',
                 va='bottom',
                 color='blue')

# Create a second y-axis to draw the line chart (growth rate)
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_rate, color='orange', label='Growth rate', marker='o', markersize=6)
ax2.set_ylabel('Growth rate (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add data labels to the line chart
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%',
                 xy=(x[i], rate),
                 xytext=(5, 5) if rate >= 0 else (5, -5),  # Adjust the position according to positive or negative
                 textcoords="offset points",
                 ha='left',
                 va='bottom' if rate >= 0 else 'top',
                 color='orange',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Add a legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# Set the title
plt.title('Attention proportion and growth rate of the divorce lawsuit industry by city level in May')

# Add grid lines
ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()  # Ensure all elements fit in the chart area
plt.show()