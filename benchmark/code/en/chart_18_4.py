import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ["South Korea", "Japan", "USA", "Egypt"]
costs = [31, 41, (11 + 17) / 2, 44]  # Take the average of the range for the USA

# Color scheme
colors = ['#638EC6', '#7BC67B', '#FFBC52', '#FF6F6F']

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart, add transparency and borders
bars = ax.barh(countries, costs, color=colors, alpha=0.8, edgecolor='black', linewidth=0.8)

# Add a title and labels
ax.set_title("Comparison of Marriage Costs Abroad", fontsize=16, pad=15)
ax.set_xlabel("Marriage Cost (in RMB 10,000)", fontsize=12, labelpad=10)
ax.set_ylabel("Country", fontsize=12, labelpad=10)

# Add numerical labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width:.1f}', ha='left', va='center', fontsize=10)

# Set the axis style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)

# Set the tick style
ax.tick_params(axis='both', which='major', labelsize=10)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add a background grid
plt.grid(axis='x', linestyle='--', alpha=0.3)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()