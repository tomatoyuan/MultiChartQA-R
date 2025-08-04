import matplotlib.pyplot as plt
import numpy as np

# Channel names
channels = [
    "SEO", "SEM", "Email Marketing", "Social Media Ads",
    "Influencer Marketing", "Paid Ads", "Affiliate Marketing"
]

# Convert the effectiveness speed to numerical levels (1 = slow, 3 = fast)
speed_levels = [1, 3, 2, 3, 2, 3, 2]

# Convert the cost to numerical levels (1 = low, 3 = high)
cost_levels = [1, 3, 1, 2.5, 2, 3, 2.5]

x = np.arange(len(channels))
width = 0.35  # Bar width

fig, ax = plt.subplots(figsize=(12, 6))

bars1 = ax.bar(x - width/2, speed_levels, width, label='Effectiveness Speed', color='#4CAF50')
bars2 = ax.bar(x + width/2, cost_levels, width, label='Cost', color='#FF9800')

# Add text labels
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f"{bar.get_height()}", ha='center', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f"{bar.get_height()}", ha='center', fontsize=9)

# Axis settings
ax.set_ylabel('Level (1 = Low or Slow, 3 = High or Fast)', fontsize=12)
ax.set_title('Comparison of Effectiveness Speed and Cost of Each Marketing Channel', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=30, ha='right')
ax.legend()

plt.tight_layout()
plt.show()