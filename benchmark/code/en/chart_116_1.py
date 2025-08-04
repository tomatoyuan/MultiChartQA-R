import matplotlib.pyplot as plt
import numpy as np

# Purchase channels
channels = [
    "Community group buying or group buying in WeChat groups", "Supermarket", "Farmers' market", "Direct purchase from farmers or at the fields",
    "Agricultural wholesale market", "Live - streaming e - commerce or purchase on short - video platforms", "Specialty stores (such as fresh food supermarkets, fruit stores, agricultural product specialty stores, etc.)",
    "Local life service platforms (such as Meituan, Ele.me, MissFresh, etc.)", "E - commerce platforms (such as Pinduoduo, Tmall, JD.com, Suning.com, etc.)"
]
# Corresponding proportions (%)
proportions = [21.97, 22.78, 23.42, 23.75, 26.33, 27.30, 35.70, 36.35, 41.03]

y = np.arange(len(channels))  # y - axis coordinates

fig, ax = plt.subplots(figsize=(12, 8))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations on the right side of the bars
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('Proportion (%)')
ax.set_title('Channels for Chinese consumers to purchase agricultural products in 2025')

plt.tight_layout()
plt.show()