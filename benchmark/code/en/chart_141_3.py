import matplotlib.pyplot as plt
import numpy as np

# Data
sources = ["Doctors", "Maternal and Infant Professional Media Editors", "Ordinary Moms in the Same Circle", "Friends Around", "Pre - pregnancy Product Brands", "KOLs"]
percentages = [77.0, 61.1, 55.1, 44.2, 38.5, 20.4]

x = np.arange(len(sources))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange', label='Trust Percentage (%)')
ax.set_ylabel('Trust Percentage (%)')
ax.set_xlabel('Sources of Pre - pregnancy Information')
ax.set_xticks(x)
ax.set_xticklabels(sources, rotation=15, ha='right')
ax.set_title('Sources of Pre - pregnancy Information Trusted by Chinese Pre - pregnancy Population in 2023')

# Add numerical labels
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()