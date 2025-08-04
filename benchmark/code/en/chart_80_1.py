import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e"]
# Market size (in billions of yuan), the data can be roughly the same
market_size = [352, 481, 549, 555, 499, 486, 530, 555, 628]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#C63982", label="Market Size (in billions of yuan)")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set the y - axis label
ax.set_ylabel("Market Size (in billions of yuan)")
# Set the title
ax.set_title("Market Size and Forecast of Chinese Baby Diapers from 2015 to 2023", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()