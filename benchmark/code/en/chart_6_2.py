import matplotlib.pyplot as plt

# Data
sizes = [11.26, 88.74]

# Colors, closer to the original image
computer_colors = ["#1976d2", "#e3f2fd"]  # Computer colors: Dark blue and light blue
mobile_colors = ["#f57c00", "#ffebee"]    # Mobile colors: Orange and light orange

# Create a canvas and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(top=0.85, bottom=0.15)  # Adjust top and bottom margins

# Draw the computer - side retrieval proportion chart (adjust label color)
wedges1, texts1, autotexts1 = ax1.pie(
    [sizes[0], 100 - sizes[0]],
    labels=["Computer", ""],  # Simplify labels
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=computer_colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw the mobile - side retrieval proportion chart (adjust label color)
wedges2, texts2, autotexts2 = ax2.pie(
    [sizes[1], 100 - sizes[1]],
    labels=["Mobile", ""],  # Simplify labels
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=mobile_colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Set label colors (consistent with the corresponding pie chart colors)
for text in texts1:
    text.set_color(computer_colors[0])  # Computer label color is dark blue
for text in texts2:
    text.set_color(mobile_colors[0])    # Mobile label color is dark orange

# Set the percentage text color to black
for text in autotexts1 + autotexts2:
    text.set_color('black')
    text.set_fontsize(14)

# Remove the axes to make the chart a perfect circle
ax1.axis('equal')
ax2.axis('equal')

# Set sub - titles (below the chart)
ax1.text(0.5, -0.1, "Computer - side Retrieval Proportion", 
         ha='center', va='center', transform=ax1.transAxes, fontsize=14)
ax2.text(0.5, -0.1, "Mobile - side Retrieval Proportion", 
         ha='center', va='center', transform=ax2.transAxes, fontsize=14)

# Set the main title
fig.suptitle("May Legal Service Industry Retrieval Device Distribution", fontsize=16, fontweight='bold')

plt.tight_layout()  # Adjust the layout to avoid overlap
plt.show()