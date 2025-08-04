import matplotlib.pyplot as plt
import numpy as np

# Data definition
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = [64.3, 69.5, 91.2, 81.2]

# Axes
x = np.arange(len(quarters))

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a gradient area chart
# Use fill_between to create the bottom gradient
ax.plot(x, sales, color="#4CAF50", linewidth=2.5, marker='o', label="Sales")
ax.fill_between(x, sales, color="#C8E6C9", alpha=0.8)

# Add data labels
for i, val in enumerate(sales):
    ax.text(x[i], val + 1.5, f"{val}", ha='center', va='bottom', fontsize=10, fontweight='bold', color="#388E3C")

# Add a text description of the total sales
total_sales = sum(sales)
ax.text(0.5, 0.9, f"Total sales exceeded {total_sales:.0f} billion in the past 4 quarters",
        transform=ax.transAxes, fontsize=12, color='#0288D1', ha='center', va='bottom', fontweight='bold')

# Set the x - axis
ax.set_xticks(x)
ax.set_xticklabels(quarters, fontsize=11)

# Hide the y - axis tick marks and only set the range
ax.set_yticks([])
ax.set_ylim(0, max(sales) + 15)

# Add a title
ax.set_title("Trend of Baijiu e - commerce sales from 2021Q2 to 2022Q1", fontsize=14, fontweight="bold", pad=15)

# Beautification: Remove the frame
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# Grid lines (to enhance readability)
ax.grid(axis='y', linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()