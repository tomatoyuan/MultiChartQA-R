import matplotlib.pyplot as plt
import numpy as np

# Usage scenarios
scenarios = ["Listening before sleep", "Commuting to and from work", "Doing housework", "Exercising or taking a walk", "Morning and evening toiletries", 
             "Driving", "Studying or working", "Social gatherings", "Parent-child education"]
# Corresponding proportions (%)
proportions = [35.24, 31.91, 30.85, 28.99, 26.86, 24.07, 23.67, 22.61, 21.68]

x = np.arange(len(scenarios))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(scenarios, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Usage scenarios of audiobook APPs by Chinese audiobook users in 2025')

plt.tight_layout()
plt.show()