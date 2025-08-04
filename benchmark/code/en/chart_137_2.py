import matplotlib.pyplot as plt
import numpy as np

# Data
functions = ["Shopping convenience", "Personalized service", "Interaction and social", "Service and after - sales",
             "Data security and privacy protection", "Image recognition", "Others"]
percentages = [67.2, 63.5, 48.8, 40.0, 31.6, 24.4, 0.0]

x = np.arange(len(functions))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Advantageous function types')
ax.set_xticks(x)
ax.set_xticklabels(functions, rotation=15, ha='right')
ax.set_title('Main advantageous functions of Chinese AI e - commerce attracting consumers in 2024')

plt.tight_layout()
plt.show()