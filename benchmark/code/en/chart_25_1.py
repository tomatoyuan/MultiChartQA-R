import matplotlib.pyplot as plt
import numpy as np

# Data (example popularity values, can be replaced with real data)
categories = ["New Year's Eve Dinner", "New Year Greetings", "Watching Spring Festival Gala / Lucky Money / Staying Up Late", "Lucky Money", "Setting Off Firecrackers / Worshiping Gods and Praying for Blessings"]
north = [85, 70, 65, 90, 75]  # Popularity values in the north (example data)
south = [95, 60, 70, 80, 55]  # Popularity values in the south (example data)

y = np.arange(len(categories))  # y-axis coordinates
max_value = max(max(north), max(south))  # Get the maximum popularity value for setting the x-axis range

# Create a canvas
fig, ax = plt.subplots(figsize=(12, 6))

# Draw the bar chart for the north (on the left, extending in the negative direction)
ax.barh(y, [-n for n in north], height=0.4, label="North", color="#1E88E5")
# Draw the bar chart for the south (on the right, extending in the positive direction)
ax.barh(y, south, height=0.4, label="South", color="#FF5722")

# Set y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12)

# Set the x-axis range and labels
ax.set_xlim(-max_value - 10, max_value + 10)
ax.set_xticks([-100, -75, -50, -25, 0, 25, 50, 75, 100])
ax.set_xticklabels(['100', '75', '50', '25', '0', '25', '50', '75', '100'])
ax.set_xlabel('Popularity Value', fontsize=12)

# Set the title and legend
ax.set_title('Comparison of Attention Popularity of "Spring Festival Rituals" between North and South', fontsize=16, pad=20)
ax.legend(loc='upper right')

# Add data labels
for i, v in enumerate(north):
    ax.text(-v - 5, i, str(v), va='center', ha='right', color='black')
for i, v in enumerate(south):
    ax.text(v + 5, i, str(v), va='center', ha='left', color='black')

# Hide the top and right borders, adjust the position of the bottom border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('center')

plt.tight_layout()
plt.show()