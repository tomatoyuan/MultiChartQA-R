import matplotlib.pyplot as plt
import numpy as np

# Countries/Regions
countries = ["Japan", "USA", "China"]
# Per capita logistics real estate area (square meters per person), the data can be roughly the same
area = [4.0, 3.7, 0.7]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a bar chart
x = np.arange(len(countries))
bar_width = 0.6
bars = ax.bar(x, area, width=bar_width, color="#C63982", label="Per capita logistics real estate area (m²/person)")

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
ax.set_xticklabels(countries)
# Hide the y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("Comparison of per capita modern logistics real estate area in China, USA and Japan in 2019", fontsize=14, fontweight="bold")

# Add a legend
ax.legend(loc='center right')

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()