import matplotlib.pyplot as plt
import numpy as np

# Recruitment digital service demand types
needs = ["Efficient resume screening", "Talent aggregation and collection", "Simplify resume storage process",
         "Efficient position management", "Precise position modeling", "Precise resume parsing", "AI virtual interviewer"]
# Corresponding proportions (%)
proportions = [35.47, 33.76, 33.55, 33.12, 32.69, 31.84, 29.70]

x = np.arange(len(needs))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations, centered above the bars
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(needs, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Demand for recruitment digital services among Chinese enterprises in 2025')

plt.tight_layout()
plt.show()