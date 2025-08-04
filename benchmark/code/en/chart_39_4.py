import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Bookstore Coffee', 'Garden Coffee', 'Camping Coffee', 'Museum Coffee', 'Theater Coffee', 'Gym Coffee', 'Market Coffee', 'Temple Coffee']
values = [62, 58, 50, 47, 43, 37, 18, 17]

# Create a plotting object
fig, ax = plt.subplots()

# Draw a horizontal bar chart
bars = ax.barh(labels, values, color='#8FBC8F')  # The color can be adjusted according to actual needs

# Label the value and percentage sign on each bar
for bar, value in zip(bars, values):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{value}', ha='left', va='center', fontsize=10)

# Set the title and style
ax.set_title('Consumers\' Preferences for the Integration of Coffee Shops with Different Business Forms')
ax.spines['right'].set_visible(False)  # Hide the right border
ax.spines['top'].set_visible(False)    # Hide the top border

# Adjust the layout to make the labels more beautiful
plt.tight_layout()

# Display the chart
plt.show()