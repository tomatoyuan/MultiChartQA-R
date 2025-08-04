import matplotlib.pyplot as plt
import numpy as np

# Sleep quality problem types
labels = ["Light sleep", "Difficulty falling asleep", "Easily awakened", "Somnolence", "Feeling fatigued after waking up", 
          "Muscle soreness and joint discomfort", "Sleep breathing disorder", "Night terror disorder", 
          "Too short sleep time", "Frequent dreaming", "Talking in sleep", "Sleepwalking disorder", "Others"]
# Proportion of each problem (%)
proportions = [32.1, 28.0, 27.7, 26.5, 26.5, 
               24.5, 23.9, 21.9, 21.7, 20.6, 
               13.1, 10.3, 4.2]

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(14, 8))

# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")

# Set the axes
ax.set_ylabel("Proportion (%)")
ax.set_xlabel("Sleep quality problem types")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')  # Rotate the labels to avoid overlap

ax.set_title("Sleep quality problems experienced by Chinese residents")

plt.tight_layout()
plt.show()