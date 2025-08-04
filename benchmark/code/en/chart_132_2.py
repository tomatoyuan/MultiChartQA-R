import matplotlib.pyplot as plt
import numpy as np

# Enterprise types
categories = ["State-owned enterprises", "Government agencies", "Private enterprises", "Foreign-invested enterprises", "Public institutions"]
# Proportions of each graduation year (Class of 2021, Class of 2022, Class of 2023)
percentages_2021 = [42.5, 11.4, 19.0, 11.2, 13.2]
percentages_2022 = [44.4, 9.4, 17.4, 11.9, 14.7]
percentages_2023 = [46.7, 12.5, 12.6, 14.6, 12.3]

x = np.arange(len(categories))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))

# Draw bar charts for the Class of 2021 (orange), Class of 2022 (yellow), and Class of 2023 (green)
bar_2021 = ax.bar(x - width, percentages_2021, width, color='coral', label='Class of 2021')
bar_2022 = ax.bar(x, percentages_2022, width, color='gold', label='Class of 2022')
bar_2023 = ax.bar(x + width, percentages_2023, width, color='green', label='Class of 2023')

# Add value labels
for bars in [bar_2021, bar_2022, bar_2023]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', ha='center', va='bottom')

ax.set_ylabel('Proportion (%)')
ax.set_xlabel('Enterprise types')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_title('Desired employment enterprise types of Chinese fresh graduates from 2021 to 2023')

plt.tight_layout()
plt.show()