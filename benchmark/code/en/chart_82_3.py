import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2015, 2022)
# Online fitness penetration rate (%), the data can be approximately the same
penetration = [0.0, 0.8, 17.5, 21.7, 33.2, 42.7, 45.5]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the line chart
line, = ax.plot(years, penetration, marker='o', color="#A4C639", label="Online fitness penetration rate in China (%)", linewidth=2)

# Add data annotations
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Set x - axis ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years)
# Set y - axis label
ax.set_ylabel("Penetration rate (%)")
# Set the title
ax.set_title("Online fitness penetration rate in China from 2015 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()