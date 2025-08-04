import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Data
categories = [
    "Learning Ability and\n Learning Habits",
    "Intellectual Development \nand Science Training",
    "Subject Tutoring and \nIn - class Knowledge",
    "Interest Cultivation",
    "Life Skills and Behavioral Habits",
    "Mental Health",
    "Competition and Athletic Ability",
    "Physical Fitness"
]
values = [68, 57, 54, 50, 40, 35, 26, 20]

# Color gradient setting
norm = mcolors.Normalize(vmin=min(values), vmax=max(values))
cmap = cm.Reds

# Draw the plot
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=cmap(norm(values)))

# Add value labels
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10)

# Beautify the graph
ax.set_ylabel('Attention Ratio (%)')
ax.set_title('Aspects Parents Focus on and Value in Family Education')
ax.set_ylim(0, 80)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.show()