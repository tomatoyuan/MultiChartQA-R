import matplotlib.pyplot as plt
import numpy as np

# Data
labels = [
    "Insufficient time",
    "Lack of energy and \n"
    "physical strength",
    "Children's learning difficulties",
    "After - school tutoring \n"
    "is too complicated",
    "Behavior management problems",
    "Health problems",
    "Difficulty in choosing \n"
    "family education methods"
]
values = [47, 40, 39, 38, 31, 28, 21]

# Set colors (gradient of red series)
colors = [
    "#FF4C4C", "#FF6666", "#FF8080", "#FF9999", "#FFB3B3", "#FFCCCC", "#FFE5E5"
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels, values, color=colors)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center')

# Beautify the chart
ax.invert_yaxis()
ax.set_xlim(0, 55)
ax.set_xlabel("Percentage (%)")
ax.set_title("Difficulties and troubles parents encounter in children's family education", fontsize=14)

plt.tight_layout()
plt.show()