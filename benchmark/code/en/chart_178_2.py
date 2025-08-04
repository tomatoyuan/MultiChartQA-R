import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['High health \nattributes of \nthe product',
              'Ready - made \ngift boxes for \nmore convenience',
              'Practical for the \ngift recipient', 'Cost - effectiveness,\n getting more for less', 'Expensive, good \nfor showing off']
values = [87, 71, 70, 58, 41]

# Create a gradient - colored bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values)

# Apply gradient color (simulated by gradient of color transparency)
for i, bar in enumerate(bars):
    bar.set_facecolor((0.6, 0, 0, 0.3 + 0.7 * values[i] / 100))  # Red channel is fixed, transparency increases with the value

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Move up 3 points
                textcoords="offset points",
                ha='center', va='bottom')

# Chart beautification
ax.set_ylabel('Attention ratio (%)')
ax.set_title('Distribution of concerns when purchasing New Year gifts (with gradient color)')
plt.xticks(rotation=20)
plt.tight_layout()

plt.show()