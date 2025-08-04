import matplotlib.pyplot as plt
import numpy as np

# Beer selling points
selling_points = [
    "Rich taste", "High - concentration malt juice", "Brewed with traditional process", 
    "Pure ingredient list", "Natural ingredients", "Low alcohol content, no hangover", 
    "Light burden, such as low - calorie, low - fat, low - sugar", "Shorter shelf life, fresher", 
    "Brewed with high - tech process", "High - value wine body"
]
# Proportion of each selling point (%)
percentages = [32.0, 26.0, 24.4, 23.0, 22.9, 22.4, 19.6, 19.2, 18.4, 16.0]

# Create a canvas and subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(selling_points))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#C6AE39")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(selling_points)
# Set x - axis label
ax.set_xlabel("Beer selling points for which consumers are willing to pay a higher price (%)")
# Set the title
ax.set_title("Top 10 beer selling points for which consumers are willing to pay a higher price", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()