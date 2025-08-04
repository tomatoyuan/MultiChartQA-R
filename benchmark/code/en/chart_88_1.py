import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2000, 2005, 2010, 2014, 2020]
# Adult obesity rates (%)
obesity_rates = [7.0, 8.0, 9.9, 10.5, 14.6]
# Adult overweight rates (%)
overweight_rates = [22.8, 29.1, 32.1, 32.7, 35.0]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(7, 5))

# Plot the line chart (Adult overweight rate, green)
overweight_line, = ax.plot(years, overweight_rates, marker='o', color="#A4C639", label="Adult Overweight Rate (%)", linewidth=2)
# Plot the line chart (Adult obesity rate, blue)
obesity_line, = ax.plot(years, obesity_rates, marker='o', color="#87CEEB", label="Adult Obesity Rate (%)", linewidth=2)

# Add data labels (Adult overweight rate)
for x, y in zip(years, overweight_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Add data labels (Adult obesity rate)
for x, y in zip(years, obesity_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# Set the x - axis ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years)
# Set the y - axis label
ax.set_ylabel("Rate (%)")
# Set the title
ax.set_title("Adult Obesity and Overweight Rates in China from 2000 to 2020", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()