import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Time periods (x-axis data)
hours = np.arange(0, 25, 4)
# Search heat (y-axis data, unit: ten thousand)
heat_values = [1100, 1100, 3000, 1200, 3000, 1100, 1000]

# Create a canvas
plt.figure(figsize=(8, 5), facecolor="#f5f5f5")

# Use cubic spline interpolation to generate a smooth curve
x_smooth = np.linspace(hours.min(), hours.max(), 300)
spl = make_interp_spline(hours, heat_values, k=3)  # k=3 means cubic spline
y_smooth = spl(x_smooth)

# Plot the smooth curve
plt.plot(x_smooth, y_smooth, color="#0077b6", linewidth=2.5)
# Plot the data points
plt.scatter(hours, heat_values, color="#023e8a", s=60, zorder=5)

# Set the title
plt.title("The time period with the highest World Cup search heat", fontsize=16, fontweight="bold", color="#03045e")
# Set the x-axis label
plt.xlabel("Time period", fontsize=12, color="#333333")
# Set the y-axis label
plt.ylabel("Search heat (ten thousand)", fontsize=12, color="#333333")

# Set the x-axis ticks
plt.xticks(hours)
# Set the y-axis ticks
plt.yticks([1000, 2000, 3000])

# Add grid lines
plt.grid(True, linestyle="--", alpha=0.7)

# Beautify the chart
plt.tight_layout()  # Automatically adjust the layout
plt.ylim(0, 3500)   # Set the y-axis range

# Display the chart
plt.show()