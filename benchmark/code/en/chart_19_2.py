import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ["Guangdong", "Zhejiang", "Shandong", "Beijing", "Jiangsu", "Shanghai", "Hubei", "Henan", "Anhui", "Hunan", "Jiangxi", "Fujian"]
# Simulated quantity values, sorted in descending order
values = [30, 28, 25, 24, 23, 22, 20, 12, 11, 10, 9, 8]

# Define color groups (pink, orange, light blue), sorted by numerical size
colors = ["#f9cbda"] * 3 + ["#f7c253"] * 4 + ["#c7e3ed"] * 5

# Create a canvas and an axis object
fig, ax = plt.subplots(figsize=(10, 8))

# Invert the y-axis so that larger values are on top
ax.invert_yaxis()

# Draw a horizontal bar chart
bars = ax.barh(regions, values, color=colors, edgecolor='none', alpha=0.85)

# Set the title and labels
ax.set_title("Regional Distribution of Consumers with Shopping Regrets", fontsize=16, fontweight="bold", pad=20)
ax.set_xlabel("Number of Consumers", fontsize=12, labelpad=10)

# Set the tick label size
ax.tick_params(axis='both', which='major', labelsize=11)

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add numerical labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}', ha='left', va='center', fontsize=10)

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()