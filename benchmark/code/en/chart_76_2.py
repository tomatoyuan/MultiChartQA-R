import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# Marketing cost per newly - added active user in the current period (yuan/person), the data can be roughly the same
marketing_cost = [67.6, 100.1, 154.6, 251.6, 435.7, 298.1, 474.8, 572.3]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, marketing_cost, width=bar_width, color="#A4C639", label="Average marketing cost per newly - added active user \nin the current period (yuan/person)")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Simulate a green outer border
for spine in ax.spines.values():
    spine.set_color('#A4C639')
    spine.set_linewidth(2)

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y - axis label
ax.set_ylabel("Average marketing cost per newly - added active user \nin the current period (yuan/person)")
# Set the title
ax.set_title("Marketing cost per newly - added active user of leading Internet listed companies from 2014 to 2021", fontsize=12, fontweight="bold")

# Add a legend
ax.legend(loc='upper left')

plt.tight_layout()  # Automatically adjust the layout
plt.show()