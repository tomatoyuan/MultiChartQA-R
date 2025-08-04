import matplotlib.pyplot as plt
import numpy as np

# Suggestions for improvement and corresponding proportion data
suggestions = [
    "Lack of teaching and other introductory knowledge", "Relevant information is not updated in time",
    "Content is cluttered and not refined enough", "Lack of entertainment functions",
    "The App is not running smoothly enough", "Inconvenient operation"
]
proportions = [47.59, 44.92, 42.25, 37.97, 36.90, 28.34]

y = np.arange(len(suggestions))

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations on the right side of the bars
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)

# Set the y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(suggestions)
ax.set_xlabel('Proportion (%)')
ax.set_title('Survey on improvement suggestions from users of Chinese securities firms\' self - operated apps')

plt.tight_layout()
plt.show()