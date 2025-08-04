import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Qingming 2023', 'Labor Day 2023', 'Dragon Boat Festival 2023', 'Mid - Autumn Festival & National Day 2023', 'New Year\'s Day 2024', 'Qingming 2024']
people_pct = [68.0, 119.1, 112.8, 104.1, 109.4, 111.5]
income_pct = [39.2, 100.7, 94.9, 101.5, 105.6, 112.7]

x = np.arange(len(labels))
width = 0.35

# Color settings (Blue - green color scheme)
colors_people = '#0072B2'  # Blue
colors_income = '#009E73'  # Green

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, people_pct, width, label='Traveler volume recovery compared to 2019', color=colors_people)
bars2 = ax.bar(x + width/2, income_pct, width, label='Tourism revenue recovery compared to 2019', color=colors_income)

# Add text labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Detail settings
ax.set_ylabel('Recovery compared to 2019 (%)')
ax.set_title('Travel recovery situation')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right')
ax.legend()
ax.set_ylim(0, 140)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()