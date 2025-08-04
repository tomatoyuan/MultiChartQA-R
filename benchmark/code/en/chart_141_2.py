import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ["Graphic", "Short video", "Live broadcast", "Offline activity", "Voice course"]
percentages = [81.9, 75.5, 40.3, 40.4, 27.9]
colors = ["#FFA500"] * len(labels)  # Uniform orange

# Initialize the chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(labels) * 2)
ax.set_axis_off()  # Hide the axes

for i, (label, perc, color) in enumerate(zip(labels, percentages, colors)):
    # Draw the orange progress bar
    ax.barh(i * 2 + 1, perc, height=1.5, left=15, color=color, alpha=0.8)
    # Draw the label
    ax.text(10, i * 2 + 1.75, label, fontsize=12, va="center")
    # Draw the percentage value
    ax.text(15 + perc + 2, i * 2 + 1.75, f"{perc}%", fontsize=12, va="center", ha="left")

ax.set_title("Information form preferences of Chinese pregnancy - planning population in 2023", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()