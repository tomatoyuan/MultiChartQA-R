import matplotlib.pyplot as plt
import numpy as np

# Purchase situation data
purchase_labels = ["Purchased", "Not purchased, plan to purchase", "Not purchased, no plan to purchase", "Still observing"]
purchase_sizes = [51.8, 11.8, 2.9, 33.5]
purchase_colors = ["#4169E1", "#00CED1", "#FF6347", "#9370DB"]

# Purchase price range data
price_labels = ["Below 100,000", "100,000 - 200,000", "210,000 - 400,000", "410,000 - 600,000", "610,000 - 800,000", "Above 800,000"]
price_sizes = [8.7, 38.7, 37.1, 8.9, 3.9, 2.7]
price_colors = ["#90EE90", "#1E90FF", "#FFD700", "#32CD32", "#4B0082", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the purchase situation classification chart (simulate classification display with a pie chart because it is single - proportion data)
wedges, texts, autotexts = ax1.pie(purchase_sizes, colors=purchase_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Purchase Situation')
ax1.legend(wedges, purchase_labels, title="Purchase Status", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# Draw the purchase price range pie chart
wedges2, texts2, autotexts2 = ax2.pie(price_sizes, colors=price_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('Purchase Price Range')
ax2.legend(wedges2, price_labels, title="Price Range", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('2023 Survey on New - energy Vehicle Purchase Situation and Purchase Price Range in China', fontsize=14)
plt.tight_layout()
plt.show()