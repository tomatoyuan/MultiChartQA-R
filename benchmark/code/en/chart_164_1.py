import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Data preparation
categories = [
    "Snow travel/Skiing", "Glamping", "Water sports", "Golf", "Equestrian", "Hot air balloon",
    "Rock climbing", "Underwater sports", "Extreme sports", "Shooting",
    "Mountaineering/Hiking/Camping", "Cycling", "Fishing", "City Walk"
]
values = [38, 38, 35, 17, 6, 1, 26, 22, 9, 8, 57, 54, 35, 29]

# Category colors
colors = [
    "#EECFA1"] * 6 + ["#F4A259"] * 4 + ["#B1D8B7"] * 4  # Luxury outdoor/Professional outdoor/Mass outdoor color scheme

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(categories, values, color=colors)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1.5, bar.get_y() + bar.get_height()/2,
            f'{int(width)}%', va='center', fontsize=10)

# Chart title
ax.set_title("Distribution of outdoor sports that consumers have tried and loved", fontsize=14, fontweight='bold', loc='center', pad=20)

# Remove redundant elements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.set_xlim(0, 65)

# Category area labels (on the right)
ax.text(65.5, 2.5, "Luxury outdoor", fontsize=12, weight='bold', color='#D4A55A', va='center')
ax.text(65.5, 8.5, "Professional outdoor", fontsize=12, weight='bold', color='#D98C3A', va='center')
ax.text(65.5, 12.5, "Mass outdoor", fontsize=12, weight='bold', color='#568259', va='center')

# Add explanatory text
plt.figtext(0.01, -0.03,
            "Data source: CBNData's research on the trend of luxury outdoor clothing in China in May 2024\n"
            "Data description: Which of the following outdoor sports/activities have you tried and loved? N = 1000",
            ha='left', fontsize=9, linespacing=1.5)

plt.tight_layout()
plt.show()