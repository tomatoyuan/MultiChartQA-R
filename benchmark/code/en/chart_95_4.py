import matplotlib.pyplot as plt
import numpy as np

# Specialty development direction data
skill_labels = ["Just for passion\nNo need to make money", "Hope to be\nmain or side job"]
skill_sizes = [32, 68]
skill_colors = ["#D3D3D3", "#87CEEB"]

# Future living city data
city_labels = ["First-tier cities", "Second-tier cities", "Below third-tier cities", "Not decided yet"]
city_sizes = [36, 42, 16, 6]
city_colors = ["#A4C639", "#A4C639", "#A4C639", "#A4C639"]  # Uniform green color scheme, can be fine - tuned

# Create a canvas (two - column layout)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Draw a pie chart for specialty development direction
ax1.pie(skill_sizes, labels=skill_labels, colors=skill_colors, startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='white'))  # Donut pie chart
ax1.set_title("Specialty Development Direction", fontsize=12, fontweight="bold", y=-0.1)  # Move the title down

# Draw a bar chart for future living cities
x = np.arange(len(city_labels))
bar_width = 0.6
ax2.bar(x, city_sizes, color=city_colors, width=bar_width)

# Add data labels to the city bar chart
for bar in ax2.patches:
    height = bar.get_height()
    ax2.annotate(f'{height}%',
                 xy=(bar.get_x() + bar_width/2, height),
                 xytext=(0, 3),  # Label position: offset 3 points above
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color='black')

# Set the x - axis ticks and labels for the city bar chart
ax2.set_xticks(x)
ax2.set_xticklabels(city_labels, rotation=10)
ax2.set_title("Future Living City", fontsize=12, fontweight="bold", y=-0.2)  # Move the title down

# Beautification: Hide the borders of the pie chart and bar chart
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.5)

plt.show()