import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ['≤1k', '1-2k', '2-3k', '3-4k', '4-5k', '5-8k', '8-10k', '>10k']
# Data
y_2023 = [5, 18, 19, 27, 17, 8, 4, 2]
y_2024 = [4, 15, 18, 25, 19, 13, 5, 1]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, y_2023, width, label='New Year gift spending in 2023', color='#8B0000')
bars2 = ax.bar(x + width/2, y_2024, width, label='New Year gift budget in 2024', color='#CD5C5C')

# Add value labels
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

# Set title and labels
ax.set_title('Budget distribution of the public for New Year gifts', fontsize=14)
ax.set_ylabel('Percentage')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_ylim(0, 35)

plt.tight_layout()
plt.show()