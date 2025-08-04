import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021"]
# Battery cost data (yuan), [Lithium-ion battery cost, Lead-acid battery cost]
battery_costs = np.array([[1800, 400], [1400, 400], [1300, 400], [1150, 400], [1050, 400]])

# Custom colors (adjustable), corresponding to lithium-ion battery and lead-acid battery respectively
colors = ["#6839C6", "#87CEEB"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a grouped bar chart, x-axis positions
x = np.arange(len(years))
# Bar width
width = 0.35

# Draw the bar chart for lithium-ion battery costs
li_ion_bars = ax.bar(x - width/2, battery_costs[:, 0], width, color=colors[0], label="Lithium-ion Battery (Yuan)")
# Draw the bar chart for lead-acid battery costs
lead_acid_bars = ax.bar(x + width/2, battery_costs[:, 1], width, color=colors[1], label="Lead-acid Battery (Yuan)")

# Add cost labels for lithium-ion batteries
for bar in li_ion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Add cost labels for lead-acid batteries
for bar in lead_acid_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set the title
ax.set_title("Battery Costs of Chinese Two-wheeled Electric Vehicles from 2017 to 2021", fontsize=14, fontweight="bold")
# Add a legend
ax.legend()

# Beautification: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()