import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2015, 2024)
# Market penetration rate (%), the data can be approximately the same
penetration = [51.6, 55.6, 59.6, 63.9, 72.2, 77.1, 82.0, 85.2, 88.6]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a line chart
line, = ax.plot(years, penetration, marker='o', color="#C63982", label="Penetration Rate (%)", linewidth=2)

# Add data annotations
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C63982")

# Set x - axis ticks and labels
ax.set_xticks(years)
ax.set_xticklabels([f"{year}" for year in years])
# Set y - axis label
ax.set_ylabel("Penetration Rate (%)")
# Set the title
ax.set_title("China Baby Diaper Market Penetration Rate and Forecast from 2015 to 2023", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()