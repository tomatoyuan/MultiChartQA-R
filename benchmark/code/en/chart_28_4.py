import matplotlib.pyplot as plt
import numpy as np

# Data definition
genders = ["Female", "Male"]
gender_percents = [48, 52]
gender_colors = ['#FF7E79', '#7EB0D5']

# Create a canvas
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# Draw a beautified horizontal segmented bar chart
bar_height = 0.4
ax.barh(0, gender_percents[0], color=gender_colors[0], 
         height=bar_height, edgecolor='white', linewidth=1.5, label=genders[0])
ax.barh(0, gender_percents[1], left=gender_percents[0], color=gender_colors[1], 
         height=bar_height, edgecolor='white', linewidth=1.5, label=genders[1])

# Add data labels
ax.text(gender_percents[0]/2, 0, f"{gender_percents[0]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')
ax.text(gender_percents[0] + gender_percents[1]/2, 0, f"{gender_percents[1]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# Set the bar chart style
ax.set_xlim(0, 100)
ax.set_yticks([])  # Remove the y-axis
ax.set_xlabel("Percentage (%)", fontsize=12, labelpad=10)
ax.set_title("Attention percentage of males and females aged 19 - 24 to Double 11", fontsize=14, pad=20, fontweight='bold')

# Customize the x-axis ticks
ax.set_xticks([0, 25, 50, 75, 100])
ax.tick_params(axis='x', which='major', labelsize=10)

# Add a legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), 
           ncol=2, frameon=False, fontsize=12)

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Add a border
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# Add a diagonal line at the boundary - the separation line between males and females
divider_y = np.linspace(-bar_height/2, bar_height/2, 100)
divider_x = np.ones_like(divider_y) * gender_percents[0]
ax.plot(divider_x, divider_y, color='white', linewidth=1.5, linestyle='--')

# Adjust the layout
plt.tight_layout(pad=3)

# Save the chart (optional)
# plt.savefig('gender_distribution.png', dpi=300, bbox_inches='tight')

# Display the chart
plt.show()