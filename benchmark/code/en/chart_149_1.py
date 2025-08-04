import matplotlib.pyplot as plt
import numpy as np

# Data preparation (Channels for understanding sugar - free drinks)
understand_channels = [
    "E - commerce platforms (Taobao, Pinduoduo, etc.)", "Short - video platforms (Douyin, Kuaishou, etc.)",
    "Social platforms (WeChat, Weibo, etc.)", "Mid - and long - video platforms (Bilibili, iQiyi, etc.)",
    "Offline promotional posters or advertisements", "Recommendations from relatives and friends",
    "Community group - buying platforms", "In - store promotions"
]
understand_proportions = [52.1, 49.5, 44.5, 35.6, 33.9, 32.8, 27.2, 24.0]  # Proportion (%)

# Data preparation (Proportion of online purchase channels for sugar - free drinks)
purchase_channels = [
    "Comprehensive e - commerce platforms (Taobao, JD.com, etc.)", "New - type e - commerce platforms (Douyin, Kuaishou)",
    "Online supermarket platforms (Meituan, Ele.me, etc.)", "Community group - buying platforms", "Others"
]
purchase_proportions = [75.3, 55.8, 67.3, 42.6, 0.4]  # Proportion (%)

# Create a canvas (one row, two columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Draw the left "Understanding channels" bar chart ---------------------
x_understand = np.arange(len(understand_channels))
ax1.bar(x_understand, understand_proportions, color='coral')
ax1.set_title('2023 Chinese consumers\' channels for understanding sugar - free drinks', fontsize=14)
ax1.set_ylabel('Proportion (%)')
ax1.set_xlabel('Understanding channels')
ax1.set_xticks(x_understand)
ax1.set_xticklabels(understand_channels, rotation=45, ha='right')
ax1.set_ylim(0, 60)  # Adjust the y - axis range to fit the maximum proportion (52.1%)

# Add numerical labels on the left
for i, prop in enumerate(understand_proportions):
    ax1.text(x_understand[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# --------------------- Draw the right "Online purchase channels" radar chart ---------------------
# Number of angles for the radar chart (corresponding to the number of channels)
num_channels = len(purchase_channels)
angles = np.linspace(0, 2 * np.pi, num_channels, endpoint=False).tolist()
# Close the radar chart (connect the last point back to the first point)
purchase_proportions += purchase_proportions[:1]
angles += angles[:1]

ax2 = plt.subplot(1, 2, 2, polar=True)
ax2.fill(angles, purchase_proportions, color='orange', alpha=0.3)
ax2.plot(angles, purchase_proportions, color='orange', label='Proportion')

# Set the axis labels (channel names) of the radar chart
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(purchase_channels)
# Adjust the y - axis scale (fit the proportion range)
ax2.set_yticks(np.arange(0, 80, 10))
ax2.set_yticklabels(np.arange(0, 80, 10))

# Add numerical labels on the right
for i, (angle, prop) in enumerate(zip(angles[:-1], purchase_proportions[:-1])):
    ax2.text(angle, prop + 2, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

ax2.set_title('2023 Proportion of Chinese consumers\' online purchases of sugar - free drinks through different channels', fontsize=14, y=1.1)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()