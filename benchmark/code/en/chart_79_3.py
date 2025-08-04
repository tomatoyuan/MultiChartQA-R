import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Fish maw", "Blueberry", "Bilberry", "Blueberry fruit", "Wild berry"]
# Antioxidant capacity (VE content mg/100g), the data can be approximately the same
antioxidant = [1.52, 0.91, 0.45, 0.33, 0.27]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(6, 5))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, antioxidant, width=bar_width, color="#399CC6", label="Antioxidant capacity (VE content mg/100g)")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set the y - axis label
ax.set_ylabel("Antioxidant capacity (VE content mg/100g)")
# Set the title
ax.set_title("Antioxidant capacity of fish maw", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()