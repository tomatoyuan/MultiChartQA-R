import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ["Schedule", "European Cup Event Highlights", "Live Streaming URLs", "Last Game Score", "Championship Odds", "Others"]
percents = [30, 24, 17, 14, 8, 7]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#8BC34A')  # Green background

# Draw a horizontal bar chart (using a yellow gradient)
y_pos = np.arange(len(labels))
colors = plt.cm.YlOrBr(np.linspace(0.6, 1, len(labels)))  # Yellow to orange gradient
bars = ax.barh(y_pos, percents, color=colors, edgecolor='black', height=0.6)

# Add a title and a subtitle
ax.set_title('Before the Quarter - Finals\nSearch Keyword Distribution Table', fontsize=18, fontweight='bold', pad=20)

# Set the y - axis labels (keywords)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12)
ax.tick_params(axis='y', which='both', length=0)  # Hide y - axis tick marks

# Set the x - axis labels (percentages)
ax.set_xlabel('Search Proportion (%)', fontsize=12, labelpad=15)
ax.set_xlim(0, 35)  # Leave space on the right side
ax.set_xticks(np.arange(0, 36, 5))
ax.set_xticklabels([f'{x}%' for x in np.arange(0, 36, 5)], fontsize=10)

# Add numerical labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.8, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=10, fontweight='bold')

# Add "Person Icons" (using native matplotlib shapes instead)
for i, (label, percent) in enumerate(zip(labels, percents)):
    # Draw a simplified "person" (a circular head + a rectangular body)
    head = plt.Circle((-2.5, y_pos[i]), 0.3, color='yellow', ec='black')
    body = plt.Rectangle((-2.8, y_pos[i]-0.3), 0.6, 0.6, color='yellow', ec='black')
    ax.add_patch(head)
    ax.add_patch(body)

    # Add a "Heart" mark (using a triangle instead)
    heart_x = [-2.6, -2.4, -2.5]
    heart_y = [y_pos[i]+0.15, y_pos[i]+0.15, y_pos[i]+0.3]
    ax.fill(heart_x, heart_y, color='red')

# Add "Magnifying Glass" marks (using native matplotlib shapes)
for i, p in enumerate(percents):
    num_magnifiers = p // 5
    for j in range(num_magnifiers):
        # Draw a simplified magnifying glass
        magnifier_x = [-5 - j*0.8, -4.5 - j*0.8, -4.7 - j*0.8, -5 - j*0.8]
        magnifier_y = [y_pos[i]+0.1, y_pos[i]+0.1, y_pos[i]-0.1, y_pos[i]-0.1]
        ax.fill(magnifier_x, magnifier_y, color='black')
        # Magnifying glass handle
        ax.plot([-4.5 - j*0.8, -4.3 - j*0.8], [y_pos[i], y_pos[i]-0.2], 'k-', linewidth=1.5)

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

# Adjust the layout
plt.tight_layout(pad=3)
plt.show()