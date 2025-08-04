import matplotlib.pyplot as plt
import numpy as np

# Product categories
labels = ["Hard Home Furnishings", "Soft Home Furnishings", "Didn't Purchase & Don't Understand"]
# Corresponding proportions (%)
proportions = [72.34, 67.53, 6.23]

# Radar chart angle settings
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the radar chart
proportions_full = proportions + proportions[:1]
angles_full = angles + angles[:1]

# Create the figure with increased size
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw the radar chart
ax.fill(angles_full, proportions_full, color='orange', alpha=0.25)
ax.plot(angles_full, proportions_full, color='orange', linewidth=2)

# Add data labels with optimized positioning
for i in range(num_vars):
    angle = angles[i]
    value = proportions[i]
    
    # Adjust label position based on angle to avoid overlap
    if angle == 0:
        ha = 'center'
        va = 'bottom'
        offset = 5
    elif angle == np.pi/2:
        ha = 'left'
        va = 'center'
        offset = 5
    elif angle == np.pi:
        ha = 'center'
        va = 'top'
        offset = -5
    elif angle == 3*np.pi/2:
        ha = 'right'
        va = 'center'
        offset = -5
    elif 0 < angle < np.pi/2:
        ha = 'left'
        va = 'bottom'
        offset = 5
    elif np.pi/2 < angle < np.pi:
        ha = 'left'
        va = 'top'
        offset = 5
    elif np.pi < angle < 3*np.pi/2:
        ha = 'right'
        va = 'top'
        offset = -5
    else:
        ha = 'right'
        va = 'bottom'
        offset = -5
    
    # Add the label with calculated position parameters
    ax.text(angle, value + offset, f'{value}%', ha=ha, va=va, fontsize=12)

# Set axis limits and ticks to avoid data overlap
ax.set_ylim(0, 85)
ax.set_yticks(np.arange(0, 85, 15))  # Adjust tick intervals
ax.set_yticklabels([])  # Hide default tick labels

# Set axis labels
ax.set_xticks(angles)
ax.set_xticklabels(labels, fontsize=12)

# Set title
ax.set_title('Types of Home Furnishings Purchased or Known by Chinese Consumers in 2025', fontsize=16, pad=20)

# Add legend and grid lines
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()