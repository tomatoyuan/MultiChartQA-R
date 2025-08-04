import matplotlib.pyplot as plt
import numpy as np

# Channels
channels = ['Social Media', 'Influencers', 'Messaging Apps', 'Live Video', 'Video/Live Chat', 'Voice Assistants', 'Chat']
# Data for the discovery stage
discover = [50, 22, 14, 11, 8, 0, 0]
# Data for the purchase stage
purchase = [59, 0, 36, 21, 20, 24, 20]

# Positions on the x - axis
x = np.arange(len(channels))
bar_width = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(x - bar_width/2, discover, width=bar_width, label='Discovery', color='#009800')
bars2 = ax.bar(x + bar_width/2, purchase, width=bar_width, label='Purchase', color='#005B4C')

# Add numerical labels
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{int(height)}%', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{int(height)}%', ha='center', va='bottom', fontsize=10)

# Other settings
ax.set_xticks(x)
ax.set_ylim(0, 70)
ax.set_xticklabels(channels, rotation=20)
ax.set_ylabel('Percentage (%)')
ax.set_title('Global Shoppers Using Specific Channels for Product Discovery and Purchase')
ax.legend()
plt.tight_layout()
plt.show()