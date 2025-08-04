import matplotlib.pyplot as plt

# -------------------- Data Definition --------------------
labels = ["Male", "Female"]
sizes = [63.4, 36.6]  # Proportion (%)
colors = ["#a5d6a7", "#4dd0e1"]  # Color configuration (similar to the original image)

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Draw a Donut Chart --------------------
# Core: Set the donut width via wedgeprops
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  # Display percentage
    startangle=90,      # Starting angle (place the "Male" part on the right)
    colors=colors,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "width": 0.3,    # Donut width (core parameter)
        "edgecolor": "white",
        "linewidth": 2
    }
)

# -------------------- Add Center Text --------------------
# Add "63.4% of e - sports users are male" in the center of the donut
ax.text(
    0, 0, 
    "63.4% of e - sports users are male",
    ha="center", 
    va="center",
    fontsize=14,
    color="#424242",
    fontweight="bold"
)

# -------------------- Beautify the Chart --------------------
# Set the title
ax.set_title(
    "Gender Distribution of Chinese E - sports Users in 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Optimize the layout
plt.tight_layout()

plt.show()