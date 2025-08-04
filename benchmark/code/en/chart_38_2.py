import matplotlib.pyplot as plt
import numpy as np

# Category names
categories = ["Silicone hydrogel", "Hydrogel", "Rigid gas-permeable", "Mixed material", "I don't know"]
# Proportion data of each category corresponding to different types of contact lenses
data = np.array([
    [20, 20, 16],
    [18, 18, 12],
    [12, 10, 12],
    [6, 6, 6],
    [8, 8, 4]
])

# Calculate the total value of each category
total_values = data.sum(axis=1)

# Sort according to the total value (descending order)
sorted_indices = np.argsort(total_values)[::-1]

# Rearrange categories and data
categories = [categories[i] for i in sorted_indices]
data = data[sorted_indices]

# Transpose the data so that each column corresponds to a type of contact lens
data = data.T

# Labels and corresponding colors for different types of contact lenses
labels = ["Transparent contact lenses", "Colored contact lenses", "Rigid contact lenses"]
colors = ["#4CAF50", "#FF9800", "#F44336"]  

# Create a chart
fig, ax = plt.subplots(figsize=(10, 6))  # Increase the width appropriately to accommodate labels

# Draw a stacked bar chart
bottom = np.zeros(len(categories))
for i in range(len(labels)):
    bars = ax.barh(categories, data[i], left=bottom, color=colors[i], label=labels[i])
    
    # Add data labels to each bar
    for bar, value in zip(bars, data[i]):
        if value > 0:  # Only display non-zero values
            ax.text(
                bar.get_x() + bar.get_width()/2,  # x position: center of the bar
                bar.get_y() + bar.get_height()/2, # y position: center of the bar
                f"{value}%",                      # Display the value and percentage sign
                ha='center', va='center',         # Horizontally and vertically centered
                color='white', fontweight='bold', # White text, bold
                fontsize=9                        # Font size
            )
    
    bottom += data[i]

# Add annotation text (adjust the position to avoid covering labels)
annotation_text = "Silicone hydrogel is mostly for heavy users\nwho wear contact lenses for 8 - 12 hours\n(TGI>100)"
ax.text(0.7, 0.85, annotation_text, transform=ax.transAxes,
        bbox=dict(facecolor='orange', alpha=0.8), fontsize=10)

# Set chart attributes
ax.yaxis.set_label_position("right")
ax.set_ylabel("Contact lens types", fontsize=12)
ax.set_xlabel("Proportion (%)", fontsize=12)
ax.set_title("Type distribution of wearers of different contact lens materials", fontsize=14, pad=15)
ax.legend(loc='center right')  # Adjust the legend position
plt.tight_layout()
plt.show()