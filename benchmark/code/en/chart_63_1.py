import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
categories = ["Moderate Users", "Heavy Users", "Light Users"]
sizes = [53.1, 43.7, 3.2]  # Proportion (percentage)

# Color configuration (similar to the original image)
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# Legend descriptions (consistent with the original image)
legend_labels = [
    "Moderate Users - Use moderately, like to use but not very dependent",
    "Heavy Users - Use most of their leisure time",
    "Light Users - Use occasionally during a small part of their leisure time"
]

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw the pie chart --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,  # Do not set labels first, show them through the legend
    colors=colors,
    autopct='%1.1f%%',  # Show percentages
    startangle=90,      # Start drawing from 90 degrees (place moderate users on the right)
    wedgeprops={
        'edgecolor': 'white', 
        'linewidth': 1,
        # Dashed arc for heavy users: implemented by setting the 'linestyle' in wedgeprops
        'linestyle': 'dashed' if categories[1] == "Heavy Users" else 'solid'
    },  
    textprops={'fontsize': 10, 'color': '#424242', 'fontweight': 'bold'}  # Percentage text settings
)

# -------------------- Draw the dashed arc for heavy users (supplement the style not covered by the pie chart) --------------------
# Get the wedge of heavy users
heavy_user_wedge = wedges[1]
# Draw the dashed arc (from the start angle to the end angle)
theta1, theta2 = heavy_user_wedge.theta1, heavy_user_wedge.theta2
center, r = heavy_user_wedge.center, heavy_user_wedge.r

# -------------------- Beautify the chart --------------------
# Set the legend (adjust the position and style, consistent with the original image)
ax.legend(
    wedges, legend_labels,
    title="User Types",
    loc="center left",
    bbox_to_anchor=(1, 0.5),  # Place the legend in the middle on the right
    fontsize=9,
    title_fontsize=12,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Make the pie chart a perfect circle
ax.axis('equal')  

# Add a title
ax.set_title(
    "Usage of Social and Entertainment Content Platforms by Chinese Beauty Shooting App Users in 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout (prevent the legend and title from overlapping)
plt.subplots_adjust(right=0.7)

plt.show()