import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['Under 25', '25 - 40', 'Over 40']
percentages = [18, 37, 45]

# Draw a bar chart
x = np.arange(len(age_groups))
width = 0.5

fig, ax = plt.subplots(figsize=(8, 6))
rects = ax.bar(x, percentages, width, color=['#FF7F50', '#FFD700', '#4B0082'])

# Add title and labels
ax.set_title('Top 5 Internet Pyramid Schemes - Age Distribution of Internet Pyramid Scheme Incidents Represented by "Shanxinhui"', fontsize=14, fontweight='bold')
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Search Proportion (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(age_groups)

# Mark the percentage on the bars
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Display relevant search count information (can be shown in the title or text box, here is an example using a text box)
search_info = f'Relevant Search Count: 322,000'
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
ax.text(0.02, 0.95, search_info, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()