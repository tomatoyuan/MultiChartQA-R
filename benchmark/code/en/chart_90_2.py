import matplotlib.pyplot as plt
import numpy as np

# Quarters
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = np.array([7.0, 5.0, 4.2, 10.9])

# Bubble size (area) is magnified based on sales for better visualization
sizes = sales * 1000  

# Bubble colors, gradient colors
colors = ['#a8d5a2', '#82c97b', '#5eb852', '#3f9137']

fig, ax = plt.subplots(figsize=(7, 5))

# x-axis values for scatter plot positions
x = np.arange(len(quarters))

# Draw the bubble chart
scatter = ax.scatter(x, sales, s=sizes, c=colors, alpha=0.7, edgecolors='white', linewidth=1.5)

# Add data labels
for i, val in enumerate(sales):
    ax.text(x[i], val + 0.3, f'{val} billion', ha='center', fontsize=10, fontweight='bold', color='#2e2e2e')

# Set the x-axis
ax.set_xticks(x)
ax.set_xticklabels(quarters, fontsize=11, color="#424242")

# Hide the y-axis ticks
ax.set_yticks([])

# Add text to indicate the total sales
total_sales = sales.sum()
ax.text(0.5, 0.9, f"Total sales in the past 4 quarters: {total_sales:.1f} billion",
        transform=ax.transAxes, fontsize=12, color='#388e3c', ha='center', va='bottom', fontweight='bold')

# Title
ax.set_title("Bubble Chart of E-commerce Beer Sales from 2021Q2 to 2022Q1", fontsize=14, fontweight='bold')

# Beautification: Hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()