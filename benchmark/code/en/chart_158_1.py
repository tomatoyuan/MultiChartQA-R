import matplotlib.pyplot as plt

# Set questions and percentages (in the order of the original image, from highest to lowest)
labels = [
    'Moisture loss and dry skin',
    'Dull skin',
    'Rough and dull yellowish skin',
    'Enlarged pores',
    'Wrinkles and fine lines',
    'Loose and sagging skin',
    'Melanin precipitation and skin pigmentation',
    'Fragile skin barrier',
    'Poor metabolic capacity',
    'Other aging problems',
    'None of the above'
]
percentages = [65, 61, 59, 57, 53, 53, 51, 47, 30, 18, 2]

# Color definition (the first 3 are highlighted in golden yellow, and the rest are uniformly purple)
colors = ['#FFCC00', '#FBC02D', '#F9A825'] + ['#673AB7'] * (len(labels) - 3)

# Reverse the order: display from highest to lowest from top to bottom
labels = labels[::-1]
percentages = percentages[::-1]
colors = colors[::-1]
y_pos = range(len(labels))

# Create a figure
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(y_pos, percentages, color=colors)

# Add percentage labels
for bar, pct in zip(bars, percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f'{pct}%', va='center', fontsize=11)

# Chart style settings
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=11, rotation=20)
ax.invert_yaxis()  # The maximum value is on the top
ax.set_xlim(0, 70)
ax.set_title("Moisture loss, dullness, and rough dull yellowish skin are the most common skin aging problems people encounter", fontsize=14, weight='bold')

# Remove the border and redundant coordinates
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# Data source annotation
source_text = (
    "Data source: CBNData questionnaire survey in July 2024\n"
    "Q4. Do you face the following skin problems in your daily life?"
)
plt.figtext(0.5, -0.05, source_text, wrap=True, ha='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()