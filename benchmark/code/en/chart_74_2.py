import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# Digital economy growth rate (%)
digital_economy_growth = [18.9, 20.3, 20.9, 15.6, 9.7, 16.2]
# GDP growth rate (%)
gdp_growth = [6.8, 6.9, 6.7, 6.0, 2.2, 8.1]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the digital economy growth rate line chart
digital_line, = ax.plot(years, digital_economy_growth, marker='o', color="#A4C639", label="Digital Economy Growth Rate (%)", linewidth=2)
# Plot the GDP growth rate line chart
gdp_line, = ax.plot(years, gdp_growth, marker='o', color="#64B5F6", label="GDP Growth Rate (%)", linewidth=2)

# Add data labels for the digital economy growth rate
for x, y in zip(years, digital_economy_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Add data labels for the GDP growth rate
for x, y in zip(years, gdp_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# Set the y - axis label
ax.set_ylabel("Growth Rate (%)")
# Set the title
ax.set_title("China's Digital Economy Growth Rate and GDP Growth Rate from 2016 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()