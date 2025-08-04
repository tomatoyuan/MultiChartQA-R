import matplotlib.pyplot as plt
import numpy as np

# Purchase Consideration Factors
factors = [
    "Taste", "Wort Concentration", "Word - of - Mouth Evaluation", "Alcohol Content", "Brewing Ingredients",
    "Aroma/Color", "Brand Awareness", "Brewing Process", "Cost - performance Ratio", "Foam Richness",
    "New Flavors/New Tastes", "Purchase Convenience", "Shelf Life", "Bottle/Packaging Appearance",
    "Advertising Endorsers, etc.", "Limited Edition/Co - branded Products", "KOL Recommendations"
]
# Percentage of each factor (%)
percentages = [
    38.4, 31.3, 29.4, 28.1, 27.3,
    27.0, 26.5, 25.8, 24.8, 22.7,
    20.5, 20.0, 17.9, 16.5,
    12.3, 11.4, 11.1
]

# Create a canvas and subplot
fig, ax = plt.subplots(figsize=(12, 6))

# Draw a bar chart
x = np.arange(len(factors))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# Add blue borders to "Taste" and "Wort Concentration"
for i in range(2):
    bars[i].set_edgecolor('blue')
    bars[i].set_linewidth(2)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Set x - axis ticks and labels, rotate the labels for better display
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
# Set the y - axis label
ax.set_ylabel("Percentage (%)")
# Set the title
ax.set_title("Beer Purchase Consideration Factors", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()