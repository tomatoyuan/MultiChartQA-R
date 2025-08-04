import matplotlib.pyplot as plt

# Data definition
labels = [
    "Wear almost all day",
    "Wear only when looking at distant objects",
    "Wear only when using eyes for a long time",
    "No fixed pattern, wear when feeling the need"
]
sizes = [54.1, 15.5, 11.6, 18.9]
colors = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082"]

# Create a wider canvas
fig, ax = plt.subplots(figsize=(12, 6))  # Expand horizontally

# Adjust the position of the pie chart: Move the center point to the left
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    textprops={
        "fontsize": 10,
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    },
    center=(-0.8, 0)  # Control the pie chart center to move to the left
)

# Set the title
ax.set_title(
    "Habit of wearing frame glasses among myopic people",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()
plt.show()