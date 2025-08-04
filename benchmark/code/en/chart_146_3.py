import matplotlib.pyplot as plt
import numpy as np

# Data preparation (Online and offline entertainment activities and their proportions)
online_data = {
    "Watching TV shows and movies": 73.2, "Watching short videos": 59.0, "Listening to music": 46.0,
    "Watching live - streams": 42.3, "Reading news": 39.3, "Browsing content communities": 32.5,
    "Reading e - books like novels and comics": 31.8, "Playing games": 31.5, "Browsing Weibo": 19.72, "Others": 0.14
}
offline_data = {
    "Watching movies in the cinema": 51.91, "Exercising and fitness": 45.53, "Gathering with friends": 40.99,
    "Going to KTV": 31.63, "Visiting bookstores": 30.07, "Going to bars": 29.50, "Square dancing": 26.38,
    "Night market activities": 25.96, "Music festivals": 15.32, "Escape rooms": 14.61, "Scripted murder mystery games": 11.63,
    "Night - time museums": 11.06, "Paid study rooms": 5.96, "Others": 0.57
}
# Ring proportion
online_ring = 24.4
offline_ring = 34.9

# Create a canvas with a one - row, two - column layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

# --------------------- Draw the horizontal bar chart of online entertainment on the left ---------------------
x_online = list(online_data.values())
y_online = list(online_data.keys())
ax1.barh(y_online, x_online, color='orange')
ax1.set_title('2023 Preferences of Chinese residents for online entertainment at night', fontsize=12)
# Add numerical labels
for i, val in enumerate(x_online):
    ax1.text(val + 1, i, f'{val}%', ha='left', va='center', color='orange')
# Draw the ring proportion
ax1_ring = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax1.add_artist(ax1_ring)
ax1.text(-0.3, -0.3, f'{online_ring}%', ha='center', va='center', fontsize=14, color='orange')
ax1.text(-0.3, -0.5, 'Online entertainment', ha='center', va='center', fontsize=12)

# --------------------- Draw the horizontal bar chart of offline entertainment on the right ---------------------
x_offline = list(offline_data.values())
y_offline = list(offline_data.keys())
ax2.barh(y_offline, x_offline, color='gold')
ax2.set_title('2023 Preferences of Chinese residents for offline entertainment at night', fontsize=12)
# Add numerical labels
for i, val in enumerate(x_offline):
    ax2.text(val + 1, i, f'{val}%', ha='left', va='center', color='gold')
# Draw the ring proportion
ax2_ring = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax2.add_artist(ax2_ring)
ax2.text(-0.3, -0.3, f'{offline_ring}%', ha='center', va='center', fontsize=14, color='gold')
ax2.text(-0.3, -0.5, 'Offline entertainment', ha='center', va='center', fontsize=12)

# Adjust the layout
plt.suptitle('2023 Preferences of Chinese residents for online and offline entertainment at night', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()