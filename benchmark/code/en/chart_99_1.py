import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2015", "2016", "2017", "2018", "2019", "2020"]
# Simulated consumption data (kg, following the trend of the original graph)
consumptions = [40.5, 43.9, 45.6, 47.4, 51.4, 51.3]
# Free color matching (can be adjusted, using orange in the example)
line_color = "#FF8C00"  # Can be replaced with other colors such as "#32CD32"

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a line chart
x = np.arange(len(years))
line, = ax.plot(x, consumptions, marker='o', color=line_color, label="Weight (kg)")

# Add data labels
for i, val in enumerate(consumptions):
    ax.annotate(f'{val}',
                xy=(x[i], val),
                xytext=(5, 5),  # Label position: offset 5 points to the right and down
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y-axis ticks (35 - 55 kg, suitable for the data)
ax.set_ylim(35, 55)
# Set the title
ax.set_title("Per capita fresh fruit consumption of national residents from 2015 to 2020", fontsize=14, fontweight="bold")
# Add a legend
ax.legend()

# Beautification: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()