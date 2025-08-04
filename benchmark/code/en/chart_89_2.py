import matplotlib.pyplot as plt
import numpy as np

# Consumption scenarios
scenarios = ["Friend Gathering", "Family Gathering", "Business Entertainment", "Drinking Alone", "Couple's Date"]
# Proportion of 18 - 29 years old (%)
age18_29 = [39.2, 21.1, 22.5, 13.2, 3.9]
# Proportion of 30 years old and above (%)
age30_up = [43.7, 28.4, 15.7, 10.1, 2.2]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(7, 6))

# Draw a horizontal bar chart for 18 - 29 years old (green)
y = np.arange(len(scenarios))
bar_width = 0.35
bars1 = ax.barh(y + bar_width/2, age18_29, height=bar_width, color="#A4C639", label="Aged 18 - 29 (%)")
# Draw a horizontal bar chart for 30 years old and above (blue)
bars2 = ax.barh(y - bar_width/2, age30_up, height=bar_width, color="#87CEEB", label="Aged 30 and above (%)")

# Add data labels for 18 - 29 years old
for bar in bars1:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Add data labels for 30 years old and above
for bar in bars2:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Draw yellow dashed boxes for Business Entertainment and Drinking Alone
# Find the indices of Business Entertainment and Drinking Alone
start_idx = scenarios.index("Business Entertainment")
end_idx = scenarios.index("Drinking Alone")
# Calculate the coordinates of the box
y_min = y[start_idx] - bar_width/2 - 0.1
y_max = y[end_idx] + bar_width/2 + 0.1
x_min = 0
x_max = max(max(age18_29), max(age30_up)) + 5  # Extend the x - axis range appropriately

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(scenarios)
# Set x - axis label
ax.set_xlabel("Proportion (%)")
# Set the title
ax.set_title("Liquor Consumption Scenarios (by Age)", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()