import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2021', '2022', '2023']
total = [6, 42, 69]
local = [4, 25, 52]

bar_width = 0.4
y_pos = np.arange(len(years))

# Colors
total_color = '#FFDDDD'
local_color = '#E0E0E0'

# Create the chart
fig, ax = plt.subplots(figsize=(8, 5))

bars1 = ax.barh(y_pos, total, height=bar_width, color=total_color, label='Number of new raw material filings (units)')
bars2 = ax.barh(y_pos, local, height=bar_width/2, color=local_color, label='Number of new raw material filings by local enterprises (units)')

# Add value labels
for i, (b1, b2) in enumerate(zip(bars1, bars2)):
    ax.text(b1.get_width() + 1, b1.get_y() + b1.get_height()/2, f'{total[i]}', va='center', fontsize=10, color='red')
    ax.text(b2.get_width() + 1, b2.get_y() + b2.get_height()/2, f'{local[i]}', va='center', fontsize=10, color='black')

# Set title and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(years)
ax.invert_yaxis()
ax.set_xlim(0, max(total) + 15)
ax.set_title('Number of new raw material filings in the cosmetics industry', fontsize=14, loc='left', pad=20)
ax.legend()

# Add top text description
plt.figtext(0.01, -0.1, 'In 2023, a total of 69 new raw materials completed filings, of which 52 were filed by local enterprises,\n accounting for 75.36%. Compared with 2022, the number of new raw material filings by local enterprises \nincreased by 108%.',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()