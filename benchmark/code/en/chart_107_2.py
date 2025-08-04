import matplotlib.pyplot as plt
import numpy as np

# Consideration factors
factors = ["Others' evaluation", "Family sharing plan", "Price", "Customer service quality", "Privacy protection and security", "Call quality", 
           "Available package types and quantities", "Network coverage", "Signal and network speed", "Value-added services (Short numbers, video memberships, broadband, etc.)", 
           "Data traffic policies (Unused data rollover, data transfer, etc.)"]
# Corresponding proportions (%)
proportions = [17.88, 21.73, 24.84, 26.45, 26.87, 27.41, 
               29.34, 30.73, 32.66, 32.87, 34.26]

y = np.arange(len(factors))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 7))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(factors)
ax.set_xlabel('Proportion (%)')
ax.set_title('Main factors considered by Chinese users when choosing a telecom operator in 2025')

plt.tight_layout()
plt.show()