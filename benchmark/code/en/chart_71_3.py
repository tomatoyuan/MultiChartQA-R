import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Per capita sports consumption expenditure of residents", "Per capita sports consumption expenditure of adults", "Per capita sports consumption expenditure of the elderly"]
# Data in 2014 (Yuan), the data can be approximately the same
data_2014 = [926.0, 968.4, 504.0]
# Data in 2020 (Yuan), the data can be approximately the same
data_2020 = [1330.4, 1758.2, 1092.2]

# Bar width
bar_width = 0.35
# Color settings, similar to the green and blue in the original figure
colors = ["#A4C639", "#64B5F6"]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the bar chart for 2014 data
x = np.arange(len(categories))
bar_2014 = ax.bar(x - bar_width/2, data_2014, width=bar_width, color=colors[0], label="2014 (Yuan)")
# Draw the bar chart for 2020 data
bar_2020 = ax.bar(x + bar_width/2, data_2020, width=bar_width, color=colors[1], label="2020 (Yuan)")

# Add data labels for 2014
for bar in bar_2014:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels for 2020
for bar in bar_2020:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=25)
# Set y - axis label
ax.set_ylabel("Consumption expenditure (Yuan)")
# Set the title
ax.set_title("Per capita sports consumption expenditure in China in 2014 & 2020", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()