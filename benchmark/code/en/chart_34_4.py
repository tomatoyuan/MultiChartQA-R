import matplotlib.pyplot as plt
import numpy as np

# Data
data = [1, 1, 1, 1, 0.4]  # Simulate the proportion of each interval, the sum corresponds to the average of 2.4 scenarios, can be fine - tuned according to the actual situation
labels = ["1 scenario", "2 scenarios", "3 scenarios", "4 scenarios", "5 scenarios"]
colors = ["#4CAF50", "#FFC107", "#F44336", "#9C27B0", "#607D8B"]  # Simulate similar colors

# Draw a donut chart
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",  # Display percentages
    startangle=90,
    pctdistance=0.85,  # The distance of the percentage label from the center of the circle
    wedgeprops={"width": 0.3, "edgecolor": "white"}  # Set the width and edge color of the ring
)

# Add center text to display the average number of scenarios
ax.text(
    0,
    0,
    "Average\n2.4 scenarios",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold"
)

# Add a color - coded legend on the right
text_descriptions = [
    "Daily Commute",
    "Fashionable Outfit",
    "High - energy Fitness",
    "Mountain Outdoor",
    "Home Relaxation"
]

# Calculate the vertical coordinates for text display to evenly distribute the text
y_positions = np.linspace(0.8, -0.8, len(text_descriptions))
for i, (desc, color) in enumerate(zip(text_descriptions, colors)):
    # Add color markers
    ax.scatter(
        1.2,  # x - position (slightly shifted to the left to make room for the marker)
        y_positions[i],
        s=50,  # Marker size
        color=color,  # Use the corresponding color
        zorder=3  # Ensure the marker is displayed on top
    )
    # Add text descriptions
    ax.text(
        1.35,  # Text starting position (shifted to the right to avoid overlap)
        y_positions[i],
        desc,
        fontsize=12,
        ha="left",
        va="center"
    )

# Add a title
plt.title("User Scenario Usage Distribution", fontsize=16, fontweight="bold", pad=20)

# Adjust the layout to avoid element overlap (slightly expand the right - hand space)
plt.subplots_adjust(right=0.75, top=0.85)

# Display the chart
plt.show()