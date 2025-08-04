import matplotlib.pyplot as plt
import numpy as np

# Types of content of concern
contents = ["Nutritional and healthy diet advice", "Sharing of maternal and infant knowledge and experience", "Online doctor consultations", "Prenatal psychological counseling and emotional management", 
            "Expert knowledge Q&A", "Parent - child interaction and activities", "Whole - process records of pregnancy and parenting", "Mall product purchases"]
# Corresponding proportions (%)
proportions = [33.40, 32.59, 30.75, 29.94, 29.33, 28.31, 28.11, 27.29]

x = np.arange(len(contents))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(contents, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Content that Chinese maternal and infant consumers are concerned about when using maternal and infant vertical APPs in 2025')

plt.tight_layout()
plt.show()