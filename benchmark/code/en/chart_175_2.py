import matplotlib.pyplot as plt

# Data
labels = [
    'Market expansion and\n'
    ' growth opportunities',
    'Customer service',
    'Transformation, \n'
    'upgrading and innovation',
    'Promote sustainable development',
    'Supply chain',
    'Technology \n'
    'and talent resources',
    'Market demand changes',
    'Policy influence',
    'Others'
]
values = [55, 19, 7, 6, 4, 3, 3, 2, 1]
colors = ['orange', 'orange'] + ['#0070C0'] * 7  # First two are orange, the rest are blue

# Chart main body
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=colors[::-1])

# Add percentage labels
for bar in bars:
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():.0f}%', va='center', fontsize=11)

# Set axis labels and title
ax.set_xlim(0, 60)
ax.set_xlabel('Proportion (%)', fontsize=12)
ax.set_title('Core driving factors for Chinese enterprises to go global at the current stage', fontsize=14, pad=15)

# Remove the chart borders
ax.spines[['top', 'right']].set_visible(False)

# Add legend and data source
plt.figtext(0.01, -0.04, 'Legend: Core driving factors for Chinese enterprises to go global at the current stage',
            fontsize=10, ha='left')
plt.figtext(0.01, -0.08, 'Data source: Deloitte, compiled by 36Kr Research Institute',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()