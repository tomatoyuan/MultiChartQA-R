import matplotlib.pyplot as plt
import numpy as np

# --------------------- Purchase frequency pie chart data ---------------------
frequency_labels = ["Once a month", "Once every 2 - 3 months", "Once a week", "2 - 3 times a week or more", "Once every six months", "Almost never buy"]
frequency_sizes = [31.0, 23.7, 16.2, 6.2, 9.6, 2.7]  # Sort data in the order of the legend
frequency_colors = ["#32CD32", "#8B4513", "#FFD700", "#FF7F50", "#D2B48C", "#8F9779"]

# --------------------- Acceptable unit price bar chart data ---------------------
price_labels = ["10 yuan and below", "11 - 30 yuan", "31 - 50 yuan", "51 - 100 yuan", "101 - 150 yuan", "151 - 200 yuan", "Above 200 yuan"]
price_percents = [2.1, 10.2, 25.5, 32.3, 15.7, 8.3, 5.9]

# Create a canvas with a 1 - row, 2 - column layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Draw the purchase frequency pie chart (left chart) ---------------------
wedges, texts, autotexts = ax1.pie(frequency_sizes, colors=frequency_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Frequency of Chinese consumers purchasing cultural and creative products in 2023')
# Adjust the legend (match in the order of the original chart)
ax1.legend(wedges, frequency_labels, title="Purchase frequency", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the acceptable unit price bar chart (right chart) ---------------------
x = np.arange(len(price_labels))
bars = ax2.bar(x, price_percents, color='orange')
ax2.set_title('Acceptable unit price of cultural and creative products for Chinese consumers in 2023')
ax2.set_ylabel('Percentage (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(price_labels, rotation=45, ha='right')
# Add numerical annotations
for i, percent in enumerate(price_percents):
    ax2.text(i, percent + 1, f'{percent}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()