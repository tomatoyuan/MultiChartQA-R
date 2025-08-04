import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2016, 2017, 2018, 2019, 2020, 2021]
# Per capita consumption expenditure on transportation and communication of residents (yuan, simulated data)
expenditures = [2338, 2499, 2675, 2862, 2761, 3156]
# Growth rate (%, simulated data)
growth_rates = [12.0, 6.9, 7.0, 7.0, -3.5, 14.3]

# Create a canvas and sub - plots
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 6000)

# Draw a bar chart (consumption expenditure)
ax1.bar(years, expenditures, color="#A4C639", label="Per capita consumption expenditure on transportation and communication of residents (yuan)")
ax1.set_ylabel("Consumption expenditure (yuan)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Create a secondary y - axis to draw a line chart (growth rate)
ax2 = ax1.twinx()

ax2.set_ylim(-50, 25)

ax2.plot(years, growth_rates, marker='o', color="#87CEEB", label="Growth rate (%)", linewidth=2)
ax2.set_ylabel("Growth rate (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Add data labels to the bar chart
for x, y in zip(years, expenditures):
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

# Set x - axis ticks
ax1.set_xticks(years)
# Set the title
ax1.set_title("Per capita consumption expenditure on transportation and communication of Chinese residents from 2016 to 2021", fontsize=14, fontweight="bold")

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()