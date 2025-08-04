import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# Data
labels = ['Supplement trace elements', 'Contain dietary fiber', 'Contain probiotics', 'Contain DHA', 'Supplement vitamins']
values = [70, 56, 46, 41, 23]
x = np.arange(len(labels))

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Custom gradient color list (from dark to light)
gradient_colors = [
    ('#00d2c8', '#a2f0ec'),
    ('#00c0d6', '#a3e8f5'),
    ('#00a6de', '#a4dbf7'),
    ('#0091e6', '#a5cef9'),
    ('#0077ed', '#a7c2fb')
]

# Draw each gradient bar
bar_width = 0.6
for i, (val, (color_top, color_bottom)) in enumerate(zip(values, gradient_colors)):
    # Custom gradient bar (simulated by rectangle superposition)
    for j in range(100):  # 100 segments to simulate gradient
        fraction = j / 100
        height = val * (1 / 100)
        y = height * j
        color = LinearSegmentedColormap.from_list("grad", [color_bottom, color_top])(fraction)
        ax.add_patch(Rectangle((x[i] - bar_width / 2, y), bar_width, height, color=color, linewidth=0))

    # Add percentage text on top of the bar
    ax.text(x[i], val + 1.5, f'{val}%', ha='center', fontsize=10)

# Set labels
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylim(0, 80)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_title('Attention of Chinese parents to beneficial ingredients with efficacy', fontsize=14, fontweight='bold', pad=20)

# Legend
ax.legend(['Percentage (%)'], loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# Beautify
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()