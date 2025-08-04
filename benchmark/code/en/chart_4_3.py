import matplotlib.pyplot as plt
import numpy as np

# Use the exact data you provided
dates = [f"5/{i}" for i in range(1, 32)]
values = [
    7200000, 7000000, 7800000, 6800000, 6500000, 6800000, 7000000, 6200000, 
    6500000, 5800000, 7000000, 500000, 7200000, 3500000, 4000000, 3000000, 
    3500000, 4500000, 5200000, 4800000, 4500000, 4300000, 5000000, 5500000, 
    6000000, 6200000, 6800000, 6000000, 6500000, 7000000, 7500000
]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 5))  # Slightly widen the canvas to accommodate more data points

# Draw a line chart with the same color and line width as the original image
ax.plot(dates, values, color="#4285f4", linewidth=2.5)

# Set the title
ax.set_title("May Medical Aesthetics Industry News Attention Trend", fontsize=14, fontweight="bold")

# Set the y-axis (Attention)
ax.set_ylabel("Attention", fontsize=12)
ax.set_ylim(0, 9000000)  # Match the y-axis range of the original image
ax.set_yticks(np.arange(0, 10000000, 1000000))  # Y-axis tick interval is 1 million

# Set the x-axis (Date) - Display a tick every 3 days
ax.set_xticks(np.arange(0, len(dates), 3))  # Display a tick every 3 days
ax.set_xticklabels([dates[i] for i in range(0, len(dates), 3)], rotation=45, ha="right")  # Rotate 45 degrees to avoid overlap

# Add grid lines
ax.grid(linestyle="--", color="gray", alpha=0.5)

# Optimize the layout
plt.tight_layout()

# Display the chart
plt.show()