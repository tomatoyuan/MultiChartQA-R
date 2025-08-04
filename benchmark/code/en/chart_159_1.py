import matplotlib.pyplot as plt
import numpy as np

# Data
years = [f"{y} Jan" for y in range(2014, 2025)]
users = [1869, 2094, 2320, 2804, 3212, 3478, 3726, 4214, 4632, 4770, 5036]
growth = [12.0, 10.8, 20.9, 14.5, 8.3, 7.1, 13.1, 9.9, 3.0, 5.6]

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Draw the bar chart
bars = ax.bar(years, users, color='#419D83', width=0.6)

# Add user - count labels on top of the bars
for bar, value in zip(bars, users):
    ax.text(bar.get_x() + bar.get_width()/2, value + 100,
            f"{value:,}", ha='center', va='bottom', color='white', fontsize=11)

# Add growth - rate labels (simulated with white - background circular frames)
for i, (bar, pct) in enumerate(zip(bars[1:], growth)):
    # x = bar.get_x() + bar.get_width() / 2
    x = bar.get_x() - bar.get_width() / 3
    y = 200  # Set below without compressing the main chart
    ax.text(x, y, f"+{pct:.1f}%", ha='center', va='center',
            fontsize=10, color='black',
            bbox=dict(boxstyle="circle,pad=0.3", facecolor='white', edgecolor='none'))

# Beautify the axes
ax.set_ylim(0, 5500)
ax.set_xlim(-0.5, len(years)-0.5)
ax.set_yticks([])
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, color='white', fontsize=11, rotation=30)
ax.spines[['left', 'top', 'right']].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.tick_params(axis='x', colors='white')

# Main title box in the top - left corner
plt.text(-0.5, 5300, "Jan 2024", fontsize=12, color='white',
         bbox=dict(facecolor='#1E6E57', boxstyle="round,pad=0.4"))
plt.title("Social Media Users Over the Years", fontsize=16, color='white', loc='left', pad=20)

# Data source
plt.text(-0.5, -900, "*Data Source: We Are Social", color='white', fontsize=10)

plt.tight_layout()
plt.show()