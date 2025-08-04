import matplotlib.pyplot as plt
import numpy as np

# Data (Major names + Search index)
majors = [
    "Bioengineering", "International Economics and Trade", "Communication Engineering", 
    "Finance", "Business Administration", "Economics", 
    "Computer Application", "Electrical Automation"
]
search_index = [323, 712, 1060, 1374, 1241, 945, 581, 447]

# Reverse the data order (to have "Bioengineering" at the top, consistent with the original figure)
majors = majors[::-1]
search_index = search_index[::-1]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
colors = ["#99D8C9", "#4ECDC4", "#239B56", "#E74C3C", "#F39C12", "#F1C40F", "#3498DB", "#9B59B6"]
ax.barh(majors, search_index, color=colors, height=0.7)

# Add search index labels
for i, idx in enumerate(search_index):
    ax.text(idx + 20, i, str(idx), va="center", fontsize=10, fontweight="bold")

# Set the title
ax.set_title("What Happened to the Once Popular Majors?", fontsize=14, fontweight="bold", pad=20, loc="left")

# Hide the top, right borders and x-axis ticks
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])

# Adjust the font size of the y-axis ticks
ax.tick_params(axis='y', labelsize=11)

# Set the x-axis range to leave space for labels
ax.set_xlim(0, max(search_index) + 200)

plt.tight_layout()
plt.show()