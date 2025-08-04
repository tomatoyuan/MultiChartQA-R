import matplotlib.pyplot as plt
import numpy as np

# Data about the number of champions for each surname
data = {
    "Wang": 139, "Li": 132, "Liu": 127, "Zhang": 127, 
    "Chen": 113, "Yang": 63, "Huang": 58, "Zhao": 50, 
    "Zhou": 50, "Wu": 39
}

# Extract surnames and corresponding counts
surnames = list(data.keys())
counts = list(data.values())

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(12, 7))

# Set gradient - colored columns
cmap = plt.cm.get_cmap('viridis', len(surnames))
colors = [cmap(i) for i in range(len(surnames))]
bars = ax.bar(surnames, counts, color=colors, edgecolor='black', alpha=0.8)

# Add numerical annotations
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1.5,
            f'{height}', ha='center', va='bottom', fontsize=12)

# Add title and labels
ax.set_title('Champion Surname Ranking List', fontsize=18, pad=20)
ax.set_xlabel('Surname', fontsize=14, labelpad=10)
ax.set_ylabel('Number of People', fontsize=14, labelpad=10)

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set the y - axis range
ax.set_ylim(0, max(counts) * 1.1)

# Add background color
ax.set_facecolor('#f8f9fa')

# Adjust the layout
plt.tight_layout()

# Display the graph
plt.show()