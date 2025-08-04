import matplotlib.pyplot as plt

# -------------------- Data Definition --------------------
labels = ["High school or below", "Undergraduate or above", "Junior college"]
sizes = [60.2, 27.1, 12.7]  # Proportion (%)
tgis = [76, 218, 156]       # TGI value

# Color configuration (similar to the original image color scheme)
colors = ["#a5d6a7", "#81d4fa", "#c8e6c9"]

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 6))  # Increase figure width for better layout

# -------------------- Draw a Pie Chart --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=None,  # Remove labels from pie chart (will add to legend instead)
    autopct="%1.1f%%",  # Display percentage
    startangle=90,      # Starting angle (place "High school or below" on the right)
    colors=colors,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "linewidth": 2, 
        "edgecolor": "white"
    }
)

# -------------------- Beautify the Chart --------------------
# Set the title
ax.set_title(
    "Protein powder overall: Educational background",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the legend position to the left and outside the chart
ax.legend(
    labels,  # Add labels to legend
    loc="center left",  # Position legend on the left
    bbox_to_anchor=(-0.35, 0.5),  # Adjust position (move further left)
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white",
    framealpha=1.0,  # Make legend background opaque
    handlelength=1.5,  # Adjust legend handle length
    handleheight=1.5   # Adjust legend handle height
)

# Optimize the layout
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Adjust layout to make room for legend

plt.show()