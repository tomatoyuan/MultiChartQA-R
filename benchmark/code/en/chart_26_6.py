import matplotlib.pyplot as plt
import numpy as np

# Gift types
gifts = ["Mobile Phone", "Chocolate", "Luggage", "Flowers", "Perfume"]
# Corresponding values of gifts
values = [430998, 416132, 411167, 323635, 124097]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))

# Define custom colors
colors = ['#FF69B4', '#FF7F50', '#FFB6C1', '#FF1493', '#DB7093']

# Plot the bars with custom colors
bars = plt.barh(gifts, values, color=colors)

# Add title and labels
plt.title('Valentine\'s Day Gift Ranking This Year', fontsize=16)
plt.xlabel('Number of Gifts', fontsize=12)
plt.ylabel('Gift Type', fontsize=12)

# Add data labels with formatted numbers
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5000, bar.get_y() + bar.get_height()/2,
             f'{width:,}', ha='left', va='center', fontsize=10)

# Format x-axis labels with thousands separator
plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Add grid lines for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Display the chart
plt.show()