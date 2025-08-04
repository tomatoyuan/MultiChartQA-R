import matplotlib.pyplot as plt

# -------------------- Data Definition --------------------
labels = ["Purchased dietary supplements in the past year", "Did not purchase dietary supplements in the past year"]
sizes = [70.6, 29.4]  # Proportion (%)

# Color configuration (similar to the original image color scheme)
colors = ["#a5d6a7", "#dcdcdc"]

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Draw a pie chart --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # Display percentage
    startangle=90,      # Starting angle (place the "Purchased" part on the right)
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

# -------------------- Beautify the chart --------------------
# Set the title
ax.set_title(
    "Proportion of people who purchased dietary supplements in the past year",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the legend position (simulate the layout of the original image)
ax.legend(
    loc="upper left", 
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Optimize the layout
plt.tight_layout()

plt.show()