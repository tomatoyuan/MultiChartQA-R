import matplotlib.pyplot as plt
import numpy as np

# Consumption expenditure categories
categories = [
    "Food and Tobacco", "Housing", "Transportation and Communication", "Education, Culture and Entertainment", 
    "Health Care", "Clothing", "Household Goods and Services", "Other Goods and Services"
]
# Corresponding proportion data (%)
data = [29.8, 23.4, 13.1, 10.8, 8.8, 5.9, 5.9, 2.4]
# Color setting, similar to the green color in the original image
color = "#A4C639"

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=color, edgecolor="white")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set the y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(categories)
# Hide the x-axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Composition of Per Capita Consumption Expenditure of Chinese Residents in 2021", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()