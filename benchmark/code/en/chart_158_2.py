import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Age group labels
age_groups = ['Under 20', '21 - 25', '26 - 30', '31 - 34', '35 - 40', '41 - 45', 'Over 45']
generations = ['Post - 00s', 'Post - 95s', 'Post - 90s', 'Post - 85s', 'Pre - 85s']

# Percentage matrix
percent_data = np.array([
    [52, 0, 0, 0, 1],
    [42, 29, 5, 5, 2],
    [2, 70, 60, 24, 5],
    [2, 1, 33, 51, 24],
    [0, 0, 2, 17, 38],
    [1, 0, 0, 0, 22],
    [1, 0, 0, 0, 9],
])

# Calculate the position of the maximum value in each column (for yellow highlighting)
highlight_mask = (percent_data == np.max(percent_data, axis=0))

# Color mapping
cmap = plt.cm.Purples
norm = mcolors.Normalize(vmin=0, vmax=np.max(percent_data))

# Prepare the figure
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, len(generations))
ax.set_ylim(0, len(age_groups))

# Draw cells
for i in range(len(age_groups)):
    for j in range(len(generations)):
        value = percent_data[i, j]
        if value > 0:
            if highlight_mask[i, j]:
                color = '#FFD700'  # Yellow highlighting for maximum values
                text_color = 'black'
            else:
                color = cmap(norm(value))  # Purple heatmap
                text_color = 'white' if value > 30 else 'black'
            ax.add_patch(plt.Rectangle((j, len(age_groups)-1-i), 1, 1, color=color))
            ax.text(j + 0.5, len(age_groups)-1-i + 0.5, f'{value}%',
                    ha='center', va='center', fontsize=11, color=text_color)

# Set axis labels
ax.set_xticks(np.arange(len(generations)) + 0.5)
ax.set_xticklabels(generations, fontsize=12)
ax.set_yticks(np.arange(len(age_groups)) + 0.5)
ax.set_yticklabels(age_groups[::-1], fontsize=12)
ax.invert_yaxis()

# Title and data source
plt.title('Distribution of the first perception of skin aging \n'
          'at different age groups among different generations', fontsize=14, weight='bold', loc='left')
plt.text(0, -1, 'Data source: CBNData questionnaire survey in July 2024\nQ5. At what age did you start to notice signs of skin aging?',
         fontsize=9, color='gray')

# Clean up the style
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)
plt.grid(False)

# Add a color bar (only show the purple mapping)
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap),
                    ax=ax, orientation='vertical', shrink=0.6, pad=0.02)
cbar.set_label('Percentage intensity (non - maximum values)', fontsize=10)

plt.tight_layout()
plt.show()