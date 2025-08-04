import matplotlib.pyplot as plt
import numpy as np

# Data definition
age_groups = ["19 - 24 years old", "25 - 34 years old", "Under 18 years old", "35 - 49 years old", "Over 50 years old"]
age_percentages = [52, 41, 5, 2, 0]
age_colors = ['#4A7ABC', '#5EB95E', '#F37B1D', '#905CA9', '#E5E5E5']

# Create a canvas
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Draw a beautified pie chart
wedges, texts = ax.pie(
    age_percentages,
    labels=None,
    autopct=None,
    startangle=90,
    colors=age_colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    pctdistance=0.8,
)

# Add a shadow effect to the pie chart
for w in wedges:
    w.set_alpha(0.9)
    w.set_zorder(1)

# Set the title
ax.set_title("Attention proportion of different age groups to Double 11", fontsize=16, pad=25,
              fontweight='bold', color='#333333')
ax.axis('equal')  # Ensure the pie chart is circular

# Optimize the label position calculation, using a diagonal + horizontal line style
label_positions = []

for i, (wedge, group, percent) in enumerate(zip(wedges, age_groups, age_percentages)):
    if percent == 0:  # Skip the 0% part
        continue

    # Get the angle of the wedge
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    rad = np.deg2rad(ang)
    y = np.sin(rad)
    x = np.cos(rad)

    # Intelligently adjust the label distance
    angle = wedge.theta2 - wedge.theta1
    base_radius = 1.25
    radius = base_radius + max(0, 0.3 - angle / 180)

    # Calculate the end points of the diagonal line and the horizontal line
    line1_length = 0.25
    line2_length = 0.4

    line1_end_x = x * (1 + line1_length)
    line1_end_y = y * (1 + line1_length)

    if x > 0:  # Right - side labels
        line2_end_x = line1_end_x + line2_length
        line2_end_y = line1_end_y
    else:  # Left - side labels
        line2_end_x = line1_end_x - line2_length
        line2_end_y = line1_end_y

    # Check if there is an overlap with existing labels
    overlap = False
    label_pos = (line2_end_x, line2_end_y)

    for pos in label_positions:
        dist = np.sqrt((label_pos[0] - pos[0]) ** 2 + (label_pos[1] - pos[1]) ** 2)
        if dist < 0.3:
            overlap = True
            if x > 0:  # Move the right - side label up
                line1_end_y += 0.1
                line2_end_y += 0.1
            else:  # Move the left - side label down
                line1_end_y -= 0.1
                line2_end_y -= 0.1
            break

    label_positions.append(label_pos)

    # Draw the two - segment connection line
    ax.plot([x, line1_end_x], [y, line1_end_y], color='#999999', linestyle='-', linewidth=1)
    ax.plot([line1_end_x, line2_end_x], [line1_end_y, line2_end_y], color='#999999', linestyle='-', linewidth=1)

    # Add label text
    if x > 0:
        ax.text(line2_end_x + 0.05, line2_end_y, f"{group}: {percent}%",
                ha='left', va='center', fontsize=11, backgroundcolor='white')
    else:
        ax.text(line2_end_x - 0.05, line2_end_y, f"{group}: {percent}%",
                ha='right', va='center', fontsize=11, backgroundcolor='white')

# Adjust the layout
plt.tight_layout(pad=3)

# Save the chart (optional)
# plt.savefig('age_distribution.png', dpi=300, bbox_inches='tight')

# Display the chart
plt.show()