import matplotlib.pyplot as plt
import numpy as np

# Complaint channel data
channel_names = ["Website", "Phone", "Email, etc."]
channel_percents = [68, 22, 10]

# Create a canvas and subplot
plt.figure(figsize=(8, 6))
ax = plt.subplot(111)

# Draw a bar chart of the proportion of complaint channels
bars = ax.bar(
    channel_names, 
    channel_percents, 
    color=["#FF7F50", "#FF6347", "#FFD700"],  # Keep the original color scheme
    width=0.6  # Adjust the bar width
)

# Set the chart title and axis labels
ax.set_title("Proportion Distribution of Infringement Complaint Channels", fontsize=16, fontweight="bold", pad=15)
ax.set_ylabel("Proportion (%)", fontsize=12)
ax.set_ylim(0, 100)  # Set the y-axis range to 0 - 100%

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height + 1.5,  # Adjust the label position
        f"{height}%",
        ha="center", 
        va="bottom",
        fontsize=12
    )

# Set grid lines and background
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_axisbelow(True)  # Place the grid lines at the bottom layer

# Optimize the layout
plt.tight_layout()
plt.show()