import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e"]
# Simulated sales percentage data (close to the original graph)
percentages = [5.4, 7.5, 12.7, 14.7, 20.6, 23.4, 27.3]
# Free color matching (can be adjusted, using green + blue in the example)
bar_color = "#87CEEB"  # Can be replaced with other colors such as "#FF8C00"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color=bar_color)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar_width/2, height),
                xytext=(0, 3),  # Label position: offset 3 above
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y-axis ticks (0 - 30%)
ax.set_ylim(0, 30)
# Set the title
ax.set_title("Sales Proportion and Forecast of Two - wheeled Lithium - battery Bicycles in China from 2016 to 2022", fontsize=14, fontweight="bold")

# Beautify: hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()