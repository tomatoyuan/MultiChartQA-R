import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Equestrian', 'Golf', 'Glamping', 'Water Sports', 'Extreme Sports', 'Rock Climbing']
values = [181, 123, 120, 111, 120, 117]
categories = ['Luxury Outdoor'] * 4 + ['Professional Outdoor'] * 2
colors = ['#d7a970'] * 4 + ['#f2c56d'] * 2

fig, ax = plt.subplots(figsize=(9, 8))

# Draw horizontal bars
bars = ax.barh(activities, values, color=colors)

# Add value labels to bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{int(width)}',
            va='center', ha='left', fontsize=10, color='white', fontweight='bold')

# Add category background bands
ax.axhspan(-0.5, 3.5, facecolor='#3b2d44', alpha=0.3)
ax.axhspan(3.5, 5.5, facecolor='#3a2b1f', alpha=0.3)

# Add category labels (centered vertically in each band)
ax.annotate('Luxury Outdoor', xy=(150, 1.5), ha='center', va='center', fontsize=12, color='white', fontweight='bold')
ax.annotate('Professional Outdoor', xy=(150, 4.5), ha='center', va='center', fontsize=12, color='white', fontweight='bold')

# Title
ax.set_title('Highly Preferred Outdoor Scenarios', fontsize=16, fontweight='bold', pad=15)

# Style settings
ax.invert_yaxis()
ax.set_xlim(0, 200)
ax.set_xticks([])
y_pos = np.arange(len(activities))
ax.set_yticks(y_pos)
ax.set_yticklabels(activities, fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.figtext(0.02, 0.02,
    'Data Source: CBNData May Survey\n'
    'Data Explanation: Preference TGI = (Proportion of this group choosing this scenario / Proportion of all consumers choosing this scenario) * 100. '
    'TGI > 100 indicates preference.',
    fontsize=9, ha='left', va='bottom', wrap=True)

plt.tight_layout()
plt.subplots_adjust(bottom=0.18)

plt.show()