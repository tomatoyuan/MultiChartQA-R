import matplotlib.pyplot as plt
import numpy as np

# Operator names
operators = ["China Mobile", "China Unicom", "China Telecom", "China Broadcasting Network"]
# Corresponding proportions (%)
proportions = [59.10, 38.65, 35.33, 16.27]

x = np.arange(len(operators))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(operators)
ax.set_ylabel('Proportion (%)')
ax.set_title('Communication operators commonly used by Chinese users in 2025')

plt.tight_layout()
plt.show()