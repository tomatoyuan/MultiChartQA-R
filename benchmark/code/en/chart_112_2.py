import matplotlib.pyplot as plt
import numpy as np

# Handmade types
handmade_types = ["Gundam series handmade", "Game - type handmade", "Virtual character handmade", 
                  "Marvel and DC movie series handmade", "Car model handmade", 
                  "Domestic anime handmade (e.g., Qin Shi Ming Yue)", 
                  "Japanese anime handmade (e.g., Naruto)"]
# Corresponding proportions (%)
proportions = [28.94, 30.09, 32.41, 36.81, 37.04, 38.66, 38.89]

y = np.arange(len(handmade_types))  # y - axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(handmade_types)
ax.set_xlabel('Proportion (%)')
ax.set_title('Favorite handmade types of Chinese handmade consumers in 2025')

plt.tight_layout()
plt.show()