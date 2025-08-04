import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
labels = ["Very Satisfied", "Fairly Satisfied", "Average", "Somewhat Dissatisfied", "Completely Dissatisfied"]
sizes = [7.8, 37.4, 46.9, 4.6, 3.4]  # Proportion (%)
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082", "#ff8a80"]  # Color configuration (similar to the original image)

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Draw Pie Chart --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # Display percentage
    startangle=140,     # Starting angle (adjust sector position)
    colors=colors,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# -------------------- Add Annotation (Only 45.2% of consumers are satisfied) --------------------
# Calculate the proportion of satisfied consumers (Very Satisfied + Fairly Satisfied)
satisfied_percent = sizes[0] + sizes[1]
ax.annotate(
    f"Only {satisfied_percent:.1f}% of consumers are satisfied with the product",
    xy=(1.1, 0.8),  # Annotation position (upper right)
    xytext=(1.3, 0.9), 
    arrowprops=dict(
        facecolor="pink", 
        edgecolor="pink", 
        arrowstyle="->", 
        linewidth=1
    ),
    fontsize=12,
    color="#424242",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", fc="pink", ec="pink", alpha=0.5)
)

# -------------------- Beautify the Chart --------------------
# Set the title
ax.set_title(
    "Satisfaction level of live - streaming e - commerce consumers with products",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the legend position to the right outside the chart
ax.legend(
    loc="center left",  # Position legend on the right
    bbox_to_anchor=(1, 0.5),  # Move legend outside the chart
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Optimize the layout
plt.tight_layout()

plt.show()