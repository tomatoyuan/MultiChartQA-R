import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["AI boosts click - through rate of target group by approximately",
          "AI boosts conversion rate of target group by approximately",
          "Efficiency of target group selection increases by approximately"]
values = [20, 30, 100]  # Percentage values
colors = ["#FF99CC", "#FF99CC", "#FF99CC"]  # Similar pink colors
bar_width = 0.5  # Width of the bar chart
x = np.arange(len(labels))  # Positions on the x - axis

# Create a figure
fig, ax = plt.subplots(figsize=(8, 4))  # Adjust the canvas size, similar to the original chart's ratio

# Draw the bar chart
bars = ax.bar(x, values, width=bar_width, color=colors, edgecolor="white")

# Add a title
ax.set_title("What's the use of 'AI Audience Selection'?", fontsize=14, fontweight="bold", y=1.1)  # Position the title slightly higher

# Add data labels
for bar, value in zip(bars, values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{value}%",
            ha="center", va="bottom", fontsize=12, color="pink")

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, rotation=45, ha='right')

# Hide the y - axis (The original chart doesn't show the y - axis)
ax.yaxis.set_visible(False)

# Hide the borders (To achieve a simpler style similar to the original chart)
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()