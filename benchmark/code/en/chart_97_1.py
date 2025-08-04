import matplotlib.pyplot as plt
import numpy as np

# Education categories
education = ["High school or below", "Associate degree", "Bachelor's degree", "Master's/MBA or above"]
# Simulated percentage data (close to the original figure)
percentages = [15.0, 19.0, 54.3, 11.7]
# Custom color (adjustable)
bar_color = "#C6BF39"  # Basic green, can also change to other colors like "#FF8C00"

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a horizontal bar chart
y = np.arange(len(education))
bar_height = 0.6  # Define the bar_height variable
bars = ax.barh(y, percentages, color=bar_color, height=bar_height)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # Label position: offset 5 to the right
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(education)
# Set x-axis ticks (0 - 60%)
ax.set_xlim(0, 60)
# Set the title
ax.set_title("Educational Background of Chinese Football Fans in 2022", fontsize=14, fontweight="bold")

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()