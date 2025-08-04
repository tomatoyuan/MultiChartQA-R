import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ['Shelves', 'Contents']
# Domestic brand data
domestic_data = [22, 27]
# International brand data
international_data = [8, 3]

x = np.arange(len(categories))  # x-axis positions
width = 0.35  # Bar width

fig, ax = plt.subplots()
# Draw domestic brand bars
rects1 = ax.bar(x - width/2, domestic_data, width, label='Domestic Brands', color='#4B72C2')
# Draw international brand bars
rects2 = ax.bar(x + width/2, international_data, width, label='International Brands', color='#F08C2E')

# Add data labels to the bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set y-axis label (not clearly shown in the original chart, can be added as needed)
# ax.set_ylabel('Quantity')
# Set the chart title
ax.set_title('Proportion of Domestic & International Brands among MAT2024 TOP 30 Brands')
# Add a legend
ax.legend()

plt.tight_layout()  # Adjust the layout to ensure labels are fully displayed
plt.show()