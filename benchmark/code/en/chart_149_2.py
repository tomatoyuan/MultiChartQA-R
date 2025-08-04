import matplotlib.pyplot as plt
import numpy as np

# --------------------- Pie chart data for "Purchase Frequency" on the left ---------------------
frequency_labels = [
    "Almost every day", "3 - 4 times a week", "1 - 2 times a week", 
    "1 - 2 times a month", "Irregular", "Rarely"
]
frequency_sizes = [11.9, 29.5, 38.3, 7.9, 10.7, 1.7]  # Percentage
frequency_colors = ["coral", "gold", "green", "brown", "olive", "darkgreen"]

# --------------------- Horizontal bar chart data for "Preferred Promotion Activities" on the right ---------------------
promotion_labels = [
    "Win a prize when opening the bottle", "Second bottle at half price", "Discount", "Free small gifts"
]
promotion_proportions = [59.2, 55.8, 50.5, 44.8]  # Percentage
promotion_colors = ["coral"] * len(promotion_labels)  # Uniform orange

# --------------------- Create a canvas (one row, two columns) ---------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Draw the pie chart for "Purchase Frequency" on the left ---------------------
wedges, texts, autotexts = ax1.pie(
    frequency_sizes, 
    colors=frequency_colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.8  # Adjust the label position to avoid overlap
)
ax1.set_title('2023 Purchase Frequency of Sugar - free Drinks by Chinese Consumers', fontsize=14)
# Adjust the legend position (outside the chart on the right)
ax1.legend(
    wedges, 
    frequency_labels, 
    title="Purchase Frequency", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)
# Optimize the label text color (use white text for dark slices and black for light ones)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the horizontal bar chart for "Preferred Promotion Activities" on the right ---------------------
x_promotion = np.arange(len(promotion_labels))
ax2.barh(x_promotion, promotion_proportions, color=promotion_colors)
ax2.set_title('2023 Preferred Promotion Activities for Sugar - free Drinks by Chinese Consumers', fontsize=14)
ax2.set_xlabel('Percentage (%)')
ax2.set_ylabel('Promotion Activity Types')
ax2.set_yticks(x_promotion)
ax2.set_yticklabels(promotion_labels)
ax2.set_xlim(0, 70)  # Adjust the x - axis range to fit the maximum proportion (59.2%)

# Add numerical labels on the right
for i, prop in enumerate(promotion_proportions):
    ax2.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# --------------------- Add sample source description ---------------------
fig.text(0.5, -0.05, 'Sample Source: Strawberry Pie Data Survey and Calculation System', 
         fontsize=10, ha='center')

plt.tight_layout()
plt.show()