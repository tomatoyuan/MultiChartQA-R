import matplotlib.pyplot as plt
import numpy as np

# Data
factors = ["Maximum cruising range", "Charging time required", "Vehicle safety", "Price of new energy vehicles", 
           "Energy - saving and emission - reduction performance", "National subsidies", "Appearance of new energy vehicles", 
           "Promotion efforts of car companies", "Following the trend"]
percentages = [51.3, 46.2, 46.0, 45.1, 38.2, 35.7, 34.8, 22.9, 17.4]

x = np.arange(len(factors))

fig, ax = plt.subplots(figsize=(12, 7))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Purchase factors')
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=15, ha='right')
ax.set_title('Analysis of purchase factors of new energy vehicle users in China in 2023')

plt.tight_layout()
plt.show()