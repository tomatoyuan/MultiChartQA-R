import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2007, 2009, 2011, 2013, 2015, 2017, 2019]
# Average starting salaries of different educational backgrounds (yuan/month, simulated data, close to the trend)
specialty = [1410, 1510, 1856, 2285, 2734, 3185, 3548]
bachelor = [1788, 2276, 2743, 3278, 3961, 4825, 5417]
master = [3469, 3637, 4003, 5461, 6334, 8556, 8778]
doctor = [3252, 3757, 5118, 8800, 6746, 10774, 13849]

# Color configuration (close to the original figure)
colors = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4"]
labels = ["Associate degree holders (yuan/month)", "Bachelor's degree holders (yuan/month)", "Master's degree holders (yuan/month)", "Doctoral degree holders (yuan/month)"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a line chart and annotate the data
for i, (data, color, label) in enumerate(zip([specialty, bachelor, master, doctor], colors, labels)):
    ax.plot(years, data, marker='o', color=color, label=label, linewidth=2)
    # Add data annotations
    for x, y in zip(years, data):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(5, 5),  # Annotation position offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color=color)

# Set x-axis ticks
ax.set_xticks(years)
# Set the title
ax.set_title("Average starting salaries of college graduates with different educational levels from 2007 to 2019", fontsize=14, fontweight="bold")

# Add a legend
ax.legend(loc='upper left')

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()