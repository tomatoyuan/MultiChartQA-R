import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Nutrition supplement", "Work - rest adjustment", "Pregnancy and childbirth knowledge", "Conception intercourse skills", "Maternity products", "Postpartum recovery", "Others"]
percentages = [88.7, 78.1, 67.9, 66.0, 52.8, 48.3, 2.3]
colors = ["#FF9933"] * len(labels)  # Uniform orange, similar to the original image style

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw the bar chart
bars = ax.barh(x, percentages, color=colors)
ax.set_ylabel('Concerned content')
ax.set_xlabel('Attention percentage (%)')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # Place "Nutrition supplement" at the top, similar to the original image order

# Add numerical annotations
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, 
            f'{width}%', ha='left', va='center')

ax.set_title('Distribution of concerns among Chinese preconception population in 2023')

plt.tight_layout()
plt.show()