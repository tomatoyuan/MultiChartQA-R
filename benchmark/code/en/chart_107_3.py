import matplotlib.pyplot as plt
import numpy as np

# Shortcomings
shortcomings = ["Low package cost - performance ratio", "Excessive sales calls", "Poor after - sales service", 
                "Poor network speed and throttling", "Complicated business procedures", 
                "High value - added service fees", "Short call duration", 
                "Uneven network coverage (weak or unstable signal in some areas)", "Difficult package change"]
# Corresponding proportions (%)
proportions = [44.75, 38.97, 34.58, 31.69, 27.30, 25.05, 20.66, 18.31, 9.31]

x = np.arange(len(shortcomings))  # x - axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x - axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(shortcomings, rotation=15, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Deficiencies of current communication operators perceived by Chinese users in 2025')

plt.tight_layout()
plt.show()