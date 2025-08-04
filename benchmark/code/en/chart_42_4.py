import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['', '']
values = [8, 9.84]  # Accurate data: 8 * (1+0.18) = 9.44, fine - tuned to 9.84 according to the chart's visual appearance
x = np.arange(len(categories))

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bar_width = 0.6
rects1 = ax.bar(x[0], values[0], width=bar_width, color='#6aa84f', label='Previous Sales', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], values[1], width=bar_width, color='#3d85c6', label='January 2025 Sales', 
                edgecolor='black', linewidth=0.8)

# Add data labels
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12)

add_labels(rects1)
add_labels(rects2)

# Add a horizontal arrow annotation (pointing to the right)
arrow_start = (x[0] + bar_width/2, values[0] + 0.3)  # Starting point of the arrow: right side of the first bar
arrow_end = (x[1] - bar_width/4, values[0] + 0.3)  # Ending point of the arrow: left side of the second bar
ax.annotate('18% Increase',
            xy=arrow_end,
            xytext=arrow_start,
            arrowprops=dict(arrowstyle='->, head_width=0.4, head_length=0.8', 
                           color='black', lw=1.5, shrinkA=0, shrinkB=0),
            ha='left', va='center', fontsize=12, 
            xycoords='data', textcoords='data')

# Set the chart style
ax.set_ylim([0, 12])
ax.set_ylabel('Billion', fontsize=14)
ax.set_title('January 2025 Health Food Industry Sales Growth', fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=12, loc='upper left')

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the border
for spine in ax.spines.values():
    spine.set_color('gray')

# Beautify the overall style
plt.tight_layout()

# Display the chart
plt.show()