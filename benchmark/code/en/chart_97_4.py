import matplotlib.pyplot as plt
import numpy as np

# Reasons for watching the game (simulated data, following the logic of the original image)
reasons = [
    "Cheer for your favorite team/player", "It has become a long - term habit",
    "Appreciate high - level teamwork", "Bring entertainment and excitement",
    "Appreciate the excellent football skills of players", "Feel the spirit of hard work and struggle",
    "Experience the sense of tension/stimulation", "Learn football skills",
    "Want to relieve stress", "Have common topics with people around",
    "The anchor/commentator is very interesting", "Kill time",
    "Watch with friends/family"
]
# Simulated percentages (can be adjusted while retaining the trend)
percentages = [81.1, 63.5, 58.9, 56.2, 
               55.3, 44.7, 37.1, 24.9, 
               23.5, 19.6, 10.2, 9.5, 3.7]

# Free color matching (avoid green, use a combination of blue and orange)
bar_colors = ["#4169E1", "#1E90FF", "#87CEFA", "#ADD8E6", 
              "#FFA07A", "#FF8C00", "#FF6347", "#FF4500", 
              "#FFD700", "#FFC107", "#DAA520", "#B8860B", "#8B4513"]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 7))  # Adjust the height for a long list

# Draw a horizontal bar chart
y = np.arange(len(reasons))
bars = ax.barh(y, percentages, color=bar_colors, height=0.6)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(
        f'{width}%', 
        xy=(width, bar.get_y() + bar.get_height()/2),
        xytext=(5, 0),  # Offset 5px to the right
        textcoords="offset points",
        ha='left', va='center',
        fontsize=8,
        color='black'
    )

# Configure the axes and title
ax.set_yticks(y)
ax.set_yticklabels(reasons, fontsize=9)  # Reduce the font size to avoid overcrowding
ax.set_title("Reasons for Chinese football fans to watch games in 2022", fontsize=14, fontweight="bold", y=1.02)

# Beautify: Hide the borders + Add horizontal gridlines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.3)  # Add auxiliary gridlines

plt.tight_layout()  # Automatically optimize the layout
plt.show()