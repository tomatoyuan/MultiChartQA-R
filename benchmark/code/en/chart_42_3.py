import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Before', '2024']
values = [100, 117]
x = np.arange(len(categories))

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bar_width = 0.6
rects1 = ax.bar(x[0], values[0], width=bar_width, color='#6aa84f', label='Previous Sales Revenue', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], values[1], width=bar_width, color='#3d85c6', label='2024 Sales Revenue', 
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

# Add a horizontal growth arrow annotation
ax.annotate('17% Growth', 
            xy=(0.8, 105),  # Arrow starting point
            xytext=(0.2, 105),  # Arrow ending point
            arrowprops=dict(facecolor='black', shrink=0.02, width=1.5, headwidth=8, connectionstyle="arc3"),
            ha='center', va='center', fontsize=12)

# Set chart style
ax.set_ylim([0, 140])
ax.set_ylabel('Sales Revenue (Billion)', fontsize=14)
ax.set_title('Growth of Health Food Industry Sales Revenue in 2024', fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=12, loc='upper left')

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the border
for spine in ax.spines.values():
    spine.set_color('gray')

# Beautify the overall style
plt.tight_layout()

# Display the chart
plt.show()