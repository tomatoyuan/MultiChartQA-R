import matplotlib.pyplot as plt
import numpy as np

# Performance change categories
categories = ["Growth over 20%", "Growth within 20%", "Decline within 20%", "Decline over 20%"]
# Online learning institution data (%)
online = [51, 31, 16, 2]
# Training supplier data (%)
supplier = [16, 31, 43, 11]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a grouped bar chart
x = np.arange(len(categories))
bar_width = 0.35
online_bars = ax.bar(x - bar_width/2, online, width=bar_width, color="#C68439", label="Online Learning Institutions")
supplier_bars = ax.bar(x + bar_width/2, supplier, width=bar_width, color="#64B5F6", label="Training Suppliers")

# Add data labels for online learning institutions
for bar in online_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels for training suppliers
for bar in supplier_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set y - axis label
ax.set_ylabel("Proportion (%)")
# Set the title
ax.set_title("Performance of Online Learning Institutions and Training Suppliers in 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()