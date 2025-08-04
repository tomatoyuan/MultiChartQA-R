import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# Number of stores (in ten thousand, simulated data)
store_count = [339, 506, 602, 579, 657, 906, 917, 891]
# Year-on-year growth rate (%, simulated data)
growth_rate = [49.3, 19.0, -3.8, 13.5, 37.9, 1.2, -2.8]

# Create a canvas and subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 2000)

# Draw a bar chart (number of stores)
ax1.bar(years, store_count, color="#A4C639", label="Number of Stores (in ten thousand)")
ax1.set_ylabel("Number of Stores (in ten thousand)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Create a secondary y-axis to draw a line chart (growth rate)
ax2 = ax1.twinx()

ax2.set_ylim(-125, 100)

ax2.plot(years[:-1], growth_rate, marker='o', color="#87CEEB", label="Year-on-Year Growth Rate (%)", linewidth=2)
ax2.set_ylabel("Year-on-Year Growth Rate (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Add data labels to the bar chart
for x, y in zip(years, store_count):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Add data labels to the line chart
for x, y in zip(years[:-1], growth_rate):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="black")

# Set x-axis tick labels
ax1.set_xticks(years)
# Set the title
ax1.set_title("Number of Chinese Catering Stores from 2014 to 2021", fontsize=14, fontweight="bold")

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()