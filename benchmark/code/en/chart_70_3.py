import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022.7"]
# Total number of financings (times)
total_financing = [10, 11, 12, 12, 14, 6, 9]
# Number of financings over 100 million yuan (times)
billion_financing = [2, 3, 2, 3, 3, 3, 2]

# Bar width
bar_width = 0.35
# Color settings, similar to the green and blue in the original figure
colors = ["#49C639", "#F664D9"]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the bar chart for the total number of financings
x = np.arange(len(years))
total_bars = ax.bar(x - bar_width/2, total_financing, width=bar_width, color=colors[0], label="Total number of financings (times)")
# Draw the bar chart for the number of financings over 100 million yuan
billion_bars = ax.bar(x + bar_width/2, billion_financing, width=bar_width, color=colors[1], label="Number of financings over 100 million yuan (times)")

# Add data labels for the total number of financings
for bar in total_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels for the number of financings over 100 million yuan
for bar in billion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set the y - axis label
ax.set_ylabel("Number of financings (times)")
# Set the title
ax.set_title("Number of low - code financing events in China from 2016 to July 2022", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()