import matplotlib.pyplot as plt
import numpy as np

# Sleep problems classification (TOP10)
problems = [
    "Too short deep sleep time", "Difficulty falling asleep", "Habitually staying up late",
    "Light sleep/easily awakened", "Insufficient sleep duration", "Feeling sleepy/low - energy during the day",
    "Irregular sleep schedule", "Staying in bed/getting up late on weekends, etc.", "Having many dreams/nightmares"
]
# Simulated proportion data (close to the original figure)
percentages = [13.8, 11.7, 10.6, 10.0, 9.7, 9.5, 7.9, 7.1, 6.3]
# Free color matching (can be adjusted, using blue series as an example)
bar_color = "#CB87EB"  # Can be replaced with other colors such as "#FF8C00"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(problems))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # Label position: offset 5 to the right
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Set the y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(problems)
# Set the x - axis ticks (0 - 15%)
ax.set_xlim(0, 15)
# Set the title
ax.set_title("User - reported sleep problems (TOP10)", fontsize=14, fontweight="bold")

# Beautification: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()