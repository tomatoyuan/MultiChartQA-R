import matplotlib.pyplot as plt
import numpy as np

# Data organization (grouped by category, each category contains the proportion of each tier of cities)
categories = [
    "Food and Beverage Packages", "Leisure and Entertainment", "Hotel Accommodation", "Tourism Tickets",
    "Travel and Transportation", "Life Services", "Beauty and Skin Care", "Training and Consultation"
]
# Proportions (%) of first-tier cities, new first-tier cities, second - and third - tier cities, and fourth - and fifth - tier cities under each category
data = {
    "Food and Beverage Packages": [61.8, 59.9, 72.4, 69.2],
    "Leisure and Entertainment": [56.6, 57.3, 58.6, 43.6],
    "Hotel Accommodation": [42.6, 41.4, 30.9, 35.9],
    "Tourism Tickets": [39.7, 49.7, 47.4, 20.5],
    "Travel and Transportation": [39.0, 40.8, 42.1, 48.7],
    "Life Services": [36.8, 42.0, 48.7, 48.7],
    "Beauty and Skin Care": [31.6, 35.7, 33.6, 23.1],
    "Training and Consultation": [22.9, 21.3, 23.0, 15.4]
}
# Colors corresponding to each tier of cities (consistent with the legend)
colors = ['coral', 'sandybrown', 'lightpink', 'gold']
# Labels for each tier of cities
city_labels = ["First - tier Cities", "New First - tier Cities", "Second - and Third - tier Cities", "Fourth - and Fifth - tier Cities"]

x = np.arange(len(categories))  # x - axis coordinates (one position for each category)
bar_width = 0.2  # Width of each city - type bar

fig, ax = plt.subplots(figsize=(16, 8))

# Loop to draw bars for each city type
for i in range(4):
    ax.bar(
        x + i * bar_width,  # Control the x - position of the bars to achieve grouping
        [data[cat][i] for cat in categories],  # Take the proportion of the i - th city type under each category
        width=bar_width,
        color=colors[i],
        label=city_labels[i]
    )

ax.set_title('Survey of Consumption Categories of On - site Service Users in Chinese Cities of Different Tiers in 2023', fontsize=14)
ax.set_ylabel('Consumption Proportion (%)')
ax.set_xlabel('Consumption Categories')
ax.set_xticks(x + bar_width * 1.5)  # Adjust the position of x - axis ticks to place labels in the middle of the groups
ax.set_xticklabels(categories)
ax.legend(title='City Types', loc='upper right')

# Add numerical annotations
for i in range(len(categories)):
    for j in range(4):
        value = data[categories[i]][j]
        ax.text(
            x[i] + j * bar_width,
            value + 1,
            f'{value}%',
            ha='center',
            va='bottom',
            color='black',
            fontsize=9
        )

plt.tight_layout()
plt.show()