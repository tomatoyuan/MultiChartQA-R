import matplotlib.pyplot as plt
import numpy as np

# Satisfaction categories
categories = ["Very Satisfied", "Satisfied", "Average", "Dissatisfied"]
# Corresponding percentages (%)
percentages = [14.5, 45.7, 32.7, 7.1]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Draw a red border to circle "Very Satisfied" and "Satisfied"
x1, y1 = bars[0].get_xy()
x2, y2 = bars[1].get_xy() + np.array([bars[1].get_width(), bars[1].get_height()])
rect = plt.Rectangle((x1 - 0.1, y1 - 0.1), x2 - x1 + 0.2, y2 - y1 + 0.2,
                     fill=False, edgecolor='red', linewidth=2, linestyle='--')
ax.add_patch(rect)

# Add explanatory text
ax.text(0.7, 0.9, "Nearly 60% of residents are satisfied with their current health status",
        transform=ax.transAxes, fontsize=12, color='red', ha='center')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set y - axis label
ax.set_ylabel("Percentage of health satisfaction evaluation (%)")
# Set the title
ax.set_title("2022 China Residents' Health Satisfaction", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()