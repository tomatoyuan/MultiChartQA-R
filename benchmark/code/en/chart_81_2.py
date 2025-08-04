import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2018", "2019", "2020"]
# General warehouse area (in hundreds of millions of square meters), the data can be roughly the same
general_warehouse = [10.60, 10.80, 11.45]
# High - standard warehouse area (in hundreds of millions of square meters), the data can be roughly the same
high_standard_warehouse = [3.00, 3.15, 3.45]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(6, 5))

# Draw a grouped bar chart
x = np.arange(len(years))
bar_width = 0.35
# General warehouse (green)
general_bars = ax.bar(x - bar_width/2, general_warehouse, width=bar_width, color="#C63982", label="General Warehouse (Hundreds of Millions of Square Meters)")
# High - standard warehouse (blue)
high_standard_bars = ax.bar(x + bar_width/2, high_standard_warehouse, width=bar_width, color="#64B5F6", label="High - Standard Warehouse (Hundreds of Millions of Square Meters)")

# Add data labels for general warehouses
for bar in general_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels for high - standard warehouses
for bar in high_standard_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y - axis label
ax.set_ylabel("Area (Hundreds of Millions of Square Meters)")
# Set the title
ax.set_title("Area of General and High - Standard Warehouses in China from 2018 to 2020", fontsize=14, fontweight="bold")

# Add a legend
ax.legend(loc='lower center')

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()