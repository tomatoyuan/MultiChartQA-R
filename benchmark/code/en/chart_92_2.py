import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2016, 2017, 2018, 2019, 2020, 2021]
# New energy vehicle production (in 10,000 units, simulated data)
production = [52, 79, 127, 124, 137, 355]
# Growth rate (%, simulated data)
growth_rates = [53.6, 59.9, -2.2, 10.0, 159.5]  # Note: There is no growth rate for 2016 (compared with the previous year). According to the data logic in the figure, the growth rate points start from 2017.

# Create a canvas and sub - plots
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 700)

# Draw a bar chart (production)
ax1.bar(years, production, color="#A4C639", label="Production (in 10,000 units)")
ax1.set_ylabel("Production (in 10,000 units)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Create a secondary y - axis to draw a line chart (growth rate)
ax2 = ax1.twinx()

ax2.set_ylim(-100, 200)

# The x - axis of the line chart takes values from 2017 to 2021 (corresponding to the growth rate data points), which is consistent with the original figure.
ax2.plot(years[1:], growth_rates, marker='o', color="#87CEEB", label="Growth rate (%)", linewidth=2)
ax2.set_ylabel("Growth rate (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Add data labels to the bar chart
for x, y in zip(years, production):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  # Fine - tune the label position
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Add data labels to the line chart (Note: Only label from 2017 to 2021)
for x, y in zip(years[1:], growth_rates):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(-2, 15),  # Fine - tune the label position
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Set the x - axis tick marks
ax1.set_xticks(years)
# Set the title
ax1.set_title("New energy vehicle production in China from 2016 to 2021", fontsize=14, fontweight="bold")

# Combine the legends (Note: The line chart starts from 2017, and the legend display needs to be adjusted)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()