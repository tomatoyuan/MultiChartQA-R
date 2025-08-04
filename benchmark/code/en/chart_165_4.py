import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Necessary Demand', 'Self - Pleasure', 'Show Taste/Personality', 'Renewal',
          'Recommendation or \nInfluenced by Others', 'Curiosity - Driven', 'Gift - Giving', 'Impulse Buying']
values = [55, 42, 36, 36, 30, 21, 15, 11]

# Prepare angles and close the loop
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]
values += values[:1]

# Create radar plot
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Draw radar shape
ax.plot(angles, values, color='blue', linewidth=2)
ax.fill(angles, values, color='blue', alpha=0.25)

# Hide default labels
ax.set_xticks([])
ax.set_yticklabels([])

# Annotate with outer labels and connecting lines
label_radius = max(values) + 10
for angle, label, value in zip(angles[:-1], labels, values[:-1]):
    # Calculate coordinates for point and label
    x_end = angle
    y_end = value

    x_label = angle
    y_label = label_radius

    # Draw connecting line from point to outer label
    ax.plot([x_end, x_label], [y_end, y_label], color='gray', linewidth=0.8, linestyle='--')

    # Determine alignment based on angle
    rotation = np.rad2deg(angle)
    if np.pi/2 < angle < 3*np.pi/2:
        ha = 'right'
    else:
        ha = 'left'

    # Text label (multi-line: label + value)
    ax.text(x_label, y_label, f"{label}\n{value}%", ha=ha, va='center', fontsize=10)

# Title and data source
fig.text(0.5, 1.05, 'Consumer Demands in the Appliance Industry', ha='center', fontsize=16, fontweight='bold')
plt.figtext(0.1, 0.01, "Data Source: Magic Mirror Insights", ha="left", fontsize=10)
plt.tight_layout()
plt.show()