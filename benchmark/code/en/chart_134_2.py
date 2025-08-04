import matplotlib.pyplot as plt
import numpy as np

# Left: Frequency of use data
labels_freq = ["Often used", "Daily", "Occasionally", "Rarely used"]
sizes_freq = [62.3, 23.4, 12.6, 1.7]
colors_freq = ["#FF7F24", "#FFD700", "#90EE90", "#FFC0CB"]

# Right: Price acceptance data
labels_price = ["50 yuan - 99 yuan", "100 yuan - 149 yuan", "150 yuan and above", "Below 50 yuan"]
sizes_price = [46.1, 41.2, 7.0, 5.7]
colors_price = ["#FF7F24", "#FFD700", "#90EE90", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the left pie chart for frequency of use
wedges, texts, autotexts = ax1.pie(sizes_freq, colors=colors_freq, autopct='%1.1f%%', startangle=90)
ax1.set_title('Frequency of Chinese consumers using sunscreen cosmetics')
# Adjust the legend position to make the labels clearer
ax1.legend(wedges, labels_freq, title="Frequency of use", loc="center left", bbox_to_anchor=(1, 0.5))

# Draw the right pie chart for price acceptance (with 3D effect, similar to the original image)
wedges2, texts2, autotexts2 = ax2.pie(sizes_price, colors=colors_price, autopct='%1.1f%%', startangle=90,
                                      explode=[0, 0, 0, 0.1], shadow=True)
ax2.set_title('Price acceptance of Chinese consumers for \nsunscreen cosmetics (taking a 60g bottle as an example)')
ax2.legend(wedges2, labels_price, title="Price range", loc="center left", bbox_to_anchor=(1, 0.5))

# Optimize the text color of the automatic labels (distinguish between dark/light slices)
for autotext in autotexts + autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()