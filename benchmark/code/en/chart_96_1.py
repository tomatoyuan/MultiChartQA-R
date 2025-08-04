import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# MPV sales (in 10,000 vehicles, simulated data)
sales = [49.8, 49.3, 130.5, 191.4, 210.7, 249.7, 207.1, 173.5, 138.4, 105.4, 105.5]
# Annual growth rate (%, simulated data)
growth_rates = [11.7, -0.9, 164.5, 46.7, 10.1, 18.5, -17.1, -16.2, -20.2, -23.8, 0.1]

# Create a canvas and subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 500)

# Draw a bar chart (MPV sales)
ax1.bar(years, sales, color="#A4C639", label="MPV Sales (10,000 vehicles)")
ax1.set_ylabel("MPV Sales (10,000 vehicles)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Create a secondary y-axis to draw a line chart (growth rate)
ax2 = ax1.twinx()

ax2.set_ylim(-200, 200)

ax2.plot(years, growth_rates, marker='o', color="#87CEEB", label="Annual Growth Rate (%)", linewidth=2)
ax2.set_ylabel("Annual Growth Rate (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Add data labels to the bar chart
for x, y in zip(years, sales):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Add data labels to the line chart
for x, y in zip(years, growth_rates):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Set x-axis tick marks
ax1.set_xticks(years)
# Set the title
ax1.set_title("China MPV Sales and Growth Rate from 2011 to 2021", fontsize=14, fontweight="bold")

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()