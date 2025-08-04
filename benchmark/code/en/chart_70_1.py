import matplotlib.pyplot as plt
import numpy as np

# Technical directions
tech_directions = ["Artificial Intelligence", "Big Data", "Testing", "Operation/Technical Support", "Backend Development", "Frontend Development", "Mobile Development"]
# Corresponding percentage data
data = np.array([87.7, 44.2, 38.5, 38.0, 35.1, 22.2, 21.1])

# Bubble size (simulate the perceived area with the square of the data)
sizes = data ** 2.2  # Adjust the exponent to optimize visual perception
colors = plt.cm.plasma(data / max(data))  # Use the plasma color map to enhance the design sense

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Axis settings
x = np.arange(len(tech_directions))

# Draw a bubble chart
scatter = ax.scatter(x, [1]*len(x), s=sizes, c=colors, alpha=0.8, edgecolors='white', linewidths=1.5)

# Add numerical annotations
for i in range(len(tech_directions)):
    ax.text(x[i], 1.02, f"{data[i]}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Set the x-axis labels as technical directions
ax.set_xticks(x)
ax.set_xticklabels(tech_directions, rotation=15, ha="right", fontsize=11)
ax.set_yticks([])

# Add a title
ax.set_title("Year-on-year change in recruitment demand for major Internet technical directions in Spring 2022", fontsize=14, fontweight="bold", pad=20)

# Remove the border
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()