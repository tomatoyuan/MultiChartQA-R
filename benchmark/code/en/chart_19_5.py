import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Clothing and Footwear", "Furniture and Home Appliances", "Food and Fresh Produce", "Mobile Phones and Digital Products", "Beauty and Personal Care", "Medical and Health Care"]
ranks = [1, 2, 3, 4, 5, 6]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set the bar chart colors (blue gradient)
colors = plt.cm.Blues(np.linspace(0.8, 0.3, len(categories)))

# Draw a horizontal bar chart
bars = ax.barh(categories, ranks, color=colors)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2,
            f'{int(width)}', ha='left', va='center', fontsize=10)

# Set the title and axis labels
ax.set_title("Ranking of E - commerce Product Categories Regretted to Buy on Double Eleven", fontsize=16, pad=15)
ax.set_xlabel("Ranking", fontsize=12, labelpad=10)
ax.set_ylabel("Product Categories", fontsize=12, labelpad=10)

# Set the x - axis ticks
ax.set_xticks(range(1, max(ranks) + 1))

# Add grid lines to improve readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()