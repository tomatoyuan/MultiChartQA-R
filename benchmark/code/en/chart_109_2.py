import matplotlib.pyplot as plt
import numpy as np

# Platform names
platforms = ["Douyin Online Store", "Taobao", "Pinduoduo", "Kuaishou Online Store", "JD.com", "Xiaohongshu", 
             "Community Group Buying", "MissFresh", "Tmall", "Vip.com", "Suning.com", "WeChat Video Account"]
# Corresponding proportions (%)
proportions = [29.79, 25.00, 24.73, 24.20, 24.20, 23.14, 23.14, 23.14, 23.14, 20.74, 20.74, 19.95]

x = np.arange(len(platforms))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(platforms, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Commonly Used Platforms for Rural E-commerce Operators to Sell Goods in China in 2025')

plt.tight_layout()
plt.show()