import matplotlib.pyplot as plt
import numpy as np

# Data
channels = ["Online Search Engines", "Social Media", "E-commerce Platform Official Channels", "Traditional News Media", "Industry Reports and Surveys", "Relatives and Friends", "Others"]
percentages = [63.0, 59.2, 55.3, 35.2, 11.4, 6.3, 0.2]

x = np.arange(len(channels))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Sources of Information')
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=15, ha='right')
ax.set_title('Main Ways for Chinese Consumers to Learn about AI E-commerce in 2024')

plt.tight_layout()
plt.show()