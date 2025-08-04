import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axis object
fig, ax = plt.subplots(figsize=(10, 10))
# Set the aspect ratio of the axis to be equal
ax.set_aspect('equal')
# Turn off the axis
ax.axis('off')

# ✅ Reduce the size of the main circle
# Create the outer main circle
center_circle = plt.Circle((0, 0), 0.6, color='white', ec='black', lw=2.5, zorder=3)
# Create the inner main circle
center_circle_inner = plt.Circle((0, 0), 0.45, color='white', ec='black', lw=2.5, zorder=4)
# Add the outer main circle to the axis
ax.add_artist(center_circle)
# Add the inner main circle to the axis
ax.add_artist(center_circle_inner)
# Add text to the center of the main circle
ax.text(0, 0.06, '1.11 billion', ha='center', va='center', fontsize=17, fontweight='bold')
# Add text below the center text
ax.text(0, -0.22, 'National Internet Users (2024)', ha='center', fontsize=12)

# Parameters for the sub - circles (finely adjusted)
positions = [(-1.4, 1.0), (1.4, -1.0), (-1.4, -1.0)]
colors = ['#76C7C0', '#58A4B0', '#4C8C9D']
labels = ['Short - video Users', 'Live - streaming Users', 'Online Shopping Users']
users = ['1.04 billion', '0.83 billion', '0.97 billion']
rates = ['CAGR¹ = 4.5%', 'CAGR¹ = 7.8%', 'CAGR¹ = 5.6%']
percents = ['× 93.8%', '× 75.2%', '× 87.9%']

r_outer = 0.22
r_inner = 0.18

for i in range(3):
    x, y = positions[i]
    color = colors[i]

    # Draw the sub - circles
    outer = plt.Circle((x, y), r_outer, color='white', ec=color, lw=2.5, zorder=3)
    inner = plt.Circle((x, y), r_inner, color='white', ec=color, lw=2.5, zorder=4)
    ax.add_artist(outer)
    ax.add_artist(inner)

    # Draw the connecting line and add the proportion
    ax.plot([0, x], [0, y], color='gray', lw=1, zorder=1)
    ax.text(x * 0.5, y * 0.5, percents[i], ha='center', va='center', fontsize=12, color=color)

    # Add descriptions for the sub - circles
    ax.text(x, y - 0.28, users[i], ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(x, y - 0.42, labels[i], ha='center', va='top', fontsize=12, color=color)
    ax.text(x, y - 0.56, rates[i], ha='center', va='top', fontsize=10)

# ✅ Move the title down, closer to the center of the figure
ax.text(0, 1.6, 'Analysis of the Growth Space of Live - streaming E - commerce Users', ha='center', fontsize=18, fontweight='bold')
ax.text(0, -2.2, '¹ CAGR: Compound Annual Growth Rate', ha='center', fontsize=10, color='gray')

# Automatically adjust the layout
plt.tight_layout()
# Display the plot
plt.show()