import matplotlib.pyplot as plt
import numpy as np

# Data (categories and corresponding percentages, approximately close to the original data)
labels = ["More emphasis on comfort and health performance", "More emphasis on brand value and quality",
          "More emphasis on self - pleasure", "More emphasis on functionality in specific scenarios",
          "More emphasis on the composite functions of products"]
percentages = [76.0, 59.2, 52.7, 49.4, 49.1]

# Set the position for each bar (use y - axis coordinates for horizontal bar charts)
y_pos = np.arange(len(labels))

# Create a figure and an axis object
fig, ax = plt.subplots(figsize=(8, 5))  # Adjust the size to fit the original chart's scale

# Draw a horizontal bar chart. Choose a light color similar to the original chart. Here, use #D3D3D3 (a gray - like color, which can be fine - tuned according to the actual situation)
ax.barh(y_pos, percentages, color='#D3D3D3')

# Set the y - axis ticks and labels to display the categories on the left
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)

# Set the x - axis label (percentage) and adjust the font and other styles to make it closer to the original chart style
ax.set_xlabel('Percentage (%)', fontsize=10)

# Add data labels to display the percentage values on the right side of each bar
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=9)

# Hide the top and right borders to make it closer to the simple style of the original chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set the title (consistent with the original chart title)
ax.set_title('Consumers\' underwear consumption attitudes are continuously advancing, and diverse and personalized demands are increasing', fontsize=12, pad=15)

# Adjust the layout to avoid label squeezing
plt.tight_layout()

# Display the chart
plt.show()