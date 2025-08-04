import matplotlib.pyplot as plt
import numpy as np

# MPV space pain point data
space_pain = {
    "Insufficient trunk space when using the third row": 30.0,
    "Inconvenient access to the third row": 28.3,
    "Weak flexibility and low utilization rate of space use": 25.0,
    "Small space in the third row": 23.8,
    "Unreasonable/storage space with a small quantity": 22.9,
    "Insufficient trunk space after the third row is folded down": 20.8,
    "Small space in the front row": 16.3,
    "Small space in the second row": 11.7
}
# MPV driving comfort pain point data
comfort_pain = {
    "The third - row seats cannot open windows": 29.9,
    "Poor sound effect": 27.7,
    "Poor shock absorption effect": 26.4,
    "Poor heat insulation performance": 25.5,
    "Poor air - conditioning effect": 22.1,
    "High in - car noise": 21.6,
    "Inconvenient getting on and off the vehicle": 18.6,
    "Poor seat comfort": 18.2
}

# Extract labels and values
space_labels = list(space_pain.keys())
space_values = list(space_pain.values())
comfort_labels = list(comfort_pain.keys())
comfort_values = list(comfort_pain.values())

# Color scheme (freely match and can be adjusted)
bar_colors = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4", 
              "#90EE90", "#B0C4DE", "#FFA07A", "#D8BFD8"]

# Create a two - column layout canvas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=False)

# Draw the horizontal bar chart for space pain points
x1 = np.arange(len(space_labels))
ax1.barh(x1, space_values, color=bar_colors, height=0.6)
ax1.set_yticks(x1)
ax1.set_yticklabels(space_labels, fontsize=9)
ax1.set_title("MPV [Space] Pain Points\n(N = 240)", fontsize=12, fontweight="bold")
# Add annotations for space pain points
for i, val in enumerate(space_values):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# Draw the horizontal bar chart for driving comfort pain points
x2 = np.arange(len(comfort_labels))
ax2.barh(x2, comfort_values, color=bar_colors, height=0.6)
ax2.set_yticks(x2)
ax2.set_yticklabels(comfort_labels, fontsize=9)
ax2.set_title("MPV [Driving Comfort] Pain Points\n(N = 231)", fontsize=12, fontweight="bold")
# Add annotations for driving comfort pain points
for i, val in enumerate(comfort_values):
    ax2.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# Beautification: Hide the top and right borders
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.3)  # Add auxiliary grid

plt.tight_layout()
plt.show()