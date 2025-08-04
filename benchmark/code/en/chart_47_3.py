import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2022, 2023, 2024]
# Transaction amount (billion yuan)
amounts = [2763, 2818, 2959]

x = np.arange(len(years))
width = 0.5

fig, ax = plt.subplots(figsize=(10, 6))
rects = ax.bar(x, amounts, width, label='Transaction Amount', color='#D9B3A6')

# Label the transaction amount
for rect, amount in zip(rects, amounts):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height + 5,
            f'{amount}', ha='center', va='bottom')

# Set the Y-axis range to magnify the height difference
ax.set_ylim(2700, 3000)

ax.set_ylabel('Unit: Billion Yuan')
ax.set_title('Trend of Skincare Product Retail Sales Scale from 2022 to 2024')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()