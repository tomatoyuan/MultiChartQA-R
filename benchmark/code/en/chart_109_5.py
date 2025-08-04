import matplotlib.pyplot as plt
import numpy as np

# Promotion measures
measures = ["Introduce young talents", "Strengthen rural network infrastructure construction", "Policy and financial support from government departments", 
            "Provide high - quality e - commerce operation venues", "Strengthen training of technical and management personnel", "Support agricultural enterprises to provide more products", 
            "Regulate the e - commerce market and create a good business environment", "Industry associations provide more guidance and information"]
# Corresponding proportion (%)
proportions = [28.79, 30.30, 30.45, 31.52, 31.67, 33.18, 34.09, 34.24]

y = np.arange(len(measures))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 7))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(measures)
ax.set_xlabel('Proportion (%)')
ax.set_title('Measures considered effective in promoting the development of rural e - commerce by Chinese rural e - commerce consumers in 2025')

plt.tight_layout()
plt.show()