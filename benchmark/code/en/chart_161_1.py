import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data
categories = {
    'Skin Care': {
        'labels': ['Facial Care', 'Skin Care Sets', 'Masks', 'Cleansers', 'Toners', 'Eye Care', 'Sun Protection', 'Other Skin Care', 'Lip Care'],
        'values': [38, 23, 12, 9, 5, 5, 5, 1, 1],
        'color': 'Reds'
    },
    'Makeup': {
        'labels': ['Facial Makeup', 'Lip Makeup', 'Eye Makeup', 'Makeup Tools', 'Makeup Sets', 'Nail Art'],
        'values': [47, 24, 12, 10, 6, 1],
        'color': 'Blues'
    },
    'Perfume': {
        'labels': ['Perfume'],
        'values': [100],
        'color': 'Greens'
    }
}

# Initialize the figure
fig, ax = plt.subplots(figsize=(16, 10))
y_base = 0
bar_height = 0.6
group_gap = 1.2
label_padding = 0.5

# Main plotting loop
for group_index, (group, content) in enumerate(categories.items()):
    labels = content['labels']
    values = content['values']
    cmap = plt.get_cmap(content['color'])
    num_items = len(values)

    # Color gradient
    colors = [cmap(0.3 + 0.6 * i / max(len(values)-1, 1)) for i in range(len(values))]

    # Background block
    ax.add_patch(
        patches.Rectangle(
            (-10, y_base - bar_height/2 - 0.3),
            110, num_items * (bar_height + 0.2),
            color=cmap(0.05), zorder=0
        )
    )

    # Left-side group name label
    ax.text(-15, y_base + (num_items - 1) * (bar_height + 0.2)/2,
            f'{group}', va='center', ha='center',
            fontsize=13, weight='bold', bbox=dict(facecolor=cmap(0.2), boxstyle='round,pad=0.4', edgecolor='none'))

    for i, (label, value) in enumerate(zip(labels, values)):
        y = y_base + i * (bar_height + 0.2)
        ax.barh(y, value, height=bar_height, color=colors[i], edgecolor='black')
        ax.text(value + 1, y, f'{value}%', va='center', ha='left', fontsize=10)
        ax.text(-0.5, y, label, va='center', ha='right', fontsize=10)

    y_base += num_items * (bar_height + 0.2) + group_gap

# Formatting settings
ax.set_xlim(-10, 110)
ax.set_ylim(-1, y_base)
ax.set_xticks(range(0, 101, 20))
ax.set_xticklabels([f'{x}%' for x in range(0, 101, 20)])
ax.set_yticks([])ax.set_xlabel('Percentage (%)', labelpad=15)
ax.set_title('Q1 2024 E-commerce Market Sub - category Scale Distribution (Level 2)', fontsize=14, weight='bold')
ax.invert_yaxis()
plt.tight_layout()
plt.show()