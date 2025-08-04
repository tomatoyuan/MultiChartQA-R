import matplotlib.pyplot as plt
import numpy as np

# Main reasons for learning music
reasons = ["Cultivate children's interest", "Improve self - cultivation", "Acquire an extra skill", 
           "Cultivate children's spirit", "Relieve academic pressure", "Self - love for music", 
           "Get extra points for college entrance examination", "Others' children are learning", 
           "Pursue related careers", "Get close to celebrities"]
# Corresponding proportions (%)
proportions = [30.09, 28.88, 27.26, 26.18, 25.37, 25.37, 21.46, 21.46, 21.05, 20.78]

x = np.arange(len(reasons))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 0.5, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(reasons, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Main reasons for Chinese users to learn music in 2025')

plt.tight_layout()
plt.show()