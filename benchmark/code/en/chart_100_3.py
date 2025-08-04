import matplotlib.pyplot as plt
import numpy as np

# Generation classification
generations = ["Post - 00s", "Post - 90s", "Post - 80s", "Post - 70s", "Post - 60s+"]
# Simulate sleep score data (close to the original image)
scores = [81.7, 82.7, 83.0, 83.3, 83.5]
# Free color matching (can be adjusted, using green series as an example)
bar_color = "#A4C639"  

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart
x = np.arange(len(generations))  
bar_width = 0.5  
bars = ax.bar(x, scores, width=bar_width, color=bar_color)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(generations)
# Set y - axis ticks (80 - 85, adapting to the data)
ax.set_ylim(80, 85)
# Set the title
ax.set_title("Sleep Scores of Different Generations", fontsize=14, fontweight="bold")

# Beautification: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()