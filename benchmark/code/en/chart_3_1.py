import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Digital transformation of marketing is very important", 
          "In the digital age, operations and data are equally important", 
          "In the digital age, the brand is still very important", 
          "In the digital age, building a marketing platform is very important"]
very_agree = np.array([64, 68, 78, 53])  # Percentage of strongly agree
agree = np.array([33, 29, 19, 40])  # Percentage of agree
disagree = np.array([2, 2, 2, 5])  # Percentage of disagree
strong_disagree = np.array([1, 1, 1, 2])  # Percentage of strongly disagree

# Color scheme (using a more modern color palette)
colors = ['#E63946', '#F1FAEE', '#A8DADC', '#1D3557']  # Gradient from red to dark blue

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size

# Draw a horizontal stacked bar chart
bottom = np.zeros(len(labels))
for i, (data, label, color) in enumerate(zip(
    [strong_disagree, disagree, agree, very_agree],
    ['Strongly Disagree', 'Disagree', 'Agree', 'Strongly Agree'],
    colors
)):
    bars = ax.barh(labels, data, left=bottom, color=color, label=label, 
                  alpha=0.9, edgecolor='w', linewidth=0.5)
    
    # Label the percentage on each bar
    for bar, value in zip(bars, data):
        if value > 2:  # Only display text on bars that are wide enough
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_y() + bar.get_height()/2,
                f"{value}%", 
                ha='center', 
                va='center',
                color='black' if i < 2 else 'white',  # Adjust the text color according to the background color
                fontweight='bold',
                fontsize=10
            )
    
    bottom += data

# Set the title
ax.set_title('Survey Results of Advertisers\' Digital Marketing Views in 2021', fontsize=16, fontweight='bold', pad=20)

# Set the labels
ax.set_xlabel('Percentage (%)', fontsize=12, labelpad=10)
# ax.set_ylabel('Opinions', fontsize=12, labelpad=10)  # Remove the y-axis label

# Set the grid lines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set the x-axis range
ax.set_xlim(0, 100)

# Beautify the legend - Place it below the title
fig.legend(loc='upper center', bbox_to_anchor=(0.6, 0.95), ncol=4, frameon=False, fontsize=10)

# Adjust the borders
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust the layout to make space for the legend
plt.subplots_adjust(top=0.85)  # Reduce the top margin
plt.tight_layout()

# Show the chart
plt.show()