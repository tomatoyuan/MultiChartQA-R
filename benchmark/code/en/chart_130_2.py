import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Very Satisfied", "Relatively Satisfied", "Average", "Relatively Dissatisfied", "Very Dissatisfied"]
percentages = [19.1, 46.4, 26.7, 6.7, 1.1]
# Satisfaction scores for sorting (assuming high to low)
satisfaction_score = [5, 4, 3, 2, 1]

# Sort by satisfaction score
sorted_indices = np.argsort(satisfaction_score)
labels = [labels[i] for i in sorted_indices]
percentages = [percentages[i] for i in sorted_indices]
satisfaction_score = [satisfaction_score[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(8, 6))

# Draw a line chart
ax.plot(satisfaction_score, percentages, marker='o', color='orange', linewidth=2)
ax.fill_between(satisfaction_score, percentages, color='orange', alpha=0.2)

# Add data points and numerical annotations
for x, y, label in zip(satisfaction_score, percentages, labels):
    ax.scatter(x, y, color='orange', s=50)
    ax.text(x, y + 1.5, f'{y}%', ha='center', va='bottom')

# Set the x-axis labels to satisfaction levels
ax.set_xticks(satisfaction_score)
ax.set_xticklabels(labels, rotation=15)
ax.set_ylabel('Percentage (%)')
ax.set_title('Subjective Evaluation of Chinese Residents\' Sleep Quality')

plt.tight_layout()
plt.show()