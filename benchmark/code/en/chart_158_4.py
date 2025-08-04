import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Data
labels = ['Increase within 1 hour', 'Increase 1 - 2 hours', 'Increase more than 2 hours']
sizes = [55, 28, 17]
colors = ['#D1C4E9', '#7E57C2', '#4527A0']

# Create a figure
fig, ax = plt.subplots(figsize=(7, 6))

# Draw a pie chart, use autopct to automatically display the percentage and center it
wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.5, edgecolor='white'),
    autopct='%1.0f%%',
    pctdistance=0.75
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(13)
    autotext.set_fontweight('bold')

# Left - hand text
ax.text(-1.5, 0.1, '45%', fontsize=24, fontweight='bold', color='#512DA8')
ax.text(-1.5, -0.1, 'Increase more than 1 hour', fontsize=11, color='#333333')

# Legend
ax.legend(wedges, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False, fontsize=10)

# Data source
plt.figtext(
    0.5, -0.1,
    "Data source: CBNData questionnaire survey in July 2024\nQ23. Compared with 3 - 5 years ago, how much has your average daily working hours increased?",
    wrap=True, ha='center', fontsize=9, color='gray'
)

plt.tight_layout()
plt.show()