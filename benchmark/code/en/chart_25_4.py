import matplotlib.pyplot as plt
import numpy as np

# Data and labels
labels = ["Mobile Phone", "Online Games", "Red Envelope Snatching", "Reluctant to Go Home", "Others"]
values = [0.6, 0.4, 0.3, 0.2, 0.1]  # Simulated proportion, can be adjusted according to actual situation
colors = ["#F5A623"] * len(labels)  # Thermometer main color

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#D52B1E")  # Red background

# Draw a horizontal bar chart (simulating a thermometer)
y_pos = np.arange(len(labels))
bars = ax.barh(
    y_pos,
    values,
    color=colors,
    edgecolor="white",
    height=0.6,
    left=0.2  # Reserve blank space to simulate the "glass tube" of the thermometer
)

# Simulate the white scale lines of the thermometer (overlay blank bars)
ax.barh(
    y_pos,
    [1 - v for v in values],
    color="white",
    edgecolor="white",
    height=0.6,
    left=0.2 + np.array(values)
)

# Add numerical labels
for i, (value, label) in enumerate(zip(values, labels)):
    # Calculate the label position (middle of the bar chart)
    x_pos = 0.2 + value / 2
    ax.text(
        x_pos, i,
        f"{value:.1f}",
        ha='center', va='center',
        color='white', fontsize=12,
        fontweight='bold'
    )

# Beautification settings
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12, color="gold")  # Golden text
ax.set_xticks([])  # Hide x-axis ticks
ax.spines[:].set_visible(False)  # Hide the border

# Add a title and a slogan
ax.text(
    0.5, 1.1,
    'Mobile Phones Are the Biggest Culprits in "Killing" the Spring Festival Ritual Sense',
    ha='center', va='top',
    fontsize=14, color='gold',
    transform=ax.transAxes
)
ax.text(
    0.5, -0.15,
    'Put down your phone and spend time with your family.',
    ha='center', va='bottom',
    fontsize=12, color='white',
    transform=ax.transAxes
)

plt.tight_layout()
plt.show()