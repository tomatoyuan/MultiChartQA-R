import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2010", "2014", "2018", "2020"]
# Number of myopic students in each educational stage (in ten thousand people), 
# the data is consistent with the corresponding levels in the chart and can be adjusted as needed
data = {
    "Primary School Students": [3107.13, 4458.78, 3722.13, 3818.24],
    "Middle School Students": [3061.82, 3262.66, 3331.25, 3493.92],
    "High School Students": [3554.52, 3616.31, 3187.08, 3351.23]
}
# Color settings to match the chart's color scheme
colors = ["#A4C639", "#a8dda8", "#87CEEB"]  

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a stacked bar chart
bottom = np.zeros(len(years))
for i, (category, values) in enumerate(data.items()):
    ax.bar(years, values, bottom=bottom, color=colors[i], label=category)
    # Add data labels
    for x, y in zip(np.arange(len(years)), values):
        ax.text(x, bottom[x] + y / 2, f'{y}', ha='center', va='center', color='black')
    bottom += np.array(values)

# Set the y-axis label
ax.set_ylabel("Number of Myopic Students (in ten thousand people)")
# Set the title
ax.set_title('Total Number of Myopic Primary, Middle, and High School Students in China from 2010 - 2020', fontsize=14, fontweight='bold')

# Add a legend
ax.legend()

# Beautification: Hide the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()