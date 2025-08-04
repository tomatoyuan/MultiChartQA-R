import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2019, 2024)
# Myopia population in China (in hundreds of millions)
myopia_pop = [6.0, 6.5, 6.9, 6.9, 7.0]
# Total population in China (in hundreds of millions)
total_pop = [14.1, 14.2, 14.6, 14.6, 14.6]
# Proportion of myopia population (%)
myopia_ratio = [42.6, 45.8, 47.3, 47.3, 47.9]

x = np.arange(len(years))  # x-axis tick positions

fig, ax1 = plt.subplots(figsize=(12, 6))  # Adjust the chart size

# Adjust the width and position of the bar chart to avoid overlap
width = 0.35
rects1 = ax1.bar(x - width/2, myopia_pop, width, label='Myopia population in China (in hundreds of millions)', color='greenyellow', alpha=0.8)
rects2 = ax1.bar(x + width/2, total_pop, width, label='Total population in China (in hundreds of millions)', color='dodgerblue', alpha=0.8)

ax1.set_ylabel('Population (in hundreds of millions)', fontsize=12)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.legend(loc='lower center')
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines

# Create a second y-axis to draw a line chart
ax2 = ax1.twinx()
ax2.plot(x, myopia_ratio, marker='o', markersize=8, label='Proportion of myopia population (%)', color='blue', linewidth=2.5)
ax2.set_ylabel('Proportion (%)', fontsize=12)
ax2.set_ylim(40, 50)  # Adjust the y-axis range
ax2.legend(loc='upper left')

# Add numerical labels to the bar chart
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # Vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

autolabel(rects1)
autolabel(rects2)

# Add numerical labels to the line chart
for i, ratio in enumerate(myopia_ratio):
    ax2.annotate(f'{ratio}%',
                 xy=(x[i], ratio),
                 xytext=(0, 8),  # Vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))

plt.title('Myopia population and its proportion in China from 2019 to 2023', fontsize=15, pad=15)
plt.tight_layout()  # Optimize the layout
plt.show()