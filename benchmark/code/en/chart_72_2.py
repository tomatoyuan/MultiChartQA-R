import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# Retail prices of domestic infant milk powder (yuan/jin), the data can be approximately the same
domestic_prices = [166.3, 171.9, 179.8, 189.5, 204.3, 211.6]
# Retail prices of international infant milk powder (yuan/jin), the data can be approximately the same
international_prices = [214.3, 220.7, 228.0, 235.5, 250.5, 257.8]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the line chart of domestic brand prices
domestic_line, = ax.plot(years, domestic_prices, marker='o', color="#A4C639", label="Domestic infant milk powder (yuan/jin)", linewidth=2)
# Plot the line chart of international brand prices
international_line, = ax.plot(years, international_prices, marker='o', color="#64B5F6", label="International infant milk powder (yuan/jin)", linewidth=2)

# Add data labels for domestic brands
for x, y in zip(years, domestic_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Add data labels for international brands
for x, y in zip(years, international_prices):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# Set the y - axis label
ax.set_ylabel("Retail price (yuan/jin)")
# Set the title
ax.set_title("Trend of retail prices of infant milk powder in China from 2016 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()