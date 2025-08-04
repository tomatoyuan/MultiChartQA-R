import matplotlib.pyplot as plt
import numpy as np

# Industry names
industries = ["Technology", "Finance", "Professional Services", "Manufacturing", "Real Estate", "Pharmaceuticals and Life Sciences"]
# Corresponding data (percentage)
data = [33.6, 21.9, 8.8, 8.2, 6.0, 4.1]
# Color settings, similar to the original green color scheme
colors = ["#A4C639"] * len(industries)

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a horizontal bar chart
y = np.arange(len(industries))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color=colors, edgecolor="white")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(industries)
# Hide x-axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Leasing Demand Share of Main Office Building Tenants in 2021", fontsize=14, fontweight="bold")

# Beautify the chart by hiding the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.show()