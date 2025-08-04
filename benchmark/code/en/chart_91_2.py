import matplotlib.pyplot as plt
import numpy as np

# Simulated time nodes (simplified, can be refined according to actual situation)
dates = np.arange(2017, 2022, 0.5)  
# Simulated price data (general trend, can be adjusted)
prices = [1.8, 1.6, 1.9, 1.8, 1.7, 1.8, 1.7, 1.8, 1.9, 1.8]  

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 4))

ax.set_ylim(0, 8)

# Draw a line chart
ax.plot(dates, prices, color="#A4C639", label="Stainless Steel: 304/2B Coil 1*1219*C: Wuxi (10,000 yuan/ton)", linewidth=2)

# Simulate labeling key nodes (example, can be supplemented according to actual situation)
key_dates = [2017, 2021]
key_prices = [1.8, 2.2]
for x, y in zip(key_dates, key_prices):
    ax.annotate(f'{y}', xy=(x, y), xytext=(5, 5), textcoords="offset points", ha='center', va='bottom', color="#A4C639")

# Set x - axis ticks (simplified to display years, can be refined)
ax.set_xticks(np.arange(2017, 2022))
ax.set_xticklabels([f"{year}.1" for year in range(2017, 2022)])  # Simulate the time format of the original chart

# Set y - axis label
ax.set_ylabel("Price (10,000 yuan/ton)")
# Set the title
ax.set_title("China's Stainless Steel Price Trend from 2017 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()