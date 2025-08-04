import matplotlib.pyplot as plt
import numpy as np

# Purposes for enterprises to use AI digital humans
purposes = [
    "Improve work efficiency and quality", "Enhance enterprise digitalization level", "Reduce labor costs", 
    "Product endorsement and live - streaming sales", "Reduce economic costs", "Enhance customer interaction and experience", 
    "Enhance corporate image", "Data collection and analysis", "Innovative technology application demonstration"
]
# Corresponding proportions (%)
proportions = [48.80, 43.09, 36.44, 35.37, 27.13, 23.80, 23.14, 16.22, 8.11]

x = np.arange(len(purposes))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations at the center above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center', va='center', fontsize=9)

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(purposes, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Purposes of Chinese enterprises using AI digital humans in 2025')

plt.tight_layout()
plt.show()