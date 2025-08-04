import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


# Data
categories = ['Firming and Anti - aging', 'Soothing and Anti - allergy', 'Nourishing and Repairing', 'Whitening and Spot - fading', 'Moisturizing']
q1_2023 = [648, 190, 297, 365, 191]
q1_2024 = [884, 215, 314, 395, 233]
growth = [q1_2024[i] - q1_2023[i] for i in range(len(q1_2023))]

x = np.arange(len(categories))
width = 0.35

# Color settings
color_2023 = '#fcd7cc'
color_2024 = '#f29676'

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, q1_2023, width, label='Number of brands in Q1 2023', color=color_2023)
bars2 = ax.bar(x + width/2, q1_2024, width, label='Number of brands in Q1 2024', color=color_2024)

# Value labels
for i in range(len(x)):
    ax.text(x[i] - width/2, q1_2023[i] + 10, str(q1_2023[i]), ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + width/2, q1_2024[i] + 10, str(q1_2024[i]), ha='center', va='bottom', fontsize=10)
    ax.annotate(f'+{growth[i]}',
                xy=(x[i] + width/2, q1_2024[i] + 40),
                xytext=(x[i] + width/2, q1_2024[i] + 60),
                ha='center',
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='black', lw=1))

# Group border areas
ax.add_patch(patches.Rectangle((-0.5, 0), 1.0, 1000, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(-0.5, 1050, 'Intensified competition', color='orangered', fontsize=12)

ax.add_patch(patches.Rectangle((1.5, 0), 1.0, 500, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(1.5, 550, 'Stable competition', color='peru', fontsize=12)

# Other settings
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=30)
ax.set_ylabel('Number of brands')
ax.set_ylim(0, 1200)
ax.set_title('[Cream Sub - category] Competition pattern of cream brands by efficacy in Q1 2024 (Major e - commerce platforms)')
ax.legend()

plt.tight_layout()
plt.show()