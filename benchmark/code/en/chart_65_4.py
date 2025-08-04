import matplotlib.pyplot as plt
import numpy as np

# Revenue sources
labels = ["Traffic sharing (e.g., platform ad revenue sharing programs)", 
          "Private orders (e.g., providing personalized customization services)", 
          "Content marketing (e.g., brand collaboration and promotion)", 
          "E-commerce product promotion (graphic/video/live streaming)", 
          "Knowledge payment (e.g., paid courses, premium content)", 
          "Other sources"]
# Corresponding data
sizes = [46.2, 44.5, 18.9, 16.5, 13.9, 12.0]
# Color settings, trying to be close to the original green color scheme
colors = ["#A4C639"] * len(labels)

x = np.arange(len(labels))  # Used to set x-axis positions
bar_width = 0.5  # Bar chart width

fig, ax = plt.subplots()
# Draw bar chart
bars = ax.bar(x, sizes, width=bar_width, color=colors, edgecolor="white")  

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical distance from the bar
                textcoords="offset points",
                ha='center', va='bottom')

# Set x-axis ticks and labels, rotate labels for better display
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=25, ha="right")
# Set y-axis label (original chart doesn't display y-axis label, decide whether to add based on needs)
# ax.set_ylabel("Percentage (%)")
# Set chart title
ax.set_title("Main Revenue Sources of Content Creators Who Monetize Their Content in China and Overseas")

# Beautify the chart, hide top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust layout to avoid incomplete label display
plt.show()