import matplotlib.pyplot as plt
import numpy as np

# Left purchase reasons data
left_reasons = ["Portability", "Ease of operation", "Grip comfort", "Small and beautiful appearance", "Reduce screen time", "Low price"]
left_proportions = [73.5, 54.4, 45.2, 38.4, 24.1, 11.0]

# Right influencing factors data
right_factors = [
    "Think the brand has high influence", "Have purchased other phones of the brand before", "High cost - performance", 
    "Good after - sales service", "The system better suits personal usage habits", "Small - screen technology is leading among similar brands", 
    "Processor manufacturer"
]
right_proportions = [47.2, 46.6, 42.6, 40.2, 33.3, 19.7, 10.0]

fig = plt.figure(figsize=(16, 6))
# Left sub - plot
ax1 = fig.add_subplot(121)
y1 = np.arange(len(left_reasons))
bars1 = ax1.barh(y1, left_proportions, color='orange')
for i, proportion in enumerate(left_proportions):
    ax1.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)
ax1.set_yticks(y1)
ax1.set_yticklabels(left_reasons)
ax1.set_xlabel('Proportion (%)')
ax1.set_title('Reasons for Chinese consumers to buy small - screen phones')

# Right sub - plot
ax2 = fig.add_subplot(122)
y2 = np.arange(len(right_factors))
bars2 = ax2.barh(y2, right_proportions, color='orange')
for i, proportion in enumerate(right_proportions):
    ax2.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)
ax2.set_yticks(y2)
ax2.set_yticklabels(right_factors)
ax2.set_xlabel('Proportion (%)')
ax2.set_title('Influencing factors for Chinese consumers to choose small - screen phone brands')

plt.tight_layout()
plt.show()