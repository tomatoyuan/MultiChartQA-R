import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Fish maw", "Hyaluronic acid water"]
# Hyaluronic acid content ratio (mg/100g), the data can be roughly the same
hyaluronic_acid = [230.0, 19.8]

# Create a canvas and sub - plots
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, hyaluronic_acid, width=bar_width, color="#C6395C", label="Hyaluronic acid content ratio (mg/100g)")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Hide y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("Hyaluronic acid content in fish maw", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()