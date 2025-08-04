import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2020", "2022", "2023", "Estimated 2025"]
# Per capita annual coffee consumption in corresponding years
data = [9.1, 11.3, 16.74, 20]
# Set a different color for the estimated data in 2025, here using orange, which can be fine - tuned according to actual needs
colors = ["#1f77b4", "#1f77b4", "#1f77b4", "#ff7f0e"]  

x = np.arange(len(years))  # Positions of the x - axis

fig, ax = plt.subplots()
# Draw a bar chart
bars = ax.bar(x, data, color=colors)  

# Set the tick labels on the x - axis
ax.set_xticks(x)
ax.set_xticklabels(years)

# Add a title
ax.set_title("Per capita annual coffee consumption in China (cups)")

# Add data labels to each bar
for bar, value in zip(bars, data):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{value}",
            ha='center', va='bottom')

# Display the chart
plt.show()