import matplotlib.pyplot as plt
import numpy as np

# Data preparation
online_channels = ["E-commerce platforms", "Live streaming shopping", "Short - video shopping", "WeChat shopping", "Others"]
online_percentages = [69.4, 15.2, 10.3, 4.7, 0.4]

offline_channels = ["Malls and supermarkets", "Convenience stores", "Pedestrian streets", "Street stalls", "Others"]
offline_percentages = [65.8, 55.0, 49.8, 26.2, 0.0]

# Set up the canvas and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the bar chart for online shopping channels
x1 = np.arange(len(online_channels))
bars1 = ax1.bar(x1, online_percentages, color='orange')
ax1.set_title('Online shopping channels')
ax1.set_ylabel('Proportion (%)')
ax1.set_xticks(x1)
ax1.set_xticklabels(online_channels, rotation=45, ha='right')

# Add value labels for online shopping channels
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom')

# Draw the bar chart for offline shopping channels
x2 = np.arange(len(offline_channels))
bars2 = ax2.bar(x2, offline_percentages, color='gold')
ax2.set_title('Offline shopping channels')
ax2.set_ylabel('Proportion (%)')
ax2.set_xticks(x2)
ax2.set_xticklabels(offline_channels, rotation=45, ha='right')

# Add value labels for offline shopping channels
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom')

plt.suptitle('Distribution of online and offline night - time shopping channels among Chinese residents in 2023', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()