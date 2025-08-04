import matplotlib.pyplot as plt

# Chart 4: Distribution of requirements for takeout dishes
labels = [
    "Fresh food with guaranteed ingredient quality",
    "Balanced nutrition and reasonable combination",
    "Rich taste and good flavor",
    "Wide variety and multiple choices",
    "Well - maintained food temperature",
    "Customizable food",
    "Large portion size to fill you up"
]
values = [77.2, 68.2, 68.0, 48.6, 31.9, 31.8, 23.5]

colors = plt.cm.Greens_r([0.2 + i*0.1 for i in range(len(values))])

fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.barh(labels, values, color=colors)

# Add numerical labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1.5, bar.get_y() + bar.get_height()/2,
            f'{width:.1f}%', va='center', fontsize=10)

# Chart settings
ax.set_xlim(0, 90)
ax.set_xlabel("Proportion (%)", fontsize=12)
ax.set_title("Distribution of requirements for takeout dishes", fontsize=14, weight='bold')
plt.gca().invert_yaxis()  # Invert the y - axis to place the maximum value at the top

# Data source

plt.tight_layout()
plt.show()