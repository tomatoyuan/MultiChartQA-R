import matplotlib.pyplot as plt
import numpy as np

# Snack categories
categories = ['Sweet drinks', 'Chewy snacks', 'Fried puffed foods', 'Yogurt', 'Baked goods', 'Nuts', 'Spicy snacks', 'High - sugar foods', 'Dried fruits and candied fruits']
# Corresponding selection percentages
percentages = [55, 43, 43, 42, 42, 39, 38, 36, 33]

x = np.arange(len(categories))  # x-axis coordinates

fig, ax = plt.subplots()
# Draw a bar chart
rects = ax.bar(x, percentages, color='green')

# Add title and axis labels
ax.set_title('Snack selection distribution of "punk overtime workers" when they have a craving at work')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=25, ha='right')
ax.set_ylabel('Selection percentage (%)')

# Label the values on the bars
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()