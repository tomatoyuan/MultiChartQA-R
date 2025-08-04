import matplotlib.pyplot as plt

# Data
categories = [
    "Spring Festival, \nMid - Autumn Festival, \nDragon Boat Festival",
    "Birthday, Wedding, Anniversary",
    "Valentine's Day, Qixi Festival",
    "Father's Day, Mother's Day",
    "Christmas, New Year's Day",
    "Double 11, 618 \nShopping Festival"
]
values = [96, 92, 81, 76, 53, 48]

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(categories, values, color="#8B0000")
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Proportion (%)")
ax.set_title("Distribution of Gift - giving Festivals in China's Gift Economy", fontsize=14)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center')

plt.tight_layout()
plt.show()