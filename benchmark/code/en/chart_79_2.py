import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Fish Maw", "Sea Cucumber", "Pig's Trotters", "Bird's Nest"]
# Collagen content (%); the data can be approximately the same
collagen_content = [84.0, 54.2, 11.1, 1.5]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 5))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, collagen_content, width=bar_width, color="#A4C639", label="Collagen Content (%)")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Add bottom explanatory text
ax.text(0.5, -0.25, "● The collagen content is more than 7 times that of pig's trotters", 
        ha='center', va='bottom', fontsize=10, color='green')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set y - axis label
ax.set_ylabel("Collagen Content (%)")
# Set the title
ax.set_title("Collagen Content of Fish Maw", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()