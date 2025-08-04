import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Data
labels = [
    "Lose more than 500,000 followers", "Lose 300,000 - 500,000 followers", "Lose 100,000 - 300,000 followers", "Lose 0 - 100,000 followers",
    "Gain 0 - 100,000 followers", "Gain 100,000 - 300,000 followers", "Gain 300,000 - 500,000 followers", "Gain more than 500,000 followers"
]
values = [0.3, 0.4, 12.7, 38.3, 14.1, 14.1, 7.8, 12.2]
colors = ['#a0c8f0'] * 4 + ['#c09ee6'] * 4

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(range(len(labels)), values, color=colors)

# Add value labels
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{values[i]}%", va='center', fontsize=10)

# Add group annotations
ax.text(40, 1.5, "Follower - losers\nAccount for 51.7%", fontsize=12, color='white', backgroundcolor='#619de2', ha='center', va='center')
ax.text(40, 6.5, "Follower - gainers\nAccount for 48.3%", fontsize=12, color='white', backgroundcolor='#a460e8', ha='center', va='center')

# Add dashed dividing line
ax.axhline(y=3.5, color='orange', linestyle='--', linewidth=2)
ax.text(35, 5, 'Average follower gain: 351,000', fontsize=13, weight='bold')

# Format settings
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, rotation=30)
ax.invert_yaxis()
ax.set_xlim(0, 60)
ax.set_xlabel("Proportion (%)")
ax.set_title("Distribution of follower gain and loss intervals")

plt.tight_layout()
plt.show()