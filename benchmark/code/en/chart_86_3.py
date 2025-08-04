import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2019", "2020", "2021"]
# Quantity of female variety show themes, data is consistent with the chart
quantity = [4, 7, 10]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a bar chart
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, quantity, width=bar_width, color="#C6395A")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Hide y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("SVC - Female Variety Show Theme Trend from 2019 to 2021", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()