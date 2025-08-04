import matplotlib.pyplot as plt
import numpy as np

# Data
causes = ["Emotional reasons", "Using mobile phones for too long before bedtime", "Work pressure", "Personal health problems",
          "Life pressure", "Environmental issues", "Diet problems", "Incorrect sleeping posture"]
proportions = [47.3, 37.7, 37.4, 32.7, 32.0, 30.8, 27.7, 21.9]

y = np.arange(len(causes))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical labels on the right side of the bars
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center')

ax.set_yticks(y)
ax.set_yticklabels(causes)
ax.set_xlabel('Proportion (%)')
ax.set_title('Main reasons for poor sleep quality among Chinese residents')

plt.tight_layout()
plt.show()