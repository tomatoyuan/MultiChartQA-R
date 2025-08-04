import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e", "2026e"]
# Current zero - sugar beverage market size (in billions of yuan), data consistent with the chart
market_size = [32, 42, 67, 97, 118, 143, 168, 195, 231, 269, 301]
# YOY (%), data consistent with the chart, add 0% for 2016 (no year - on - year data)
yoy = [0, 28.8, 61.3, 43.7, 22.1, 21.4, 17.5, 16.2, 17.9, 16.7, 11.7]

# Create a canvas
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 600)

# Draw a bar chart (market size, green)
ax1.bar(years, market_size, color="#A4C639", label="Current zero - sugar beverage market size (in billions of yuan)")
ax1.set_ylabel("Market size (in billions of yuan)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Create a secondary y - axis to draw a line chart (YOY, blue)
ax2 = ax1.twinx()

ax2.set_ylim(-120, 110)

ax2.plot(years, yoy, marker='o', color="#87CEEB", label="YOY(%)", linewidth=2)
ax2.set_ylabel("YOY(%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Add data labels (market size)
for x, y in zip(np.arange(len(years)), market_size):
    ax1.text(x, y + 5, f'{y}', ha='center', va='bottom', color='black')

# Add data labels (YOY)
for x, y in zip(np.arange(len(years)), yoy):
    ax2.text(x, y + 1, f'{y}%', ha='center', va='bottom', color='black')

# Add CAGR description text
cagr_texts = [
    (0.2, 0.85, "CAGR = 36.1%"),
    (0.7, 0.85, "CAGR = 15.6%")
]
for x, y, text in cagr_texts:
    ax1.text(x, y, text, transform=ax1.transAxes, fontsize=12, ha='center', va='bottom')

# Set the title
ax1.set_title('Market size of sugar - free beverages in China from 2016 to 2026', fontsize=14, fontweight='bold')

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Beautify: Hide the top and right borders
for spine in ['top', 'right']:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()