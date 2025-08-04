import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2007", "2009", "2011", "2013", "2015", "2017", "2019"]
# Proportions of various destinations (simulated data, trying to approximate the trend in the original graph)
employment = [54, 46, 56, 55, 59, 58, 51]    # Employment
further_study = [20, 25, 19, 19, 27, 29, 33] # Further study or intended further study
waiting = [26, 30, 25, 26, 15, 13, 16]       # Waiting for employment and others

# Color configuration (trying to approximate the original graph)
colors = ["#A4C639", "#8EBF8F", "#87CEEB"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a stacked bar chart
bottom = np.zeros(len(years))
for i, (label, data, color) in enumerate(zip(["Employment", "Further study or intended further study", "Waiting for employment and others"], 
                                            [employment, further_study, waiting], 
                                            colors)):
    ax.bar(years, data, bottom=bottom, color=color, label=label)
    bottom += data

    # Add data labels
    for x, y in zip(years, data):
        ax.annotate(f'{y}%',
                    xy=(x, bottom[i] - y/2),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Set the y-axis scale (0 - 100%)
ax.set_ylim(0, 100)
# Set the title
ax.set_title("Graduation destinations of Chinese college students from 2007 to 2019", fontsize=14, fontweight="bold")

# Add a legend
ax.legend(loc='lower right')

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()