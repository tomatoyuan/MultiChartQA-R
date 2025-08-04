import matplotlib.pyplot as plt
import numpy as np

# Main ways of digital transformation
methods = [
    "Utilize artificial intelligence and machine learning", "Adopt cloud computing and SaaS services",
    "Independently develop and build digital platforms or systems",
    "Carry out relying on upstream and downstream enterprises in the supply chain",
    "Carry out using third - party e - commerce platforms",
    "Purchase general - purpose digital software or solutions",
    "Utilize industrial Internet platforms built by leading enterprises in the industry chain",
    "Purchase digital software or solutions for specific industries"
]
# Corresponding proportions (%)
proportions = [7.69, 15.60, 16.67, 17.52, 28.63, 42.95, 47.01, 53.85]

y = np.arange(len(methods))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations on the right side of the bars
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(methods)
ax.set_xlabel('Proportion (%)')
ax.set_title('Main ways of digital transformation of Chinese enterprises in 2025')

plt.tight_layout()
plt.show()