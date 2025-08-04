import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data
labels = ['Significantly worse', 'A little worse', 'Stay the same', 'Improve a little', 'Significantly improve']
values = [2, 9, 24, 54, 11]

# Color configuration (a blue series similar to the gradient in the original image)
colors = ['#c6dbef', '#9ecae1', '#6baed6', '#3182bd', '#08519c']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(labels, values, color=colors)

# Add data labels
for bar in bars:
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width()}%', va='center', fontsize=10, color='gray')

# Highlight the "Improve a little" and "Significantly improve" areas
highlight_rect = patches.Rectangle(
    (0, 3 - 0.5), max(values) + 10, 2, linewidth=0, edgecolor=None,
    facecolor='#e5f5e0', alpha=0.4, zorder=0
)
ax.add_patch(highlight_rect)

# Title and description
plt.title("Chinese consumers are optimistic about the improvement of \ntheir financial situation by the end of 2024", fontsize=13, weight='bold')
plt.suptitle("65% of Chinese consumers are optimistic about the improvement of their financial situation by the end of 2024\nHow do you think your household's financial situation will compare to now by the end of 2024?",
             x=0.5, y=1.05, fontsize=10, color='navy', ha='center')
plt.figtext(0.99, 0.01, "Source: NIQ Consumer Outlook 2024, APAC",
            horizontalalignment='right', fontsize=9, color='gray')

plt.tight_layout()
plt.show()