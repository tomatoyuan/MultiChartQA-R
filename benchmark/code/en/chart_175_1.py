import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data
labels = [
    'Very confident, \n'
    'looking forward to \n'
    'rapid development',
    'Relatively confident, \n'
    'expecting steady growth',
    'Same as in 2022',
    'Less confident, \n'
    'needs time to recover'
]
values = [44.4, 43.2, 7.4, 4.9]
colors = ['#0070C0'] * 4

# Draw the plot
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(labels[::-1], values[::-1], color=colors)

# Add labels
for bar in bars:
    ax.text(
        bar.get_width() + 1,
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width():.1f}%',
        va='center',
        fontsize=12
    )

# Add a red dashed rectangle (enclosing the first two items)
# Calculate from the bottom, the total height of two bars is the height of 2 bars + spacing
y_top = bars[3].get_y() + bars[3].get_height() + 0.1
y_bottom = bars[2].get_y() - 0.1
rect = patches.Rectangle(
    (0, y_bottom), 50, y_top - y_bottom,
    linewidth=2, edgecolor='red', linestyle='--', facecolor='none'
)
ax.add_patch(rect)

# Add the label "Positive attitude"
ax.text(
    52, y_bottom + (y_top - y_bottom)/2,
    'Positive attitude 87.6%',
    color='red', fontsize=14, va='center'
)

# Beautify the plot
ax.set_xlim(0, 60)
ax.set_xlabel('Percentage (%)')
ax.set_title('Confidence of Chinese enterprises going global in 2023', fontsize=16)
plt.tight_layout()
plt.show()