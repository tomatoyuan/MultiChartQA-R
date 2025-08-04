import matplotlib.pyplot as plt

# Data
labels = [
    'Increased fine lines/wrinkles', 'Decreased skin elasticity', 'Excessive oil secretion', 'Rough and dull skin',
    'Enlarged pores', 'Decreased skin radiance', 'Poor complexion', 'Decreased skin moisture', 'Uneven skin tone',
    'Skin pigmentation', 'Acne and pimples', 'Skin sensitivity', 'Long - term swelling'
]
percentages = [63, 60, 59, 58, 54, 53, 53, 52, 40, 35, 33, 25, 22]

# Set colors
colors = ['#FFCC00' if i < 4 else '#673AB7' for i in range(len(labels))]

x = range(len(labels))
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(x, percentages, color=colors)

# Add percentage labels on the bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'{percentages[i]}%', ha='center', va='bottom', fontsize=11)

# Set x - axis labels
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, rotation=30, ha='right')

# Title
ax.set_title('Over 60% of people experience increased fine lines/wrinkles and decreased skin elasticity due to sleep problems',
             fontsize=14, weight='bold', pad=50)

ax.set_ylim(0, 75)
ax.set_ylabel('Percentage (%)', fontsize=12)

mid_x = (0 + 1) / 2
ax.text(mid_x-1.3, 74, 'The primary issue for \ngenerations other\n than Gen Z',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

ax.text(1.5, 72, 'More prominent \namong Gen Z, Gen 95s,\n and Gen 90s',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

# Data source footnote
plt.figtext(0.5, -0.08,
            'Data source: CBNData questionnaire survey in July 2024\nQ15. What impact do you think sleep problems (staying up late or poor sleep quality) have on your skin?',
            wrap=True, ha='center', fontsize=9, color='gray')

# Beautify
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', left=True)

plt.tight_layout()
plt.show()