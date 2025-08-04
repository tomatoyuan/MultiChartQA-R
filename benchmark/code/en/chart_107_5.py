import matplotlib.pyplot as plt
import numpy as np

# 5G application fields
fields = ["5G Smart Terminals", "5G Media", "Autonomous Driving", "Smart Home", "Telemedicine", "Education", "VR"]
# Corresponding proportions (%)
proportions = [44.00, 37.71, 37.71, 37.49, 36.80, 31.31, 27.09]

x = np.arange(len(fields))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(fields, rotation=30)
ax.set_ylabel('Proportion (%)')
ax.set_title('Fields of 5G Applications Expected by Chinese Users in 2025')

plt.tight_layout()
plt.show()